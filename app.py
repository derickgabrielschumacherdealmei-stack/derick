import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Impossível", 
    page_icon="🤖", 
    layout="wide"
)

# --- ESTILO VISUAL COM CORREÇÃO TOTAL DA FAIXA BRANCA DO CHAT ---
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #0b0b0b;
        color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #121212 !important;
        border-right: 1px solid #1f1f1f;
    }
    
    /* --- ELIMINAR COMPLETAMENTE O BRANCO DO CHAT INPUT --- */
    
    /* Força o bloco de fundo inteiro do chat input a ficar preto */
    [data-testid="stChatInputContainer"], 
    div.stChatFloatingInputContainer,
    .stChatFloatingInputContainer,
    div[class*="stChatInputContainer"] {
        background-color: #0b0b0b !important;
    }

    /* Remove fundos brancos de blocos envolventes do input */
    div.block-container div[data-testid="stVerticalBlock"] div:has(> div[data-testid="stChatInputContainer"]) {
        background-color: #0b0b0b !important;
    }

    /* Caixa de texto onde o utilizador escreve */
    .stChatInputContainer input {
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #ff3333 !important;
        border-radius: 14px !important;
        padding: 12px 20px !important;
    }
    
    .stChatInputContainer input::placeholder {
        color: #888888 !important;
    }

    /* Mensagens do Chat com fundo escuro e texto branco */
    .stChatMessage {
        background-color: #141414 !important;
        border: 1px solid #1f1f1f !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }
    
    .stChatMessage p, .stChatMessage div, .stChatMessage span {
        color: #ffffff !important;
    }

    /* Hero Banner Principal */
    .hero-box {
        background: radial-gradient(circle at 80% 20%, rgba(255, 51, 51, 0.15) 0%, rgba(11, 11, 11, 0) 60%);
        border: 1px solid #1f1f1f;
        border-radius: 16px;
        padding: 40px;
        margin-bottom: 30px;
    }
    
    .hero-title {
        color: #ffffff;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .hero-title span {
        color: #ff3333;
    }
    
    .hero-desc {
        color: #888888;
        font-size: 15px;
        max-width: 600px;
        line-height: 1.5;
    }
    
    /* Grelha de Ações Rápidas */
    .section-title {
        color: #ffffff;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        margin-bottom: 30px;
    }
    
    .action-card {
        background-color: #141414;
        border: 1px solid #1f1f1f;
        border-radius: 12px;
        padding: 18px;
        transition: all 0.3s ease;
    }
    
    .action-card:hover {
        border-color: #ff3333;
        background-color: #181414;
    }
    
    .card-title {
        color: #ffffff;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 6px;
    }
    
    .card-desc {
        color: #777777;
        font-size: 12px;
        line-height: 1.4;
    }
    
    /* Botões gerais personalizados em vermelho e preto */
    .stButton button {
        background-color: #ff3333 !important;
        color: #000000 !important;
        border: 1px solid #ff4d4d !important;
        border-radius: 8px !important;
        width: 100% !important;
        font-weight: bold !important;
    }
    
    .stButton button:hover {
        background-color: #cc0000 !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# --- GESTÃO DE ESTADO DO SOTAQUE/IDIOMA ---
if "opcao_voz" not in st.session_state:
    st.session_state.opcao_voz = "Brasileiro - Ana"

# --- BARRA LATERAL (ESTILO PAINEL DEDICADO) ---
st.sidebar.markdown("<h3 style='color: #ff3333; margin-bottom: 20px;'>⚡ Impossível</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #666; font-size: 12px; margin-top: -15px;'>Sua IA pessoal, para a vida.</p>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #fff; font-weight: 600;'>🌍 Selecione o Estilo / Sotaque:</p>", unsafe_allow_html=True)

opcoes = [
    "Brasileiro - Ana",
    "Brasileiro - Gaúcho",
    "Brasileiro - Mineiro",
    "Brasileiro - Carioca",
    "Italiano",
    "Inglês",
    "Alemão",
    "Espanhol",
    "Mexicano"
]

for op in opcoes:
    if st.sidebar.button(f"{'▶ ' if st.session_state.opcao_voz == op else ''}{op}", key=f"btn_{op}"):
        st.session_state.opcao_voz = op
        st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Limpar Histórico", key="btn_limpar"):
    st.session_state.messages = []
    st.rerun()

# --- INTERFACE PRINCIPAL ---
st.markdown("""
<div class="hero-box">
    <div style="font-size: 12px; color: #ff3333; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px;">Bem-vindo(a)</div>
    <div class="hero-title">Olá, eu sou a <span>Impossível</span></div>
    <div class="hero-desc">Sua IA pessoal, pronta para te ajudar a pensar mais longe, criar mais rápido e transformar suas ideias em realidade.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    <span style="color: #ff3333;">■</span> O que você quer fazer hoje?
</div>
<div class="cards-grid">
    <div class="action-card">
        <div class="card-title">💬 Conversar</div>
        <div class="card-desc">Tire suas dúvidas, peça conselhos e mantenha conversas fluídas.</div>
    </div>
    <div class="action-card">
        <div class="card-title">🎨 Criar Imagem</div>
        <div class="card-desc">Transforme textos em ilustrações e imagens impressionantes.</div>
    </div>
    <div class="action-card">
        <div class="card-title">📄 Analisar Documentos</div>
        <div class="card-desc">Faça upload de ficheiros para resumir, analisar e extrair insights.</div>
    </div>
    <div class="action-card">
        <div class="card-title">💻 Programar</div>
        <div class="card-desc">Escreva, depure e otimize códigos em várias linguagens.</div>
    </div>
    <div class="action-card">
        <div class="card-title">🌐 Pesquisar na Web</div>
        <div class="card-desc">Encontre informações atualizadas na internet em tempo real.</div>
    </div>
    <div class="action-card">
        <div class="card-title">💡 Brainstorming</div>
        <div class="card-desc">Gere ideias criativas e soluções inovadoras para seus projetos.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"### 💬 Chat Ativo <span style='font-size: 14px; color: #ff3333;'>({st.session_state.opcao_voz})</span>", unsafe_allow_html=True)

# Inicializar histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite a sua mensagem para a Impossível..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower().strip()
    opcao_voz = st.session_state.opcao_voz
    
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
            resposta_ia = "¡Qué onda, güey! ¿Cómo andas? ¿En qué te puedo ajudar?"
        else:
            resposta_ia = f"Sobre '{prompt}', ¡a darle con todo para resolverlo!"
        
    elif "Espanhol" in opcao_voz:
        lang_code = 'es'
        if any(w in prompt_lower for w in ["hola", "qué tal"]):
            resposta_ia = "¡Hola! ¿Cómo estás? ¿En qué te puedo ajudar hoy?"
        else:
            resposta_ia = f"Respecto a '{prompt}', esto es lo que te puedo decir."
        
    else:  # Brasileiro - Ana
        lang_code = 'pt'
        if any(w in prompt_lower for w in ["oi", "olá", "tudo bem", "como vai"]):
            resposta_ia = "Olá! É um prazer falar contigo. Como posso ajudar?"
        else:
            resposta_ia = f"Entendi a tua questão sobre '{prompt}'. Vamos lá resolver isto juntos."

    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
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
