import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="IA Impossível", page_icon="🤖", layout="wide")

st.title("🤖 IA Impossível - O teu Assistente")

# --- MENU DE DEFINIÇÕES NA BARRA LATERAL ---
st.sidebar.title("⚙️ Definições da IA")

st.sidebar.markdown("---")
st.sidebar.subheader("🌍 Idioma e Sotaque")

opcao_voz = st.sidebar.selectbox(
    "Escolha o estilo / idioma:",
    [
        "Brasileiro - Ana",
        "Brasileiro - Gaúcho",
        "Brasileiro - Mineiro",
        "Brasileiro - Carioca",
        "Italiano",
        "Inglês",
        "Alemão",
        "Espanhol",
        "Mexicano"
    ],
    key="select_idioma_voz"
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

    # Definir a resposta e o código de idioma do gTTS consoante a escolha
    if "Gaúcho" in opcao_voz:
        lang_code = 'pt'
        resposta_ia = f"Bah, guri! Tchê, sobre isso que tu perguntaste: {prompt}"
    elif "Mineiro" in opcao_voz:
        lang_code = 'pt'
        resposta_ia = f"Uai, sô! Trem bão? Negócio é o seguinte: {prompt}"
    elif "Carioca" in opcao_voz:
        lang_code = 'pt'
        resposta_ia = f"Fala, irmão! Tranquilidade? Papo reto sobre isso aí: {prompt}"
    elif "Italiano" in opcao_voz:
        lang_code = 'it'
        resposta_ia = f"Ciao! Analizzando la tua richiesta: {prompt}"
    elif "Inglês" in opcao_voz:
        lang_code = 'en'
        resposta_ia = f"Hello! Analyzing your request: {prompt}"
    elif "Alemão" in opcao_voz:
        lang_code = 'de'
        resposta_ia = f"Hallo! Ich analysiere deine Anfrage: {prompt}"
    elif "Mexicano" in opcao_voz:
        lang_code = 'es'
        resposta_ia = f"¡Qué onda, güey! Analizando tu solicitud: {prompt}"
    elif "Espanhol" in opcao_voz:
        lang_code = 'es'
        resposta_ia = f"¡Hola! Analizando tu solicitud: {prompt}"
    else:  # Brasileiro - Ana
        lang_code = 'pt'
        resposta_ia = f"Olá! Aqui fala a Ana. Analisando a tua questão: {prompt}"

    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar o áudio de forma segura com o gTTS no idioma/sotaque correto
        ficheiro_audio = "resposta_audio.mp3"
        if os.path.exists(ficheiro_audio):
            try:
                os.remove(ficheiro_audio)
            except:
                pass
            
        try:
            tts = gTTS(text=resposta_ia, lang=lang_code, slow=False)
            tts.save(ficheiro_audio)
            if os.path.exists(ficheiro_audio):
                st.audio(ficheiro_audio, format="audio/mp3")
        except Exception as e:
            st.info("💡 Mensagem processada por texto com sucesso!")
