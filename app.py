#commande : pip install streamlit (donc streamlit s'installe à l'interieur de l'environnement virtuel)
#commande : streamlit hello pour voir si tout va bien 
#commande : streamlit run nomfichier.py pour lancer dans le navigateur

import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
import pickle

def log_transform(x):
    return np.log(x + 1)



logo = st.sidebar.image('assuraimant.png', width=250)
page = st.sidebar.radio("Navigation", ["Home", "Informations","Estimation"])

if page == "Home":
    st.write("<h1>Bienvenue sur Assur'Aimant</h1>", unsafe_allow_html=True)
    st.write("<div class='test'><h2>Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page, le texte définitif venant remplacer le faux-texte dès qu'il est prêt ou que la mise en page est achevée. Généralement, on utilise un texte en faux</h2></div>", unsafe_allow_html=True)
    st.image('courtier-assurance.jpg', width=500)

elif page == "Estimation":
    with open('best_model.pkl', 'rb') as fichier:
        modele_charge = pickle.load(fichier)

    # fonction pour transformer les entrées en format compatible avec le modèle
    def prepare_inputs(age, children, sex, bmi, smoker, region):
        
        new_data = pd.DataFrame({
            'age': [age],  
            'sex': [sex],  
            'bmi': [bmi],
            'children': [children],
            'smoker': [smoker],  
            'region': [region],
        })

        return new_data

    # form
    with st.form(key='mon_formulaire'):
        age = st.number_input(label="Entrez votre age", min_value=0, max_value=100)
        children = st.number_input(label="Nombre d'enfants", min_value=0, max_value=100)
        sex = st.selectbox(label='Genre', options=['female', 'male'])
        poids = st.number_input(label="Indiquez votre poids", min_value=0.0, max_value=100.0, format="%.2f")
        taille = st.number_input(label="Indiquez votre taille", min_value=0.0, max_value=100.0, format="%.2f")
        smoker = st.selectbox(label='Etes-vous fumeur ?', options=['Oui', 'Non'])
        region = st.selectbox(label='Région', options=['southeast', 'southwest','northeast', 'northwest'])
    
        submit_button = st.form_submit_button(label='Soumettre')

    # traitement apres soumission
    if submit_button:
        bmi = poids/(taille*taille)
        inputs = prepare_inputs(age, children, sex, bmi, smoker, region)
        prediction = modele_charge.predict(inputs)
        st.write(f"Prédiction : {prediction[0]}")



st.markdown('''
<style>
.appview-container {
    # background-image: url("courtier-assurance.jpg") !important;
    # background-attachment: fixed !important;
    # background-position: center !important;
    # background-repeat: no-repeat !important;
    # background-size: cover !important;
    # height: 100vh;
    background-color: rgb(205, 197, 246);  
}

//sidebar
.eczjsme3 {
    background-color: black;       
} 
#stForm{
    background-color : black;
            }
//form
.e10yg2by1 {
    background-color: white;   
}
            
p {
    font-size: 20px;
}
            
h1 {
    color: white;
}
h2 {
    background-color: white;
    color: black;
    padding: 20px;
    border-radius: 10px;
    text-align: justify;
    font-size: 18px;
    border-color: black;
}

            
.test{
    padding-bottom : 50px;
}
</style>
''', unsafe_allow_html=True)