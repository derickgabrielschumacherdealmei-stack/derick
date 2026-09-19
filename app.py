import streamlit as st

st.title("🤖 Impossível")
st.write("Olá, Derick! Eu sou a Impossível, a tua assistente.")

# Histórico de mensagens do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensagens antigas no ecrã
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de texto para o usuário escrever
if entrada_usuario := st.chat_input("O que queres dizer à Impossível?"):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": entrada_usuario})
    with st.chat_message("user"):
        st.markdown(entrada_usuario)

    # Processar a resposta da IA
    entrada_limpa = entrada_usuario.strip().lower()
    
    if entrada_limpa in ["olá", "ola", "oi", "opa", "e aí", "e ai"]:
        resposta = "Olá, eu sou a Impossível. O que posso te ajudar hoje?"
        
    elif any(op in entrada_limpa for op in ["+", "-", "*", "/"]):
        try:
            resultado = eval(entrada_limpa)
            resposta = f"O resultado da conta é {resultado}"
        except Exception:
            resposta = "Hum, vi que tentaste fazer uma conta, mas não consegui calcular bem. Podes escrever de outra forma?"
            
    else:
        resposta = "Entendi o que disseste, vamos continuar a melhorar a nossa IA!"

    # Mostrar resposta da IA no chat
    with st.chat_message("assistant"):
        st.markdown(resposta)
    
    # Guardar resposta no histórico
    st.session_state.messages.append({"role": "assistant", "content": resposta})
