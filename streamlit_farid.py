import streamlit as st
import joblib 
import pandas as pd
from sklearn.preprocessing import FunctionTransformer

from joblib import dump 

from model_lasso import y_pred
from numpy import np



 
modele = joblib.load('/home/utilisateur/Documents/dev ia/brief_assurance_reg/model.pkl')

def log_transform(x):
    return np.log(x + 1)

def make_prediction(age, sex, bmi, children, smoker, region, bmi_smoker_interaction):



     # mapping 

    sex_mapping = {'female':1, 'male': 0}

    smoker_mapping = {'smoker':1, 'no smoker': 0}
    inputs['smoker'] = inputs['sex'].map(smoker_mapping)

    bmi_smoker_interaction = bmi * smoker

    inputs = pd.DataFrame({
        'age': [age],
        'sex': [sex,],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region],
        'bmi_smoker_interaction':[bmi_smoker_interaction]

    })


    prediction = modele.predict(inputs)

    return prediction

# Exemple d'utilisation dans Streamlit
age = st.slider("Age", min_value=18, max_value=100, value=30)
sex = st.radio("Sex", options=['female', 'male'])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.slider("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.radio("Smoker", options=['smoker', 'no smoker'])
region = st.selectbox("Region", options=['southwest', 'southeast', 'northwest', 'northeast'])
bmi_smoker_interaction = bmi * (1 if smoker == 'smoker' else 0)

# Bouton pour effectuer la prédiction
if st.button("Effectuer la prédiction"):
    prediction_result = make_prediction(age, sex, bmi, children, smoker, region, bmi_smoker_interaction)
    st.write("Résultat de la prédiction:", prediction_result)