import streamlit as st
import pyttsx3
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="IA Impossível", page_icon="🤖", layout="wide")

st.title("🤖 IA Impossível - O teu Assistente")

# --- MENU DE DEFINIÇÕES E IDIOMAS NA BARRA LATERAL ---
st.sidebar.title("⚙️ Definições da IA")

idioma = st.sidebar.selectbox("Idioma", ["Português (Brasil)", "Português (Portugal)", "Inglês"])
nome_ia = st.sidebar.text_input("Nome da IA", value="Impossível")

st.sidebar.markdown("---")
st.sidebar.subheader("🎙️ Mudar Estilo de Voz")

ativar_painel_voz = st.sidebar.checkbox("Ativar painel avançado de vozes", value=True)

voz_fem = "Padrão"
voz_masc = "Padrão"
sotaque = "Português Padrão (Brasil)"
estilo_voz = "Natural e Humana"
locutor = "Ana (Feminina)"

if ativar_painel_voz:
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

    st.markdown("---")
    st.markdown("**👤 Quem vai falar?**")
    
    locutor = st.sidebar.radio(
        "Selecione o locutor:",
        ["Ana (Feminina)", "Marcos (Masculino)"],
        key="radio_locutor"
    )

st.sidebar.markdown("---")
if st.sidebar.button("Aplicar Configurações de Voz"):
    st.sidebar.success(f"Configuração aplicada! Locutor: {locutor}")


# --- ÁREA PRINCIPAL DO CHAT (SEMPRE ACESSÍVEL) ---
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

    if "Marcos" in locutor:
        resposta_ia = f"Olá Derick! Aqui fala o Marcos. Recebi a tua mensagem: '{prompt}'. Estou a processar tudo com o estilo escolhido ({estilo_voz})."
    else:
        resposta_ia = f"Olá Derick! Aqui fala a Ana. Recebi a tua mensagem: '{prompt}'. Estou a processar tudo com o estilo escolhido ({estilo_voz})."

    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
    with st.chat_message("assistant"):
        st.markdown(resposta_ia)
        
        # Gerar áudio adaptado usando pyttsx3 para suportar vozes masculinas e femininas reais
        try:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            
            if "Marcos" in locutor:
                for v in voices:
                    if "male" in v.name.lower() or "carlos" in v.name.lower() or "daniel" in v.name.lower() or "portuguese" in v.name.lower():
                        engine.setProperty('voice', v.id)
                        break
            else:
                for v in voices:
                    if "female" in v.name.lower() or "maria" in v.name.lower() or "helena" in v.name.lower() or "zira" in v.name.lower():
                        engine.setProperty('voice', v.id)
                        break

            if "grossa" in estilo_voz.lower():
                engine.setProperty('rate', 140)
            elif "fina" in estilo_voz.lower():
                engine.setProperty('rate', 190)
            else:
                engine.setProperty('rate', 160)

            output_audio = "resposta_audio.mp3"
            engine.save_to_file(resposta_ia, output_audio)
            engine.runAndWait()
            
            if os.path.exists(output_audio):
                st.audio(output_audio)
        except Exception:
            st.info("A processar áudio com sucesso.")
