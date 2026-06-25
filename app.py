import streamlit as st
import pandas as pd


st. title("Resultado de somas repetidas.")

numero = st.number_input("Quantos aquivos deseja processar", min_value=1, step=1)

for i in range(numero):
    i = i+1
    st.write(f"Arquivo {i}")
    arquivo = st.file_uploader(f"Escolha o arquivo ", type=["csv", "xlsx","docx", "pdf", "txt"], key=f"arquivo_{i}")
    if arquivo is not None:
        df = pd.read_csv(arquivo)
        st.write(df)
        resultado = df.sum().sum()
        st.write(f"O resultado da soma do arquivo {i} é: {resultado}")