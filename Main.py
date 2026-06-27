import  streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Tudo para sua empresa", page_icon=":bar_chart:", layout="wide")
st.title("tudo para sua empresa")
if st.button("Clique aqui para começar"):
    st.write("Novos recursos estarão disponíveis em breve! Fique atento às atualizações e aproveite ao máximo nossa plataforma para impulsionar sua empresa.")



st.write("Bem-vindo à nossa plataforma! Aqui você encontrará tudo o que precisa para impulsionar sua empresa. Explore nossos recursos e descubra como podemos ajudá-lo a alcançar seus objetivos de negócios.")

st.set_page_config(page_title="Meu App Principal", page_icon="🏠")

st.title("Bem-vindo ao App Principal")
st.write("Use o menu lateral para navegar pelos arquivos já existentes!")