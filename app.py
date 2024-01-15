#commande : pip install streamlit (donc streamlit s'installe à l'interieur de l'environnement virtuel)
#commande : streamlit hello pour voir si tout va bien 
#commande : streamlit run nomfichier.py pour lancer dans le navigateur

import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from feature_engine.discretisation import ArbitraryDiscretiser
import sklearn
import pickle

#fonctions
def log_transform(x):
    return np.log(x + 1)

def custom_bmi_discretizer(df):
    custom_bins = [0, 30, 100, float('inf')]
    bmi_discretizer = ArbitraryDiscretiser(binning_dict={'bmi': custom_bins}, return_object=True)
    df[['bmi']] = bmi_discretizer.fit_transform(df[['bmi']])
    return df

#app
logo = st.sidebar.image('img/assuraimant.png', width=250)
page = st.sidebar.radio("Navigation", ["Home", "Informations","Estimation"])

if page == "Home":
    st.write("<h1>Bienvenue sur Assur'Aimant</h1>", unsafe_allow_html=True)
    st.markdown('<h2>📚 Conseil Data & IA Solutions</h2>', unsafe_allow_html=True)
    st.write("Notre étude de cas avec Assur'Aimant illustre comment nous appliquons notre expertise pour analyser les données des souscripteurs et estimer précisément les primes d'assurance, en remplaçant les méthodes traditionnelles longues et coûteuses par une approche basée sur les données.")
    st.image('img/courtier-assurance.jpg', width=500)


elif page == "Informations":
    st.write("<h2>Aperçu des Facteurs Clés Influant sur l'Estimation des Primes d'Assurance</h2>", unsafe_allow_html=True)
    
    #affichage des plots
    df = pd.read_csv('dataset.csv')
    fumeurs = df[df['smoker'] == 1]
    non_fumeurs = df[df['smoker'] == 0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # tracage des points pour les fumeurs en rouge 
    ax1.scatter(fumeurs['age'], fumeurs['charges'], color='red', label='Fumeurs', alpha=0.3)

    # tracage des points pour les non-fumeurs en bleu
    ax1.scatter(non_fumeurs['age'], non_fumeurs['charges'], color='blue', label='Non-Fumeurs', alpha=0.3)

    ax1.set_xlabel('Age')
    ax1.set_ylabel('Insurance Charges')
    ax1.legend()
    ax1.set_title("Charges d'assurance pour fumeurs et non-fumeurs en fonction de l'âge")

     # tracage des points pour les fumeurs en rouge 
    ax2.scatter(fumeurs['bmi'], fumeurs['charges'], color='red', label='Fumeurs', alpha=0.3)
    # tracage des points pour les non-fumeurs en bleu
    ax2.scatter(non_fumeurs['bmi'], non_fumeurs['charges'], color='blue', label='Non-Fumeurs', alpha=0.3)

    ax2.set_xlabel('BMI')
    ax2.set_ylabel('Insurance Charges')
    ax2.legend()
    ax2.set_title("Charges d'assurance pour fumeurs et non-fumeurs en fonction de l'âge")
    st.pyplot(fig)
    st.write("Notre approche repose sur une combinaison d'analyses de données pointues et d'intelligence artificielle avancée, permettant de déterminer avec précision les primes d'assurance adaptées à chaque individu. En se basant sur des critères essentiels tels que l'âge, le statut de fumeur, l'indice de masse corporelle et d'autres facteurs démographiques, nous fournissons une estimation détaillée qui reflète non seulement le risque individuel, mais aussi une compréhension nuancée du marché de l'assurance. Plongez dans les détails de notre méthode innovante pour voir comment nous transformons les données brutes en insights stratégiques.")



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
        age = st.slider('Indiquez votre âge', 0, 100, 0)
        children = st.slider("Combien d'enfants à charge ?", 0, 20, 0)
        sex = st.selectbox(label='Genre', options=['female', 'male'])
        poids = st.number_input(label="Indiquez votre poids", min_value=0.0, max_value=200.0, format="%.2f")
        taille = st.slider('Indiquez votre taille', 0.0, 3.0, 0.0)
        smoker = st.selectbox(label='Etes-vous fumeur ?', options=['yes', 'no'])
        region = st.selectbox(label='Région', options=['southeast', 'southwest','northeast', 'northwest'])
    
        submit_button = st.form_submit_button(label='Soumettre')

    # traitement apres soumission
    if submit_button:
        bmi = poids/(taille*taille)
        inputs = prepare_inputs(age, children, sex, bmi, smoker, region)
        prediction = modele_charge.predict(inputs)
        st.write(f"Prédiction : {round(prediction[0],2)}")



st.markdown('''
<style>
.appview-container {
    background-color: rgb(228, 228, 252) ;  
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
    text-align: justify;
}
            
h1 {
    color: rgb(125, 193, 241);
}
h2 {
    color: rgb(125, 193, 241);
    padding: 20px;
    border-radius: 10px;
    text-align: justify;
    font-size: 19px;
    border-color: black;
    
}

.test {
    width: 50%;
}      
.test{
    padding-bottom : 50px;
}
            
.StyledThumbValue{
    color: black;
}
            
.block-container img {
    width : 1000px
}
</style>
''', unsafe_allow_html=True)