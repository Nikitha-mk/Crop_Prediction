# 🌱 Crop Recommendation System (Flask + ML)

This project is a Machine Learning-based Crop Recommendation System built using Flask. It predicts the most suitable crop to grow based on soil nutrients and environmental conditions like temperature, humidity, pH, and rainfall.

---

## 🚀 Features

- Predicts the best crop based on input data  
- Uses K-Nearest Neighbors (KNN) model  
- Simple and interactive web interface  
- Fast and real-time predictions  
- Handles invalid input errors  

---

## 🧠 Input Parameters

The model takes the following inputs:

- Nitrogen (N)  
- Phosphorus (P)  
- Potassium (K)  
- Temperature (°C)  
- Humidity (%)  
- pH value  
- Rainfall (mm)  

---

## 🖥️ Tech Stack

- Backend: Python, Flask  
- Machine Learning: Scikit-learn (KNN)  
- Frontend: HTML (Jinja Templates)  
- Model Storage: Joblib  

---

## 📂 Project Structure
project-folder/
│── app.py
│── knncropmodel.pkl
│── templates/
│ └── index2.html
│── static/
│── README.md

Open in browser:

http://localhost:5000
