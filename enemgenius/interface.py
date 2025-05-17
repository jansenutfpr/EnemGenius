import streamlit as st
from core import executar_enem_assistant

# Interface Streamlit
st.set_page_config(page_title="EnemGenius", page_icon="📖")
st.title("📖 EnemGenius")
st.markdown("## Preparação Inteligente e Divertida para o Enem. 🚀")
disciplina = st.text_input("📘 Disciplina :")
tema = st.text_input("🧩 Tema, dúvida ou pergunta : ")

if st.button("Perguntar"):
    disciplina = disciplina if disciplina else None
    tema = tema if tema else None
    resposta = executar_enem_assistant(disciplina=disciplina, tema=tema)
    st.markdown("### 📚 Resposta do EnemGenius")
    st.markdown(resposta)