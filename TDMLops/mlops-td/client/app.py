import streamlit as st
import requests

# Streamlit UI
st.title('Iris Flower Prediction')
sepal_length = st.slider('Longueur Sepal', 0.0, 10.0)
sepal_width = st.slider('Largeur Sepal', 0.0, 10.0)
petal_length = st.slider('Longueur Petal', 0.0, 10.0)
petal_width = st.slider('Largeur Petal', 0.0, 10.0)

# Make prediction request
if st.button('Predict'):
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post("http://server:8000/predict", json=payload)
    prediction = response.json()['predicted_class']
    st.write(f'Classe prédite: {prediction}')
