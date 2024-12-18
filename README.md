# Fruit Image Recognition and Calorie Estimation

A Flask-based web application that identifies fruits from uploaded images, estimates their calorie content, and provides additional details like condition and description. The app uses a pre-trained **ResNet50** model for feature extraction and **cosine similarity** for matching.

## Features
- Upload fruit images to identify them.
- Get calorie content (per 100g), condition, and a brief description of the fruit.
- Powered by **Deep Learning** with ResNet50 for feature extraction.
- Dynamic handling and serving of uploaded images.
- Scalable with **Apache Spark** for large datasets.

## Technologies Used
- **Python**: TensorFlow, Flask, NumPy, Pandas, scikit-learn, Pillow
- **Deep Learning**: ResNet50 model
- **Web Framework**: Flask
- **Scalability**: Apache Spark
- **Image Similarity**: Cosine similarity for feature matching

