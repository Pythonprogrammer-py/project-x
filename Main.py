import  streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Tudo para sua empresa", page_icon=":bar_chart:", layout="wide")
st.title("tudo para sua empresa")
if st.button("Clique aqui para começar"):
    st.write("Novos recursos estarão disponíveis em breve! Fique atento às atualizações e aproveite ao máximo nossa plataforma para impulsionar sua empresa.")



st.write("Bem-vindo à nossa plataforma! Aqui você encontrará tudo o que precisa para impulsionar sua empresa. Explore nossos recursos e descubra como podemos ajudá-lo a alcançar seus objetivos de negócios.")

pag1, pag2 = st.tabs(["Serviços", "Contato"])

with pag1:
    st.header("Serviços de Qualidade você só encontra aqui!")
    st.write("Oferecemos uma ampla gama de serviços para atender às necessidades da sua empresa. Desde consultoria estratégica até soluções tecnológicas, estamos aqui para ajudá-lo a alcançar o sucesso.")
    st.write("Orçamento de arquivos, compativel com whatsapp. Para melhor eficiencia.")

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
    
with pag2:
    st.header("Entre em contato conosco!")
    st.write("Se você tiver alguma dúvida ou precisar de mais informações, não hesite em entrar em contato conosco. Nossa equipe está pronta para ajudá-lo.")
    st.write("Email: taysonvitorvitor@gmail.com")