import streamlit as st
import numpy as np 
import pandas as pd 
import pickle 
from catboost import CatBoostRegressor
import sklearn

with open ("modelo1.pkl","rb") as doc:
    model=pickle.load(doc)

st.title("Modelo - Clase 26 de septiembre 2023")
st.divider()
st.write("Ingrese los datos")

assess=st.slider("Assess",0,10000)
bedrooms=st.slider("Bedrooms",0,100)
lotsize=st.slider("Lote Size",0,500000)
square_fit=st.slider("Square Fit",0,100000)
colonial=st.selectbox("Colonial",[0,1])


prediccion=model.predict(np.array([[assess,bedrooms,lotsize,square_fit,colonial]]))
if st.button("Predecir"):
    st.write(f"El precio de la casa es de {prediccion[0]}")

