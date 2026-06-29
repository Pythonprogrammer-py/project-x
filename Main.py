import  streamlit as st
import pandas as pd


# 1. Criação do menu (pode ser na barra lateral ou no topo)
home, servicos, informacoes, contato = st.tabs(["Home", "Serviços", "Informações", "Contato"])


def login():
    with st.form("login_form"):
        name = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")

        if st.form_submit_button("Entrar"):
           st.success("Login realizado com sucesso!")
        
        else:

            st.warning("Usuário ou senha incorretos. Tente novamente.")
    

        
with home:
    st.title("Bem-vindo ao nosso site!")
    st.write("Aqui você encontra atualizações e descrição previas de serviços.")
    st.write("Estamos trabalhando para trazer mais funcionalidades em breve.")

with servicos:

    

    def registro():
        with st.form("registro_form"):
         name = st.text_input("Nome da empresa")
         email = st.text_input("Email")
         tipo_empresa = st.radio("Tipo de empresa", ["MEI", "EIRELI", "LTDA", "S/A"],)
         cnpj = st.number_input("CNPJ", step=14)
         senha = st.text_input("Senha", type="password")
        
         if st.form_submit_button("Registrar"):
             st.success("Registro realizado com sucesso!")
             st.write(f"Bem-vindo, {name}!")
         
    st.title("Serviços")
    st. write("Aqui você pode acessar nossos serviços. Para isso, é necessário estar logado.")
    if st.button("Acessar serviços"):

        st.button("Fazer login", on_click=registro())
    st.write("Se já possui uma conta faça login para continuar")
    if st.button("Fazer login"):
        login()



            
    