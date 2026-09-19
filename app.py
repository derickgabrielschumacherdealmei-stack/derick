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
    
    # Tentar detetar operações matemáticas e calcular o resultado exato
    resposta_matematica = None
    
    try:
        # Limpar o texto para extrair expressões matemáticas
        limpo = prompt_lower.replace("quanto é", "").replace("quanto vale", "").replace("calcule", "").replace("=", "").strip()
        
        # Se contiver termos ou símbolos de multiplicação
        if any(op in limpo for op in ["*", "×", "vezes", "multiplicado por", "multiplicar"]):
            # Normalizar os operadores para o Python conseguir calcular
            expressao = limpo.replace("vezes", "*").replace("×", "*").replace("multiplicado por", "*")
            # Extrair apenas números, operadores e pontos necessários
            expressao_limpa = "".join([c for c in expressao if c in "0123456789+-*/(). "])
            if expressao_limpa.strip() and "*" in expressao_limpa:
                resultado = eval(expressao_limpa)
                resposta_matematica = f"O produto exato de `{expressao_limpa.strip()}` é **{resultado}**."
        
        # Outras operações básicas caso sejam inseridas
        elif any(op in limpo for op in ["+", "-", "/"]):
            expressao = limpo.replace("mais", "+").replace("menos", "-").replace("dividido por", "/")
            expressao_limpa = "".join([c for c in expressao if c in "0123456789+-*/(). "])
            if expressao_limpa.strip():
                resultado = eval(expressao_limpa)
                resposta_matematica = f"O resultado exato de `{expressao_limpa.strip()}` é **{resultado}**."
    except:
        pass

    # Lógica de resposta estruturada
    if resposta_matematica:
        emoji = "✖️" if "*" in prompt_lower or "vezes" in prompt_lower or "×" in prompt_lower else "🧮"
        response = f"{emoji} Analisei a tua conta com rigor absoluto!\n\n{resposta_matematica}\n\n* **Conceito:** A multiplicação consiste na soma abreviada de parcelas idênticas que se repetem sucessivamente."
    elif any(op in prompt_lower for op in ["potência", "potenciacao", "elevado", "^"]):
        emoji = "⚡"
        response = f"⚡ Analisei a tua questão sobre **potenciação**. A base é multiplicada por si mesma conforme o expoente."
    elif any(op in prompt_lower for op in ["mais", "adicionar", "soma", "+"]):
        emoji = "➕"
        response = f"➕ Analisei a tua operação de **adição**. Juntamos as parcelas para encontrar o total exato."
    elif any(op in prompt_lower for op in ["menos", "subtrair", "diferença", "-"]):
        emoji = "➖"
        response = f"➖ Analisei a tua operação de **subtração**. Calculamos a diferença entre os valores."
    elif any(op in prompt_lower for op in ["dividir", "divisão", "/"]):
        emoji = "➗"
        response = f"➗ Analisei a tua operação de **divisão**. Repartimos a quantidade em partes iguais."
    elif any(word in prompt_lower for word in ["robô", "tecnologia", "computador", "código", "ia", "github"]):
        emoji = "🤖"
        response = f"🤖 Compreendi o teu apontamento tecnológico. Os sistemas processam dados com total exatidão!"
    else:
        emoji = "💡"
        response = f"💡 Entendi o que mencionaste sobre '{prompt}'. Vamos continuar a evoluir o nosso projeto com máxima dedicação!"

    # Guardar e mostrar a resposta do assistente
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
