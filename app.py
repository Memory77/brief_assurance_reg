#commande : pip install streamlit (donc streamlit s'installe à l'interieur de l'environnement virtuel)
#commande : streamlit hello pour voir si tout va bien 
#commande : streamlit run nomfichier.py pour lancer dans le navigateur

import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn

st.write("Bienvenue")

import pickle

with open('mon_modele.pkl', 'rb') as fichier:
    modele_charge = pickle.load(fichier)

# Fonction pour transformer les entrées en format compatible avec le modèle
def prepare_inputs(age, children, sex, bmi, smoker, region, bmi_smoker_interaction):

    if smoker == 'Oui':
        smoker = 1
    else:
        smoker = 0
    
    if sex == 'female':
        sex = 1
    else:
        sex = 0

    new_data = pd.DataFrame({
        'age': [age],  
        'sex': [sex],  
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],  
        'region': [region],
        'bmi_smoker_interaction': [bmi_smoker_interaction]
    })

    return new_data

# form
with st.form(key='mon_formulaire'):
    age = st.number_input(label="Entrez votre age", min_value=0, max_value=100)
    children = st.number_input(label="Nombre d'enfants", min_value=0, max_value=100)
    sex = st.selectbox(label='Genre', options=['female', 'male'])
    bmi = st.number_input(label="Entrez votre indice de masse corporelle (IMC)", min_value=0, max_value=100)
    smoker = st.selectbox(label='Etes-vous fumeur ?', options=['Oui', 'Non'])
    region = st.selectbox(label='Région', options=['southeast', 'southwest','northeast', 'northwest'])
  
    submit_button = st.form_submit_button(label='Soumettre')

# traitement apres soumission
if submit_button:
    bmi_smoker_interaction = smoker * bmi

    inputs = prepare_inputs(age, children, sex, bmi, smoker, region, bmi_smoker_interaction)

    prediction = modele_charge.predict(inputs)
    st.write(f"Prédiction : {prediction[0]}")
