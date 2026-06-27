import  streamlit as st
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu

# 1. Criação do menu (pode ser na barra lateral ou no topo)
with st.sidebar:
    opcao = option_menu(
        menu_title="Menu Principal",
        options=["Home", "Análise de Dados", "Configurações"],
        icons=["house", "bar-chart", "gear"],
        menu_icon="cast",
        default_index=0,
    )

# 2. Renderização do conteúdo com base na escolha
if opcao == "Home":
    st.title("Página Inicial")
    st.write("Bem-vindo ao sistema.")

elif opcao == "Análise de Dados":
    st.title("Análise de Dados")
    # Aqui você pode importar ou rodar o código do seu outro arquivo
    st.write("Gráficos e relatórios aqui.")

elif opcao == "Configurações":
    st.title("Configurações")
    st.write("Tela de ajustes.")