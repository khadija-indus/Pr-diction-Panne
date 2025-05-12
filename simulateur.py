import streamlit as st
import joblib
import numpy as np

# Chargement du modèle pré-entraîné
model = joblib.load('modele.pkl')

# Définir le style de l'application pour une vibe industrielle
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f0;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 12px;
    }
    .stTextInput input {
        background-color: #f5f5f5;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
    }
    .stTitle {
        font-size: 28px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }
    .stWrite {
        font-size: 16px;
        color: #555;
    }
    .result {
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
    }
    .error {
        background-color: #f8d7da;
        color: #721c24;
    }
    .success {
        background-color: #d4edda;
        color: #155724;
    }
    </style>
""", unsafe_allow_html=True)

# Titre de l'application
st.title("🔧 Simulateur de Prédiction de Panne - Industrie 4.0")

# Instructions
st.write("Entrez les valeurs exactes pour les paramètres suivants. Les résultats détermineront si une panne est probable.")

# Champs de saisie pour les variables
tempMode = st.number_input("TempMode (de 0 à 7)", min_value=0, max_value=7, value=0)
footfall = st.number_input("Footfall", min_value=0.0, value=100.0)
AQ = st.number_input("AQ", min_value=0.0, value=50.0)
USS = st.number_input("USS", min_value=0.0, value=50.0)
CS = st.number_input("CS", min_value=0.0, value=50.0)
VOC = st.number_input("VOC", min_value=0.0, value=50.0)
RP = st.number_input("RP", min_value=0.0, value=50.0)
IP = st.number_input("IP", min_value=0.0, value=50.0)
Temperature = st.number_input("Temperature", min_value=-50.0, value=25.0)

# Bouton pour prédire
if st.button("Prédire"):

    # Mise en forme des données d'entrée
    input_data = np.array([[tempMode, footfall, AQ, USS, CS, VOC, RP, IP, Temperature]])
    
    # Prédiction du modèle
    prediction = model.predict(input_data)[0]
    
    # Affichage du résultat
    if prediction == 1:
        st.markdown('<div class="result error">🛑 Panne probable</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result success">✅ Pas de panne</div>', unsafe_allow_html=True)
