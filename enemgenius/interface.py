import streamlit as st
from script3 import enem_genius_cli
from enem_genius_script import enem_assistant_cli

# Interface Streamlit
st.set_page_config(page_title="EnemGenius", page_icon="📖")
st.title("📖 EnemGenius")
st.markdown("## Preparação Inteligente para o ENEM")

disciplina = st.text_input("📘 Disciplina :")
tema = st.text_input("🧩 Tema : ")

if st.button("Perguntar"):
    resposta = enem_assistant_cli(disciplina=disciplina, tema=tema)
    st.markdown("### 📚 Resposta do EnemGenius")
    st.markdown(resposta)
