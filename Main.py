import  streamlit as st
from PIL import Image
import pandas as pd


# 1. Criação do menu (pode ser na barra lateral ou no topo)
home, servicos, contato , descricao = st.tabs(home="Home", servicos="Serviços", contato="Contato", descricao="Descrição")