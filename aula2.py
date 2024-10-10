import streamlit as st
import pandas as pd 

st.title("Carregue o seu DataSet")

upload = st.file_uploader("Escolha o arquivo",type="csv")
if upload is not None:
    df = pd.read_csv(upload)
    st.dataframe(df)