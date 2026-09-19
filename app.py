import streamlit as st

# --- MENU DE DEFINIÇÕES E IDIOMAS ---
st.sidebar.title("⚙️ Definições da IA")

# Secção de Idioma e Nome
idioma = st.sidebar.selectbox("Idioma", ["Português (Brasil)", "Português (Portugal)", "Inglês"])
nome_ia = st.sidebar.text_input("Nome da IA", value="Impossível")

st.sidebar.markdown("---")
st.sidebar.subheader("🎙️ Mudar Estilo de Voz")

# Opção para abrir o painel avançado de voz
ativar_painel_voz = st.sidebar.checkbox("Ativar painel avançado de vozes")

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

    # Botão para aplicar as configurações
    if st.button("Aplicar Configurações de Voz"):
        st.success(f"Configuração aplicada! A IA {nome_ia} vai falar com estilo selecionado.")
   
