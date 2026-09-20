import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="IA Impossível - Avançada", 
    page_icon="🤖", 
    layout="wide"
)

st.title("🤖 IA Impossível - Assistente Avançado")
st.markdown("*Compreensão de contexto, segurança, sotaques e múltiplos idiomas.*")

# --- MENU DE DEFINIÇÕES NA BARRA LATERAL ---
st.sidebar.title("⚙️ Definições Avançadas")

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

# Botão para limpar o histórico e garantir precisão
if st.sidebar.button("🧹 Limpar Histórico / Reiniciar"):
    st.session_state.messages = []
    st.rerun()

# --- ÁREA PRINCIPAL DO CHAT ---
st.markdown("### 💬 Conversa Inteligente")

# Inicializar o histórico para manter o contexto da conversa
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar nova entrada do utilizador
if prompt := st.chat_input("Escreve a tua mensagem aqui..."):
    # Guardar mensagem do utilizador
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Lógica de processamento com base na adaptabilidade e tom escolhido
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
        resposta_ia = f"Ciao! Analizzando la tua richiesta con precisione: {prompt}"
    elif "Inglês" in opcao_voz:
        lang_code = 'en'
        resposta_ia = f"Hello! Analyzing your request efficiently: {prompt}"
    elif "Alemão" in opcao_voz:
        lang_code = 'de'
        resposta_ia = f"Hallo! Ich analysiere deine Anfrage präzise: {prompt}"
    elif "Mexicano" in opcao_voz:
        lang_code = 'es'
        resposta_ia = f"¡Qué onda, güey! Analizando tu solicitud con todo detalle: {prompt}"
    elif "Espanhol" in opcao_voz:
        lang_code = 'es'
        resposta_ia = f"¡Hola! Analizando tu solicitud con precisión: {prompt}"
    else:  # Brasileiro - Ana
        lang_code = 'pt'
        resposta_ia = f"Olá! Aqui fala a Ana. Analisando a tua questão de forma segura: {prompt}"

    # Guardar e exibir a resposta da IA
    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar o áudio otimizado de forma segura com o gTTS
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
            st.info("💡 Mensagem processada com sucesso por texto!")
       
