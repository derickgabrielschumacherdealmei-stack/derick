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

# Botão para limpar o histórico
if st.sidebar.button("🧹 Limpar Histórico / Reiniciar"):
    st.session_state.messages = []
    st.rerun()

# --- ÁREA PRINCIPAL DO CHAT ---
st.markdown("### 💬 Conversa Inteligente")

# Inicializar o histórico para manter o contexto
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

    prompt_lower = prompt.lower().strip()
    
    # Gerar respostas diretas e naturais baseadas no sotaque/idioma
    if "Gaúcho" in opcao_voz:
        lang_code = 'pt'
        if any(w in prompt_lower for w in ["oi", "olá", "tudo bem", "como vai"]):
            resposta_ia = "Bah, guri! Tudo certo por aqui e contigo? Como é que eu posso te ajudar hoje?"
        else:
            resposta_ia = f"Entendido, vivente! Sobre '{prompt}', a minha visão é que nós podemos resolver isso logo."
            
    elif "Mineiro" in opcao_voz:
        lang_code = 'pt'
        if any(w in prompt_lower for w in ["oi", "olá", "tudo bem", "como vai"]):
            resposta_ia = "Uai, sô! Trem bão? Por aqui tá tudo joia. O que cê manda?"
        else:
            resposta_ia = f"Com certeza, sô! Sobre '{prompt}', o trem funciona direitinho se a gente planejar."
            
    elif "Carioca" in opcao_voz:
        lang_code = 'pt'
        if any(w in prompt_lower for w in ["oi", "olá", "tudo bem", "como vai"]):
            resposta_ia = "Fala, irmão! Tranquilidade total. Qual é a boa de hoje?"
        else:
            resposta_ia = f"Papo retíssimo, menor! Sobre '{prompt}', pode deixar que eu resolvo isso contigo."
            
    elif "Italiano" in opcao_voz:
        lang_code = 'it'
        if any(w in prompt_lower for w in ["ciao", "salve", "buongiorno"]):
            resposta_ia = "Ciao! Come posso aiutarti oggi?"
        else:
            resposta_ia = f"Ho capito riguardo a '{prompt}'. Ecco la mia risposta per te."
        
    elif "Inglês" in opcao_voz:
        lang_code = 'en'
        if any(w in prompt_lower for w in ["hi", "hello", "how are you"]):
            resposta_ia = "Hello! How can I help you today?"
        else:
            resposta_ia = f"Regarding '{prompt}', here is what I think we should do."
        
    elif "Alemão" in opcao_voz:
        lang_code = 'de'
        if any(w in prompt_lower for w in ["hallo", "guten tag"]):
            resposta_ia = "Hallo! Wie kann ich dir heute helfen?"
        else:
            resposta_ia = f"Zu '{prompt}': Das ist ein sehr interessanter Punkt."
        
    elif "Mexicano" in opcao_voz:
        lang_code = 'es'
        if any(w in prompt_lower for w in ["hola", "qué tal"]):
            resposta_ia = "¡Qué onda, güey! ¿Cómo andas? ¿En qué te puedo ayudar?"
        else:
            resposta_ia = f"Sobre '{prompt}', ¡a darle con todo para resolverlo!"
        
    elif "Espanhol" in opcao_voz:
        lang_code = 'es'
        if any(w in prompt_lower for w in ["hola", "qué tal"]):
            resposta_ia = "¡Hola! ¿Cómo estás? ¿En qué te puedo ayudar hoy?"
        else:
            resposta_ia = f"Respecto a '{prompt}', esto es lo que te puedo decir."
        
    else:  # Brasileiro - Ana
        lang_code = 'pt'
        if any(w in prompt_lower for w in ["oi", "olá", "tudo bem", "como vai"]):
            resposta_ia = "Olá! É um prazer falar contigo. Como posso ajudar?"
        else:
            resposta_ia = f"Entendi a tua questão sobre '{prompt}'. Vamos lá resolver isto juntos."

    # Guardar e exibir a resposta da IA
    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar o áudio com gTTS sem mensagens de erro no ecrã
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
        except:
            pass
