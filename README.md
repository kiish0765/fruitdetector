
# Fruit Image Recognition and Calorie Estimation

## Script Title
Fruit Image Recognition and Calorie Estimation Web App

A Flask-based web application that identifies fruits from images, estimates their calorie content, and provides details such as condition and a brief description.

---

## Prerequisites
To use this script, you need to have the following installed:
- Python 3.8 or higher
- Required modules (listed in `requirements.txt`):
  - TensorFlow
  - Flask
  - NumPy
  - Pandas
  - scikit-learn
  - Pillow
  - PySpark

Install the dependencies using:
```bash
pip install -r requirements.txt
```

Make sure the dataset file `FruitCalories_per_100g.csv` is placed in:
```
C:/Users/ADMIN/Desktop/bdt_project/FruitCalories_per_100g.csv
```

---

## How to run the script
Follow these steps to run the application:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fruit-calorie-estimator.git
   cd fruit-calorie-estimator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask server:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

5. Upload a fruit image and view the results, including:
   - Fruit name
   - Calorie content (per 100g)
   - Condition
   - Description

Example API response after uploading a fruit image:
```json
{
  "fruit": "apple",
  "calories_per_100g": 52,
  "condition": "fresh",
  "description": "A sweet, edible fruit produced by an apple tree.",
  "image_url": "/uploaded_images/your_image.jpg"
}
```

---

## Screenshot/GIF showing the sample use of the script
*home page*
![homesitefd](https://github.com/user-attachments/assets/e82250ba-c2a2-4504-b0f2-5d54935c7307)
*output page*
![outputfd](https://github.com/user-attachments/assets/87c83186-17f0-4507-94a9-f02d8482c220)
*output page*
![ouputfd2](https://github.com/user-attachments/assets/c10ad361-4def-43c5-8137-ab0300924f13)

---

## Author Name
**Kishore D**

GitHub: [simbu-kishore]([https://github.com/simbu-kishore](https://github.com/kiish0765))  
Feel free to connect or contribute to this repository!

--- 

*Contributions, issues, and feature requests are welcome!*
``` 

You can save this content as a `README.md` file in your repository. Don't forget to replace the placeholders (like `yourusername` or add the screenshot/GIF file) with actual details.
