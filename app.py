import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="IA Impossível", page_icon="🤖", layout="wide")

st.title("🤖 IA Impossível - O teu Assistente")

# --- MENU DE DEFINIÇÕES NA BARRA LATERAL ---
st.sidebar.title("⚙️ Definições da IA")

st.sidebar.markdown("---")
st.sidebar.subheader("🎙️ Seleção de Sotaque / Voz")

locutor = st.sidebar.radio(
    "Escolha o estilo de voz:",
    ["Ana", "Gaúcho", "Mineiro", "Carioca"],
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

    # Respostas naturais ajustadas a cada estilo/sotaque
    if locutor == "Gaúcho":
        resposta_ia = f"Bah, guri! Tchê, sobre isso que tu perguntaste: {prompt}"
    elif locutor == "Mineiro":
        resposta_ia = f"Uai, sô! Trem bão? Negócio é o seguinte: {prompt}"
    elif locutor == "Carioca":
        resposta_ia = f"Fala, irmão! Tranquilidade? Papo reto sobre isso aí: {prompt}"
    else:
        resposta_ia = f"Olá! Aqui fala a Ana. Analisando a tua questão: {prompt}"

    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar o áudio de forma segura com gTTS em português (pt)
        ficheiro_audio = "resposta_audio.mp3"
        if os.path.exists(ficheiro_audio):
            try:
                os.remove(ficheiro_audio)
            except:
                pass
            
        try:
            tts = gTTS(text=resposta_ia, lang='pt', slow=False)
            tts.save(ficheiro_audio)
            if os.path.exists(ficheiro_audio):
                st.audio(ficheiro_audio, format="audio/mp3")
        except Exception as e:
            st.info("💡 Mensagem processada por texto com sucesso!")
