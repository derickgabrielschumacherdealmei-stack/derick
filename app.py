import streamlit as st
import re
import math

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
    
    resposta_matematica = None
    
    try:
        limpo = prompt_lower.replace("quanto é", "").replace("quanto vale", "").replace("calcule", "").replace("=", "").strip()
        
        # 1. Deteção de Raízes Quadradas e Cúbicas / Gerais
        if "raiz" in limpo:
            # Extrair o número após a palavra raiz
            numeros_encontrados = re.findall(r'\d+', limpo)
            if numeros_encontrados:
                num = float(numeros_encontrados[0])
                if "cubica" in limpo or "cúbica" in limpo or "terceira" in limpo:
                    resultado = num ** (1/3)
                    resposta_matematica = f"A raiz cúbica de `{num}` é aproximadamente **{resultado:.4f}**."
                else:
                    # Por defeito, raiz quadrada
                    resultado = math.sqrt(num)
                    resposta_matematica = f"A raiz quadrada de `{num}` é **{resultado}**."
        
        # 2. Deteção de Potências (ex: 2^3, 2 elevado a 3)
        elif "^" in limpo or "elevado" in limpo or "potência" in limpo:
            expressao = limpo.replace("elevado a", "**").replace("elevado", "**").replace("^", "**")
            expressao_limpa = "".join([c for c in expressao if c in "0123456789*(). "])
            if "**" in expressao_limpa:
                resultado = eval(expressao_limpa)
                resposta_matematica = f"O resultado da potência `{expressao_limpa.strip()}` é **{resultado}**."
        
        # 3. Operações Básicas (Multiplicação, Adição, Subtração, Divisão)
        else:
            expressao = limpo.replace("vezes", "*").replace("×", "*").replace("multiplicado por", "*")
            expressao = re.sub(r'\bex\b|\bx\b', '*', expressao)
            expressao = expressao.replace("mais", "+").replace("menos", "-").replace("dividido por", "/")
            
            if any(op in expressao for op in ["+", "-", "*", "/"]):
                expressao_limpa = "".join([c for c in expressao if c in "0123456789+-*/(). "])
                if expressao_limpa.strip():
                    resultado = eval(expressao_limpa)
                    resposta_matematica = f"O resultado exato de `{expressao_limpa.strip()}` é **{resultado}**."
    except:
        pass

    # Lógica de resposta estruturada
    if resposta_matematica:
        emoji = "⚡" if "raiz" in prompt_lower or "elevado" in prompt_lower or "^" in prompt_lower else "🧮"
        response = f"{emoji} Analisei a tua questão com rigor matemático absoluto!\n\n{resposta_matematica}\n\n* **Conceito:** O cálculo foi processado e validado com sucesso através de operações avançadas."
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
