import streamlit as st
import re
import math

st.set_page_config(page_title="Impossível", page_icon="🤖")

# Gestão dinâmica do nome do utilizador
if "user_name" not in st.session_state:
    st.session_state.user_name = "Derick"

st.title("🤖 Impossível")

# Barra lateral para configurar quem está a usar a aplicação
with st.sidebar:
    st.header("⚙️ Definições")
    nome_inserido = st.text_input("Quem está a usar?", value=st.session_state.user_name)
    if nome_inserido != st.session_state.user_name:
        st.session_state.user_name = nome_inserido
        st.rerun()

st.write(f"Olá, {st.session_state.user_name}! Eu sou o Impossível, o teu assistente inteligente.")

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
    resposta_conteudo = None
    
    try:
        limpo = prompt_lower.replace("quanto é", "").replace("quanto vale", "").replace("calcule", "").replace("=", "").strip()
        
        # 1. Deteção de Raízes (Quadradas e Cúbicas)
        if "raiz" in limpo:
            numeros_encontrados = re.findall(r'\d+', limpo)
            if numeros_encontrados:
                num = float(numeros_encontrados[0])
                if "cubica" in limpo or "cúbica" in limpo or "terceira" in limpo:
                    resultado = num ** (1/3)
                    resposta_conteudo = f"A raiz cúbica de `{num}` é aproximadamente **{resultado:.4f}**."
                else:
                    resultado = math.sqrt(num)
                    resposta_conteudo = f"A raiz quadrada de `{num}` é **{resultado}**."
        
        # 2. Deteção de Potências
        elif "^" in limpo or "elevado" in limpo or "potência" in limpo:
            expressao = limpo.replace("elevado a", "**").replace("elevado", "**").replace("^", "**")
            expressao_limpa = "".join([c for c in expressao if c in "0123456789*(). "])
            if "**" in expressao_limpa:
                resultado = eval(expressao_limpa)
                resposta_conteudo = f"O resultado da potência `{expressao_limpa.strip()}` é **{resultado}**."
        
        # 3. Operações Matemáticas Básicas
        else:
            expressao = limpo.replace("vezes", "*").replace("×", "*").replace("multiplicado por", "*")
            expressao = re.sub(r'\bex\b|\bx\b', '*', expressao)
            expressao = expressao.replace("mais", "+").replace("menos", "-").replace("dividido por", "/")
            
            if any(op in expressao for op in ["+", "-", "*", "/"]):
                expressao_limpa = "".join([c for c in expressao if c in "0123456789+-*/(). "])
                if expressao_limpa.strip():
                    resultado = eval(expressao_limpa)
                    resposta_conteudo = f"O resultado exato de `{expressao_limpa.strip()}` é **{resultado}**."
    except:
        pass

    # Lógica de resposta estruturada (Matemática vs Português/Linguística)
    if resposta_conteudo:
        emoji = "⚡" if "raiz" in prompt_lower or "elevado" in prompt_lower or "^" in prompt_lower else "🧮"
        response = f"{emoji} {st.session_state.user_name}, analisei a tua questão com rigor absoluto!\n\n{resposta_conteudo}\n\n* **Conceito:** O cálculo foi processado e validado com sucesso."
    
    # Módulo de Português e Géneros Textuais
    elif "verbo" in prompt_lower:
        response = f"📖 {st.session_state.user_name}, o **verbo** é a classe de palavras que indica **ação, estado, mudança de estado ou fenômeno da natureza**. Flexiona-se em tempo, modo, pessoa, número e voz.\n\n* **Exemplos:** *correr* (ação), *ficar* (estado), *chover* (fenómeno da natureza)."
    elif "advérbio" in prompt_lower or "adverbio" in prompt_lower:
        response = f"📖 {st.session_state.user_name}, o **advérbio** é a palavra invariável que modifica o sentido de um verbo, de um adjetivo ou de outro advérbio, indicando circunstâncias (como tempo, lugar, modo, intensidade).\n\n* **Exemplos:** *rapidamente* (modo), *ontem* (tempo), *muito* (intensidade), *aqui* (lugar)."
    elif "notícia" in prompt_lower or "noticia" in prompt_lower:
        response = f"📰 {st.session_state.user_name}, uma **notícia** é um género textual jornalístico, informativo e de caraterística narrativa, cujo objetivo principal é relatar um acontecimento real, atual e de interesse público de forma clara e objetiva."
    elif "poesia" in prompt_lower or "poema" in prompt_lower:
        response = f"诗 {st.session_state.user_name}, a **poesia** (ou poema) é uma manifestação artística e literária que utiliza a palavra em sua dimensão estética, rítmica e simbólica, frequentemente estruturada em versos e estrofes para evocar emoções e sentimentos profundos."
    elif "género textual" in prompt_lower or "genero textual" in prompt_lower or "gêneros textuais" in prompt_lower:
        response = f"📚 {st.session_state.user_name}, os **géneros textuais** são as diferentes formas e estruturas que utilizamos nos textos para nos comunicarmos em situações sociais específicas. Eles variam conforme o objetivo, o público e o contexto (como cartas, notícias, receitas, crónicas, poemas, etc.)."
    elif "texto" in prompt_lower:
        response = f"📝 {st.session_state.user_name}, um **texto** é qualquer conjunto de palavras e frases estruturado que transmite uma mensagem com sentido completo, permitindo a comunicação entre emissor e recetor."
    elif any(word in prompt_lower for word in ["robô", "tecnologia", "computador", "código", "ia", "github"]):
        response = f"🤖 Compreendi o teu apontamento tecnológico, {st.session_state.user_name}. Os sistemas processam dados com total exatidão!"
    else:
        response = f"💡 Entendi o que mencionaste sobre '{prompt}', {st.session_state.user_name}. Vamos continuar a evoluir o nosso projeto com máxima dedicação!"

    # Guardar e mostrar a resposta do assistente
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

        
  
