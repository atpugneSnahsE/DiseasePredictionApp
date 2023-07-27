# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 01:14:10 2023

@author: USER
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#load models
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
heart_model = pickle.load(open("heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open("parkinsons_model.sav", 'rb'))


#sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction', 
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                           icons = ['person-heart', 'person-gear', 'person-slash'],
                           default_index = 0)
    
#diabetes prediction page
if(selected == 'Diabetes Prediction'):
    
    #title
    st.title('Diabetes Prediction System')
    
    #input
    #columns
    col1, col2, col3 = st.columns(3)
    
    #Datafields
    with col1:
        Pregnancies = st.text_input('Number of pregnencies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Current Blood Pressure')
    with col1:
        SkinThickness = st.text_input('Thickness of Skin')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('Body Mass Index')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Current age')
    
    #Prediction
    diabetes_diag = ''
    
    #button
    if st.button('Test Result'):
        diabetes_pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if diabetes_pred[0] == 1:
            diabetes_diag = 'The person is diabetic'
        else:
            diabetes_diag = 'The person is not diabetic'
    st.success(diabetes_diag)


#heart disease prediction page
if(selected == 'Heart Disease Prediction'):
    #title
    st.title('Heart Disease Prediction System')
    #input
    #columns
    col1, col2, col3 = st.columns(3)
    
    #Datafields
    with col1:
        age = st.text_input('Age of patient')
    with col2:
        sex = st.text_input('Gender of patient')
    with col3:
        cp = st.text_input('Chest pain type (4 values)')
    with col1:
        trestbps = st.text_input('Resting blood pressure')
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting blood sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting electrocardiographic results (values 0,1,2)')
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    with col3:
        exang = st.text_input('Exercise induced angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('The slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    with col1:
        thal = st.text_input('Thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    #Prediction
    heart_diag = ''
    
    #button
    if st.button('Test Result'):
        heart_pred = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_pred[0] == 1:
            heart_diag = 'The person has heart disease'
        else:
            heart_diag = 'The person does not have heart disease'
    st.success(heart_diag)


#parkinsons prediction page
if(selected == 'Parkinsons Prediction'):
    #title
    st.title('Parkinsons Disease Prediction System')
    #input
    #columns
    col1, col2, col3 = st.columns(3)
    
    #Datafields
    with col1:
        MDVP_Fo = st.text_input('Average vocal fundamental frequency')
    with col2:
        MDVP_Fhi = st.text_input('Maximum vocal fundamental frequency')
    with col3:
        MDVP_Flo = st.text_input('Minimum vocal fundamental frequency')
    with col1:
        MDVP_Jitter = st.text_input('Jitter(%) variation in fundamental frequency')
    with col2:
        MDVP_Jitter_Abs = st.text_input('Jitter(Abs) variation in fundamental frequency')
    with col3:
        MDVP_RAP = st.text_input('RAP variation in fundamental frequency')
    with col1:
        MDVP_PPQ = st.text_input('PPQ variation in fundamental frequency')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP variation in fundamental frequency')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer variation in amplitude')
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB) variation in amplitude')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3 variation in amplitude')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5 variation in amplitude')
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ variation in amplitude')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA variation in amplitude')
    with col3:
        NHR = st.text_input('NHR measures of ratio of noise to tonal components in the voice')
    with col1:
        HNR = st.text_input('HNR measures of ratio of noise to tonal components in the voice')
    with col2:
        RPDE = st.text_input('RDPE nonlinear dynamical complexity measures')
    with col3:
        DFA = st.text_input('DFA Signal fractal scaling exponent')
    with col1:
        spread1 = st.text_input('Spread1 nonlinear measures of fundamental frequency variation')
    with col2:
        spread2 = st.text_input('Spread2 nonlinear measures of fundamental frequency variation')
    with col3:
        D2 = st.text_input('D2 nonlinear dynamical complexity measures')
    with col1:
        PPE = st.text_input('PPE nonlinear measures of fundamental frequency variation')
    
    #Prediction
    parkinsons_diag = ''
    
    #button
    if st.button('Test Result'):
        parkinsons_pred = parkinsons_model.predict([[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if parkinsons_pred[0] == 1:
            parkinsons_diag = 'The person has parkinsons disease'
        else:
            parkinsons_diag = 'The person does not have parkinsons disease'
    st.success(parkinsons_diag)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        