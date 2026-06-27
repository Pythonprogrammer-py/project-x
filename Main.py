import  streamlit as st
from PIL import Image
import pandas as pd


# 1. Criação do menu (pode ser na barra lateral ou no topo)
home, servicos, informacoes, contato = st.tabs(["Home", "Serviços", "Informações", "Contato"])


def login():
    with st.form("login_form"):
        st.text_input("Usuário")
        st.text_input("Senha", type="password")
        st.form_submit_button("Entrar")


with home:
    st.title("Bem-vindo ao nosso site!")
    st.write("Aqui você encontra atualizações e descrição previas de serviços.")
    st.write("Estamos trabalhando para trazer mais funcionalidades em breve.")

with servicos:
    login()