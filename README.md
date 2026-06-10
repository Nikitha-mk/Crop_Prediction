# 🌱 Crop Recommendation System

A Machine Learning-based Crop Recommendation System that predicts the most suitable crop to cultivate based on soil nutrient composition and environmental conditions. The application uses a K-Nearest Neighbors (KNN) classification model and provides real-time recommendations through an interactive Flask web interface.

---

## 🔗 Live Demo

**Application:** https://crop-prediction-7k56.onrender.com

---

## ☁️ Deployment

The application is deployed on Render and can be accessed online without local installation.

**Deployment Platform:** Render

---

## 📌 Overview

Selecting the right crop is a critical factor in improving agricultural productivity. This project leverages Machine Learning to analyze soil nutrients and environmental conditions and recommend the most suitable crop for cultivation. The system provides real-time predictions through a simple and user-friendly web interface.

---

## 🚀 Features

- Real-time crop recommendation
- Interactive Flask-based web application
- Predicts among 22 crop categories
- Uses K-Nearest Neighbors (KNN) Machine Learning model
- Displays crop-specific images with prediction results
- Input validation and error handling
- Fast and reliable prediction performance
- Cloud deployment for public accessibility

---

## 🧠 Input Parameters

The model uses the following parameters:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH Value
- Rainfall (mm)

---

## 🌾 Supported Crops

The system can recommend the following crop categories:

- Rice
- Maize
- Chickpea
- Kidney Beans
- Pigeon Peas
- Moth Beans
- Mung Bean
- Black Gram
- Lentil
- Pomegranate
- Banana
- Mango
- Grapes
- Watermelon
- Muskmelon
- Apple
- Orange
- Papaya
- Coconut
- Cotton
- Jute
- Coffee

---

## 🛠️ Technology Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- K-Nearest Neighbors (KNN)

### Data Processing
- NumPy
- Joblib

### Frontend
- HTML
- CSS
- Jinja2 Templates

### Version Control
- Git
- GitHub

### Deployment
- Render

---

## 📂 Project Structure

```text
Crop_Prediction/
│
├── app.py
├── knncropmodel.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index2.html
│
└── static/
    ├── bg2.jpg
    ├── apple.jpg
    ├── banana.jpg
    ├── coffee.jpg
    ├── cotton.jpg
    ├── rice.jpg
    └── ...
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Nikitha-mk/Crop_Prediction.git
cd Crop_Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Access the Application

Open your browser and visit:

```text
http://localhost:5000
```

Or access the deployed application:

```text
https://crop-prediction-7k56.onrender.com
```

---

## 📊 Model Details

| Attribute | Description |
|------------|------------|
| Algorithm | K-Nearest Neighbors (KNN) |
| Input Features | 7 |
| Output Classes | 22 Crop Categories |
| Model Storage | Joblib |
| Task Type | Multi-Class Classification |

---

## 📸 Screenshots

### Home Page
<img width="1864" height="977" alt="Screenshot 2026-06-10 163800" src="https://github.com/user-attachments/assets/b9fd1765-10f7-421a-86b7-4c98335b573c" />



### Prediction Result

<img width="1893" height="906" alt="Screenshot 2026-06-10 163902" src="https://github.com/user-attachments/assets/02cc7d72-0f1a-454f-915e-c7170f545f0e" />


---

## 🔮 Future Enhancements

- Weather API integration
- Fertilizer recommendation system
- Crop yield prediction
- Soil health analysis
- Mobile-responsive UI improvements
- Comparison of multiple Machine Learning models
- Enhanced analytics and visualization

---

## 👩‍💻 Author

**Nikitha M K**

GitHub Profile: https://github.com/Nikitha-mk

Project Repository: https://github.com/Nikitha-mk/Crop_Prediction



---

## 📜 License

This project is developed for educational and academic purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
