# Mushroom Classification Web App

## Overview

This project is an end-to-end machine learning web application that predicts whether a mushroom is edible or poisonous based on its characteristics.

The application was built using a Neural Network model trained on mushroom data. Categorical features are processed using One-Hot Encoding and dimensionality reduction is performed using Principal Component Analysis (PCA). The final model is deployed through a Streamlit web interface.

## Features

* Interactive web application built with Streamlit
* Neural Network classification model using TensorFlow/Keras
* One-Hot Encoding for categorical variables
* PCA for dimensionality reduction
* User-friendly interface with descriptive mushroom characteristics
* Real-time prediction results

## Technologies Used

* Python
* Streamlit
* TensorFlow / Keras
* Scikit-learn
* Pandas
* NumPy

## Project Structure

app.py – Streamlit application

mushroom_pca_model.h5 – Trained Neural Network model

pca_model.pkl – PCA transformer

ohe.pkl – One-Hot Encoder

label_encoder.pkl – Label Encoder

requirements.txt – Required Python packages

README.md – Project documentation

## How to Run Locally

1. Clone the repository

2. Install dependencies:

pip install -r requirements.txt

3. Start the application:

streamlit run app.py

4. Open the local URL provided by Streamlit in your browser.

## Model Pipeline

1. User selects mushroom characteristics.
2. Input data is transformed using the saved One-Hot Encoder.
3. PCA reduces feature dimensionality.
4. The Neural Network generates a prediction.
5. The application displays the classification result.

## Educational Purpose

This project was developed as a machine learning and web application deployment exercise to demonstrate data preprocessing, dimensionality reduction, neural network modeling, and interactive deployment with Streamlit.

## Disclaimer

This application is intended for educational and demonstration purposes only. It should not be used to determine whether a real wild mushroom is safe to consume. Mushroom identification in real-world environments requires expert verification.
