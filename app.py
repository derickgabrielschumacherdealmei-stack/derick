import streamlit as st

st.set_page_config(page_title="Impossível", page_icon="🤖")

st.title("🤖 Impossível")
st.write("Olá, Derick! Eu sou o Impossível, o teu assistente inteligente.")

# Inicializar o histórico de mensagens se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar as mensagens anteriores no chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caixa de texto para o utilizador escrever
if prompt := st.chat_input("O que você quer dizer ao Impossível?"):
    # Guardar e mostrar a mensagem do utilizador
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Lógica inteligente baseada no conteúdo da mensagem do Derick
    prompt_lower = prompt.lower()
    
    if any(op in prompt_lower for op in ["mais", "menos", "vezes", "dividir", "multiplicar", "potência", "matemática", "+", "-", "*", "/", "^"]):
        emoji = "🧮"
        response = f"{emoji} Analisei a tua questão matemática sobre '{prompt}'. Na matemática, utilizamos operadores fundamentais com rigor: a adição (**+**), a subtração (**-**), a multiplicação (**×**), a divisão (**÷**) e a potenciação (**$a^b$**). Por exemplo, se elevarmos uma base ao expoente, como $2^3$, calculamos multiplicando a base por si mesma três vezes ($2 \\times 2 \\times 2 = 8$). Vamos continuar a explorar estes cálculos com precisão!"
    elif any(word in prompt_lower for word in ["robô", "tecnologia", "computador", "código", "ia", "github"]):
        emoji = "🤖"
        response = f"{emoji} Compreendi perfeitamente o teu apontamento tecnológico acerca de '{prompt}'. Os sistemas computacionais processam dados estruturados com extrema rapidez. Por exemplo, a automação de scripts no GitHub permitiu colocar esta aplicação online com sucesso. Continuamos a evoluir tecnologicamente de forma brilhante!"
    else:
        emoji = "💡"
        response = f"{emoji} Entendi com clareza o que mencionaste sobre '{prompt}'. É fascinante a forma como desenvolves raciocínios complexos. Por exemplo, cada detalhe estrutural que aprimoramos reflete um progresso notável no nosso projeto. Vamos continuar a avançar com dedicação!"

    # Guardar e mostrar a resposta do assistente
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
