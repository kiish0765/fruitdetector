import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from pyspark.sql import SparkSession
from flask import Flask, request, render_template, jsonify, send_from_directory
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize Spark session
spark = SparkSession.builder.appName("Fruit Image Recognition").getOrCreate()

# Load the fruit dataset CSV
file_path = "C:/Users/ADMIN/Desktop/bdt_project/FruitCalories_per_100g.csv"
dataset_df = pd.read_csv(file_path)

# Strip any leading/trailing spaces from column names
dataset_df.columns = dataset_df.columns.str.strip()

# Clean the fruit names and image paths (e.g., convert to lowercase for uniformity)
dataset_df["Fruit"] = dataset_df["Fruit"].str.lower()
dataset_df["Condition"] = dataset_df["Condition"].str.lower()

# Load the pre-trained ResNet50 model (load once when the server starts)
model = tf.keras.applications.ResNet50(weights='imagenet', include_top=False, pooling='avg')


# Function to preprocess the image for ResNet50
def preprocess_image(image_path):
    image = Image.open(image_path).resize((224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return tf.keras.applications.resnet50.preprocess_input(image)


# Function to extract features from an image
def extract_features(image_path):
    preprocessed_image = preprocess_image(image_path)
    features = model.predict(preprocessed_image)
    return features.flatten()


# Function to find the best match from the dataset, including description
def find_similar_fruit(image_path):
    input_features = extract_features(image_path)
    dataset_features = []
    dataset_image_paths = dataset_df["IMAGES"].str.strip().tolist()

    # Ensure image paths are correct and cleaned up
    dataset_image_paths = [path.strip().replace('"', '') for path in dataset_image_paths]

    for img_path in dataset_image_paths:
        try:
            features = extract_features(img_path)
            dataset_features.append(features)
        except Exception as e:
            print(f"Error processing {img_path}: {e}")
            dataset_features.append(np.zeros_like(input_features))

    similarities = cosine_similarity([input_features], dataset_features)
    best_match_index = np.argmax(similarities)
    row = dataset_df.iloc[best_match_index]

    # Get fruit name, calories, condition, and description from CSV
    fruit_name = row["Fruit"]
    calories = row["Calories_per_100g"]
    condition = row["Condition"]
    description = row["Description"]  # Assuming this column exists in your CSV

    return fruit_name, calories, condition, description


# Route for the main page
@app.route('/')
def home():
    return render_template('index1.html')


# Route for handling file upload and processing
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    # Ensure the upload directory exists
    upload_folder = "C:/Users/ADMIN/Desktop/hehe/uploaded_images"  # Save to static folder for access from frontend
    os.makedirs(upload_folder, exist_ok=True)

    # Save the uploaded file with a dynamic filename
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Predict fruit and calories
    try:
        fruit_name, calories, condition, description = find_similar_fruit(file_path)
        # Convert numpy types to native Python types (e.g., int64 to int)
        calories = int(calories)

        # Return the result as JSON, including the image path and description
        return jsonify({
            "fruit": fruit_name,
            "calories_per_100g": calories,
            "condition": condition,
            "description": description,  # Add the description here
            "image_url": f'/uploaded_images/{file.filename}'  # Return the relative path to the uploaded image
        })
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"})


# Serve the uploaded images
@app.route('/uploaded_images/<filename>')
def uploaded_file(filename):
    upload_folder = "C:/Users/ADMIN/Desktop/hehe/uploaded_images"
    return send_from_directory(upload_folder, filename)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
