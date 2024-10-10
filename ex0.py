#importe o streamlit
import streamlit as st

#entre com um número
number=st.number_input("Digite o número:",step=1)
#verifique se o número é positivo, negativo ou nulo

if number >0:
     st.write(f"Positivo: {number}")

elif number == 0:
     st.write(f'Nulo: {number}')

else:
     st.write(f'Negativo: {number}')
