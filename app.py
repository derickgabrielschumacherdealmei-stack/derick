st.markdown("""
<style>
    /* Força APENAS o texto das mensagens do chat (User e Assistant) para vermelho vivo/escuro legível */
    div[data-testid="stChatMessage"] div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stChatMessage"] *,
    .stChatMessage p, 
    .stChatMessage span, 
    .stChatMessage div {
        color: #cc0000 !important;
    }
</style>
""", unsafe_allow_html=True)
