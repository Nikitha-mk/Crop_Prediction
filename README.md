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


# Output:
<img width="1907" height="961" alt="Screenshot 2026-03-29 233002" src="https://github.com/user-attachments/assets/b784c381-9cbd-40a9-9b96-463225a14457" />
<img width="1880" height="968" alt="Screenshot 2026-03-29 233022" src="https://github.com/user-attachments/assets/8fa69d10-80c8-4536-9dca-37b01563b66a" />


Open in browser:

http://localhost:5000
