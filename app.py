import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="IA Impossível", page_icon="🤖", layout="wide")

st.title("🤖 IA Impossível - O teu Assistente")

# --- MENU DE DEFINIÇÕES NA BARRA LATERAL ---
st.sidebar.title("⚙️ Definições da IA")
nome_ia = st.sidebar.text_input("Nome da IA", value="Impossível")

st.sidebar.markdown("---")
st.sidebar.subheader("🎙️ Seleção de Locutor")

locutor = st.sidebar.radio(
    "Escolha quem vai falar:",
    ["Ana (Feminina)", "Marcos (Masculino)"],
    key="radio_locutor"
)

# --- ÁREA PRINCIPAL DO CHAT ---
st.markdown("### 💬 Conversa com a IA")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escreve a tua mensagem aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Definir a resposta com base na escolha do locutor
    if "Marcos" in locutor:
        resposta_ia = f"E aí, Derick! Aqui fala o Marcos. Recebi a tua mensagem: '{prompt}'."
        tlang = 'pt'
    else:
        resposta_ia = f"Olá Derick! Aqui fala a Ana. Recebi a tua mensagem: '{prompt}'."
        tlang = 'pt'

    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar o áudio de forma segura com gTTS
        ficheiro_audio = "resposta_audio.mp3"
        if os.path.exists(ficheiro_audio):
            try:
                os.remove(ficheiro_audio)
            except:
                pass
            
        try:
            tts = gTTS(text=resposta_ia, lang=tlang, slow=False)
            tts.save(ficheiro_audio)
            if os.path.exists(ficheiro_audio):
                st.audio(ficheiro_audio, format="audio/mp3")
        except Exception as e:
            st.info("💡 Mensagem processada por texto com sucesso!")
