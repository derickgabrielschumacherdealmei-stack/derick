import streamlit as st
from gtts import gTTS

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="IA Impossível", page_icon="🤖", layout="wide")

st.title("🤖 IA Impossível - O teu Assistente")

# --- MENU DE DEFINIÇÕES E IDIOMAS NA BARRA LATERAL ---
st.sidebar.title("⚙️ Definições da IA")

# Secção de Idioma e Nome
idioma = st.sidebar.selectbox("Idioma", ["Português (Brasil)", "Português (Portugal)", "Inglês"])
nome_ia = st.sidebar.text_input("Nome da IA", value="Impossível")

st.sidebar.markdown("---")
st.sidebar.subheader("🎙️ Mudar Estilo de Voz")

# Opção para mostrar o painel avançado de voz (agora sem esconder o chat)
ativar_painel_voz = st.sidebar.checkbox("Ativar painel avançado de vozes", value=True)

# Variáveis para guardar a escolha por defeito caso o painel esteja fechado
voz_fem = "Padrão"
voz_masc = "Padrão"
sotaque = "Português Padrão (Brasil)"
estilo_voz = "Natural e Humana"

if ativar_painel_voz:
    # Criar duas colunas na barra lateral para organizar as opções
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        st.markdown("**Feminino**")
        voz_fem = st.radio(
            "Escolha Feminina:",
            ["Padrão", "Gaúcha (Feminina)", "Mineira (Feminina)", "Carioca (Feminina)"],
            key="radio_fem"
        )
        
    with col2:
        st.markdown("**Masculino**")
        voz_masc = st.radio(
            "Escolha Masculina:",
            ["Padrão", "Gaúcho (Masculino)", "Mineiro (Masculino)", "Carioca (Masculino)"],
            key="radio_masc"
        )

    st.markdown("---")
    st.markdown("**Textura e Estilo da Voz**")
    
    estilo_voz = st.selectbox(
        "Como quer que a voz soe?",
        [
            "Natural e Humana", 
            "Confortável e Agradável", 
            "Voz mais grossa / grave", 
            "Voz mais fina / aguda"
        ]
    )

st.sidebar.markdown("---")
if st.sidebar.button("Aplicar Configurações de Voz"):
    st.sidebar.success(f"Configuração aplicada com sucesso!")


# --- ÁREA PRINCIPAL DO CHAT (SEMPRE ACESSÍVEL) ---
st.markdown("### 💬 Conversa com a IA")

# Inicializar o histórico de mensagens do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores no ecrã
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de texto para o utilizador escrever a mensagem
if prompt := st.chat_input("Escreve a tua mensagem aqui..."):
    # Adicionar mensagem do utilizador ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta da IA com base no input
    resposta_ia = f"Olá Derick! Recebi a tua mensagem: '{prompt}'. Estou a processar tudo com o estilo de voz selecionado ({estilo_voz})."

    # Adicionar resposta da IA ao histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar áudio adaptado usando gTTS
        texto_para_voz = resposta_ia
        if "Gaúcho" in sotaque or "Gaúcha" in voz_fem:
            texto_para_voz = "Bah, guri! " + resposta_ia
        elif "Mineiro" in sotaque or "Mineira" in voz_fem:
            texto_para_voz = "Uai, sô! " + resposta_ia
            
        tts = gTTS(text=texto_para_voz, lang='pt', tld='com.br')
        tts.save("resposta_audio.mp3")
        st.audio("resposta_audio.mp3")
        
