#commande : pip install streamlit (donc streamlit s'installe à l'interieur de l'environnement virtuel)
#commande : streamlit hello pour voir si tout va bien 
#commande : streamlit run nomfichier.py pour lancer dans le navigateur

import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

st.write("Hello World!")

# data = np.random.normal(size=1000)
# data = pd.DataFrame(data, columns=["Dist_norm"])
# st.write(data.head())
# # or st.dataframe(data.head()) pour afficher un dataframe

# #creation d'un graphique avec matplotlib

# #plt.hist(data.Dist_norm)
# #plt.show #rien ne s'affiche car streamlit a des fonctions dédiés qui fonctionnent avec des librairies comme mtlp seaborn etc
# #st.pyplot()
# #s'affiche mais y'a un warning car besoin d'un argument qui represente la figure en question et propose un code donc on le met

# fig, ax = plt.subplots()
# ax.hist(data.Dist_norm)
# st.pyplot(fig)

# Créer un formulaire
with st.form(key='mon_formulaire'):
    age = st.number_input(label="Entrez votre age", min_value=0, max_value=100)
    children = st.number_input(label="Nombre d'enfants", min_value=0, max_value=100)
    genre = st.selectbox(label='Choisissez votre genre, femme = 1 male = 0', options=[1, 0])
    bmi = st.number_input(label="Entrez votre age", min_value=0, max_value=100)
    
    # Bouton de soumission
    submit_button = st.form_submit_button(label='Soumettre')

# Traitement après la soumission du formulaire
if submit_button:
    st.write(f'Nom: {age}')
    st.write(f'Âge: {children}')
    st.write(f'Genre: {genre}')
    st.write('Accepté:' + ('Oui' if accepte else 'Non'))