import streamlit as st 
import numpy as np
import pandas as pd
import joblib

st.title('Prédiction de Survie au naufrage du TITANIC')
st.subheader('Auteur: Ange DAHOU')
st.markdown("###### Pensez vous que vous auriez survecu au naufrage du Titanic?")
st.markdown('*Cette application utilise un model de Marchine Learning pour prédire votre survie si vous etiez au bord du TITANIC*')

# Afficher une image du Titanic
st.image('titanic_image.png', caption='Le Titanic en mer', width=600)

#Chargement du model
model = joblib.load(filename='titanic.joblib')

#Definition d'une fonction d'inference
def inference(pclass, age, sex, famille):
    new_data = pd.DataFrame({'pclass': [pclass], 'sex':[sex] , 'age': [age], 'family': [family]})
    pred = model.predict(new_data)
    return pred 
# Information de l'utilisteur 
col1, col2 = st.columns(2)

with col1:
    pclass = st.number_input(label='En quelle classe voyageriez-vous?:', min_value=1, max_value=3, value=1)

with col2:
    age = st.number_input(label='Quel âge avez-vous ?', min_value=9, value=10)

col3, col4 = st.columns(2)

with col3:
    sex = st.selectbox('Quel est votre sexe ?', ['Homme', 'Femme'])
    sex = 1 if sex == 'Homme' else 0  # Conversion en 1 ou 0

with col4:
    family = st.number_input(label='De combien de personnes seriez-vous accompagné?', min_value=0, max_value=10, value=0)

#Création du boutton Prediction

if st.button('Prédiction'):
    prediction = inference(pclass, age, sex, family)
    if prediction == '1':
        st.markdown('<p style="color:green;"> Vous auriez survécu au naufrage !🎉</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color:red;">Désolé, vous n’auriez pas survécu😞</p>', unsafe_allow_html=True)