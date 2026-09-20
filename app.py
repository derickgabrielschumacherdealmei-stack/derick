import streamlit as st
from gtts import gTTS
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Impossível - IA Sem Limites", 
    page_icon="🔥", 
    layout="wide"
)

# --- ESTILO VISUAL IDÊNTICO AO DESIGN (TEMA ESCURO + VERMELHO NEON) ---
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background-color: #0b0b0b !important;
        color: #ffffff !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Barra Lateral Estilizada */
    [data-testid="stSidebar"] {
        background-color: #121212 !important;
        border-right: 1px solid #1a1a1a;
    }
    
    /* Caixa de Input de Chat */
    .stChatInputContainer input {
        background-color: #141414 !important;
        color: #ffffff !important;
        border: 1px solid #ff2a2a !important;
        border-radius: 16px !important;
        padding: 14px 20px !important;
    }
    
    .stChatInputContainer input::placeholder {
        color: #666666 !important;
    }

    /* Mensagens do Chat */
    .stChatMessage {
        background-color: #141414 !important;
        border: 1px solid #1f1f1f !important;
        border-radius: 14px !important;
        color: #ffffff !important;
        margin-bottom: 10px;
    }
    
    .stChatMessage p, .stChatMessage div, .stChatMessage span {
        color: #ffffff !important;
    }

    /* Hero Banner com Estilo Vermelho */
    .hero-container {
        background: radial-gradient(circle at 70% 30%, rgba(255, 42, 42, 0.12) 0%, rgba(11, 11, 11, 0) 70%);
        border: 1px solid #1c1c1c;
        border-radius: 20px;
        padding: 35px;
        margin-bottom: 25px;
    }
    
    .brand-subtitle {
        color: #ff2a2a;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 6px;
    }
    
    .hero-title {
        color: #ffffff;
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .hero-title span {
        color: #ff2a2a;
    }
    
    .hero-desc {
        color: #888888;
        font-size: 14px;
        max-width: 550px;
    }
    
    /* Grelha de Cartões de Ação Rápida */
    .section-label {
        color: #ffffff;
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 15px;
    }
    
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-bottom: 25px;
    }
    
    .action-card {
        background-color: #141414;
        border: 1px solid #1c1c1c;
        border-radius: 14px;
        padding: 16px;
        transition: all 0.2s ease-in-out;
    }
    
    .action-card:hover {
        border-color: #ff2a2a;
        background-color: #181414;
    }
    
    .card-icon {
        color: #ff2a2a;
        font-size: 16px;
        margin-bottom: 8px;
    }
    
    .card-title {
        color: #ffffff;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 4px;
    }
    
    .card-desc {
        color: #777777;
        font-size: 11px;
        line-height: 1.3;
    }
    
    /* Botões da barra lateral / gerais */
    .stButton button {
        background-color: #ff2a2a !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
    }
    
    .stButton button:hover {
        background-color: #e02424 !important;
        color: #ffffff !important;
    }
</style>

<script>
    function forcarFundoEscuro() {
        const alvos = document.querySelectorAll('[data-testid="stAppViewContainer"], section.main, .block-container, footer');
        alvos.forEach(el => {
            el.style.backgroundColor = '#0b0b0b';
            el.style.color = '#ffffff';
        });
    }
    setInterval(forcarFundoEscuro, 200);
</script>
""", unsafe_allow_html=True)

# --- ESTADO DO SOTAQUE/IDIOMA ---
if "opcao_voz" not in st.session_state:
    st.session_state.opcao_voz = "Brasileiro - Ana"

# --- BARRA LATERAL (PAINEL DE NAVEGAÇÃO) ---
st.sidebar.markdown("<h2 style='color: #ff2a2a; margin-bottom: 2px; font-size: 20px;'>🔥 IMPOSSÍVEL</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #777; font-size: 11px; margin-top: 0;'>IA SEM LIMITES</p>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #fff; font-weight: 600; font-size: 13px;'>🌍 Sotaque / Idioma:</p>", unsafe_allow_html=True)

opcoes_voz = [
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

for op in opcoes_voz:
    ativo = st.session_state.opcao_voz == op
    if st.sidebar.button(f"{'▶ ' if ativo else ''}{op}", key=f"sb_{op}"):
        st.session_state.opcao_voz = op
        st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Limpar Conversa", key="btn_limpar_chat"):
    st.session_state.messages = []
    st.rerun()

# --- INTERFACE PRINCIPAL (ESTILO DA IMAGEM) ---
st.markdown("""
<div class="hero-container">
    <div class="brand-subtitle">■ IMPOSSÍVEL IA</div>
    <div class="hero-title">Olá, <span>Derick</span>!</div>
    <div class="hero-desc">O que você quer criar hoje? Escolha uma das opções abaixo ou digite sua mensagem diretamente no chat.</div>
</div>
""", unsafe_allow_html=True)

# Grelha de Ações Rápidas Inspirada na Imagem
st.markdown('<div class="section-label">Sugestões de Ação</div>', unsafe_allow_html=True)
st.markdown("""
<div class="cards-grid">
    <div class="action-card">
        <div class="card-icon">💡</div>
        <div class="card-title">Criar algo novo</div>
        <div class="card-desc">Dê asas à sua imaginação e crie projetos originais.</div>
    </div>
    <div class="action-card">
        <div class="card-icon">🔍</div>
        <div class="card-title">Pesquisar</div>
        <div class="card-desc">Encontre dados, fatos e conteúdos detalhados.</div>
    </div>
    <div class="action-card">
        <div class="card-icon">💻</div>
        <div class="card-title">Escrever código</div>
        <div class="card-desc">Desenvolva e corrija scripts em qualquer linguagem.</div>
    </div>
    <div class="action-card">
        <div class="card-icon">🧠</div>
        <div class="card-title">Resolver problemas</div>
        <div class="card-desc">Solucione desafios complexos de forma lógica e rápida.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown(f"### 💬 Conversa Ativa <span style='font-size: 13px; color: #ff2a2a;'>({st.session_state.opcao_voz})</span>", unsafe_allow_html=True)

# Inicializar histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower().strip()
    voz = st.session_state.opcao_voz
    
    # Lógica de respostas por sotaque
    if "Gaúcho" in voz:
        lang = 'pt'
        resposta = f"Bah, guri! Sobre '{prompt}', a minha visão é que nós vamos longe!"
    elif "Mineiro" in voz:
        lang = 'pt'
        resposta = f"Uai, sô! Sobre '{prompt}', o trem vai funcionar perfeitamente."
    elif "Carioca" in voz:
        lang = 'pt'
        resposta = f"Papo retíssimo, menor! Sobre '{prompt}', pode deixar que eu resolvo contigo."
    elif "Italiano" in voz:
        lang = 'it'
        resposta = f"Ho capito riguardo a '{prompt}'. Facciamo grandi cose insieme!"
    elif "Inglês" in voz:
        lang = 'en'
        resposta = f"Regarding '{prompt}', let's make it happen right now."
    elif "Alemão" in voz:
        lang = 'de'
        resposta = f"Zu '{prompt}': Das packen wir gemeinsam an."
    elif "Mexicano" in voz:
        lang = 'es'
        resposta = f"¡Qué onda, güey! Sobre '{prompt}', ¡a darle con todo!"
    elif "Espanhol" in voz:
        lang = 'es'
        resposta = f"Respecto a '{prompt}', esto lo resolvemos enseguida."
    else:
        lang = 'pt'
        resposta = f"Entendi a tua questão sobre '{prompt}'. Vamos lá resolver isto juntos!"

    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)
        
        audio_file = "voz_resp.mp3"
        if os.path.exists(audio_file):
            try:
                os.remove(audio_file)
            except:
                pass
        try:
            tts = gTTS(text=resposta, lang=lang, slow=False)
            tts.save(audio_file)
            if os.path.exists(audio_file):
                st.audio(audio_file, format="audio/mp3")
        except:
            pass
