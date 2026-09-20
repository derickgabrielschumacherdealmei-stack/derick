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
    
    [data-testid="stSidebar"] {
        background-color: #121212 !important;
        border-right: 1px solid #1a1a1a;
    }
    
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

    /* Caixa das Mensagens com Fundo Claro e Letras Pretas */
    .stChatMessage {
        background-color: #f0f0f0 !important;
        border: 1px solid #dcdcdc !important;
        border-radius: 14px !important;
        color: #000000 !important;
        margin-bottom: 10px;
    }
    
    .stChatMessage p, .stChatMessage div, .stChatMessage span {
        color: #000000 !important;
    }

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
""", unsafe_allow_html=True)
