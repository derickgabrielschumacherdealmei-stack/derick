import sys
import subprocess

# Instalação automática blindada do edge-tts para o Streamlit Cloud
try:
    import edge_tts
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "edge-tts"])
    import edge_tts

import streamlit as st
import asyncio
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
    ["Ana (Feminina - Neural)", "Marcos (Masculino - Neural)"],
    key="radio_locutor"
)

# Função assíncrona protegida para gerar o áudio
async def gerar_audio_seguro(texto, voz, ficheiro_saida):
    try:
        comunicador = edge_tts.Communicate(texto, voz)
        await comunicador.save(ficheiro_saida)
        return True
    except Exception as e:
        return False

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

    # Definir a voz com base na escolha do locutor
    if "Marcos" in locutor:
        voz_escolhida = "pt-BR-AntonioNeural"  # Voz masculina natural
        resposta_ia = f"E aí, Derick! Aqui fala o Marcos. Recebi a tua mensagem: '{prompt}'."
    else:
        voz_escolhida = "pt-BR-FranciscaNeural"  # Voz feminina natural
        resposta_ia = f"Olá Derick! Aqui fala a Ana. Recebi a tua mensagem: '{prompt}'."

    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar o áudio com proteção contra erros
        ficheiro_audio = "resposta_audio.mp3"
        if os.path.exists(ficheiro_audio):
            try:
                os.remove(ficheiro_audio)
            except:
                pass
            
        # Executar a geração de áudio
        sucesso = False
        try:
            sucesso = asyncio.run(gerar_audio_seguro(resposta_ia, voz_escolhida, ficheiro_audio))
        except RuntimeError:
            # Caso o loop assíncrono já esteja aberto em algum contexto do Streamlit
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            sucesso = loop.run_until_complete(gerar_audio_seguro(resposta_ia, voz_escolhida, ficheiro_audio))
        
        if sucesso and os.path.exists(ficheiro_audio):
            st.audio(ficheiro_audio, format="audio/mp3")
        else:
            st.info("💡 A mensagem foi processada com sucesso por texto!")
