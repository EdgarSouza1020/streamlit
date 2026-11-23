import streamlit as st
from datetime import datetime, time

st.write("Hello World!")


st.title("Formulario de produtos")
email = st.text_input("Insira seu email")
data = st.date_input("Dada do cadastro", datetime.now())
hora = st.time_input("Hora do cadastro", value=time(9, 0)) # valor padrão: 09:00
valor = st.number_input("Custo", min_value=0.0, format="%.2f")
quantidade = st.number_input("Quantidade", min_value=1, step=1)
departamento = st.selectbox("Produto", options=["Limpeza", "Perfumaria", "Bebidas"])

if st.button("Salvar"):
    st.write("**Dados do cadastro**")
    st.write("email do colaborador")
    st.write("Data do cadastro")
    st.write("Hora do cadastro")
    st.write(f"Quantidade de produtos {quantidade}")
    st.write(f"Produto: {departamento}")
