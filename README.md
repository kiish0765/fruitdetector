# fruitdetector Fruit Image Recognition and Calorie Estimation Web Application
Fruit Image Recognition and Calorie Estimation Web Application
This project is a web-based application that uses Deep Learning and Flask to recognize fruits from images and estimate their calorie content. It leverages the ResNet50 model for image feature extraction, paired with a dataset containing fruit details such as calorie values, condition, and descriptions. Additionally, the application incorporates Spark for potential scalability and cosine similarity to identify the most similar fruit in the dataset.

**Features**
Fruit Image Recognition: Upload an image of a fruit, and the application identifies the fruit.
Calorie Estimation: Provides the calorie content per 100g for the identified fruit.
Fruit Condition and Description: Displays the fruit's condition (e.g., fresh, ripe) and a brief description.
Dynamic Image Upload: Users can upload images dynamically, and the app serves the results in real time.
Pre-trained ResNet50 Model: Uses a powerful convolutional neural network for feature extraction and matching.
Dataset Integration: Includes a CSV file with information on various fruits, their conditions, calorie content, and descriptions.
**Technologies Used**
Python
Libraries: TensorFlow, NumPy, Pandas, Flask, scikit-learn, Pillow
Deep Learning
Pre-trained ResNet50 model for feature extraction
Apache Spark: Prepared for handling larger datasets
Flask Framework: Backend for handling image uploads, processing, and API responses
Frontend: HTML templates for user interaction
File Management: Dynamic handling and serving of uploaded images
Cosine Similarity: For comparing image features and finding the best match
