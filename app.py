# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 


pickle_in = open("SVM_model_main.pkl","rb")
classifier=pickle.load(pickle_in)

def heart_attack_prediction(sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall):
    
    
    prediction = classifier.predict([[sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]])
    print(prediction)
    return prediction




def main():
    st.title("Heart Attack Predictor")
    html_temp = """
                 <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Attack Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sex = st.text_input("Sex-Either 0 or 1","Type Here")
    exng = st.text_input("Exercise Induced Angina(If yes 1 else 0)","Type Here")
    caa = st.text_input("No. of major vessels(0-3)","Type Here")
    cp = st.text_input("Chest Pain Type-1,2,3 or 4","Type Here")
    trtbps = st.text_input("Resting Blood pressure(mm Hg)","Type Here")
    chol = st.text_input("Cholestoral in mg/dl","Type Here")
    fbs = st.text_input("Fasting Blood Sugar(If > 120 then 1 else 0)","Type Here")
    restecg = st.text_input("Resting ECG results(0,1 or 2)","Type Here")
    thalachh = st.text_input("Maximum heart rate achieved","Type Here")
    oldpeak = st.text_input("ST depression induced by exercise relative to rest","Type Here")
    slp = st.text_input("Slope of the peak exercise ST segment (0=upsloping; 1=flat; 2=downsloping)","Type Here")
    thall = st.text_input("Thalassemia","Type Here")
    result = ""
    if st.button("Predict"):
        result = heart_attack_prediction(sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall)
        st.success('The output is {}'.format(result))
        #if result == 0:
            #st.success('The person does not get a Heart Attack! Yay!')
        #else:
            #st.write("Oops!This person will get a Heart Attack! Die soon haha!")
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")   
        
        
        
if __name__=='__main__':
    main()