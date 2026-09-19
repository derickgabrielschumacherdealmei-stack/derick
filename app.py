import streamlit as st
import re

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

    prompt_lower = prompt.lower()
    
    # Tentar detetar operações matemáticas simples com números na frase (ex: 2 + 2)
    resposta_matematica = None
    
    try:
        # Limpar o texto para extrair expressões matemáticas básicas
        # Procura por padrões como X + Y, X - Y, etc.
        limpo = prompt.replace("quanto é", "").replace("quanto vale", "").replace("=", "").strip()
        
        # Se contiver operadores e números, tenta calcular com segurança
        if any(op in limpo for op in ["+", "-", "*", "×", "/", "dividido", "vezes", "mais", "menos"]):
            # Substituições amigáveis para cálculo
            expressao = limpo.replace("mais", "+").replace("menos", "-").replace("vezes", "*").replace("×", "*").replace("dividido por", "/").replace("dividir", "/")
            # Manter apenas números, operadores e pontos/espaços
            expressao_limpa = "".join([c for c in expressao if c in "0123456789+-*/(). "])
            if expressao_limpa.strip():
                resultado = eval(expressao_limpa)
                resposta_matematica = f"O resultado exato de `{expressao_limpa.strip()}` é **{resultado}**."
    except:
        pass

    # Lógica de resposta
    if resposta_matematica:
        emoji = "🧮"
        response = f"{emoji} Analisei a tua conta com precisão absoluta!\n\n{resposta_matematica}\n\n* **Conceito:** Cada operação matemática processa os valores introduzidos de forma rigorosa para garantir um resultado correto."
    elif any(op in prompt_lower for op in ["potência", "potenciacao", "elevado", "^"]):
        emoji = "⚡"
        response = f"⚡ Analisei a tua questão sobre **potenciação** acerca de '{prompt}'. A potenciação multiplica a base por si mesma com base no expoente. Por exemplo, $2^3 = 2 \\times 2 \\times 2 = 8$."
    elif any(op in prompt_lower for op in ["mais", "adicionar", "soma", "+"]):
        emoji = "➕"
        response = f"➕ Analisei a tua operação de **adição**. Na adição, juntamos parcelas para obter o total. Por exemplo, $2 + 2 = 4$."
    elif any(op in prompt_lower for op in ["menos", "subtrair", "diferença", "-"]):
        emoji = "➖"
        response = f"➖ Analisei a tua operação de **subtração**. Calculamos a diferença entre os valores introduzidos."
    elif any(op in prompt_lower for op in ["vezes", "multiplicar", "produto", "*", "×"]):
        emoji = "✖️"
        response = f"✖️ Analisei a tua operação de **multiplicação**. Somamos parcelas idênticas repetidamente."
    elif any(op in prompt_lower for op in ["dividir", "divisão", "/"]):
        emoji = "➗"
        response = f"➗ Analisei a tua operação de **divisão**. Repartimos o valor em partes iguais."
    elif any(word in prompt_lower for word in ["robô", "tecnologia", "computador", "código", "ia", "github"]):
        emoji = "🤖"
        response = f"🤖 Compreendi o teu apontamento tecnológico sobre '{prompt}'. Os sistemas processam dados com extrema rapidez!"
    else:
        emoji = "💡"
        response = f"💡 Entendi o que mencionaste sobre '{prompt}'. Vamos continuar a evoluir o nosso projeto com total dedicação!"

    # Guardar e mostrar a resposta do assistente
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
