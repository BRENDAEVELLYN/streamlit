
#importando a biblioteca StreamLit
import streamlit as st

"""
Estamos iniciando o streamlite
Ele nos ajudará no projeto final
Em sua instalação vem incluido o pandas e outras libs

"""
idade = st.number_input("Digite sua idade:", min_value=14, max_value=120)
if idade >=18:
    #uso obrigatório de identação
    st.write(f"Alô Mundo - você é maior de idade: {idade}")
else:
   st.write(f"Alô Mundo - você é menor de idade:{idade}") 
