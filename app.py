import streamlit as st
import re
import math

st.set_page_config(page_title="Impossível", page_icon="🤖")

# --- GESTÃO DE ESTADO E MEMÓRIA ---
if "user_name" not in st.session_state:
    st.session_state.user_name = "Derick"

if "idioma" not in st.session_state:
    st.session_state.idioma = "Português (Brasil)"

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- BARRA LATERAL (DEFINIÇÕES) ---
with st.sidebar:
    st.header("⚙️ Definições")
    
    # Alterar o nome de quem está a usar
    nome_inserido = st.text_input("Quem está a usar?", value=st.session_state.user_name)
    if nome_inserido != st.session_state.user_name:
        st.session_state.user_name = nome_inserido
        st.rerun()
        
    # Seletor de Idiomas (Português Brasil, Inglês, Espanhol e Italiano)
    idioma_escolhido = st.selectbox(
        "🌐 Idioma da IA", 
        ["Português (Brasil)", "English (Inglês)", "Español (Espanhol)", "Italiano (Italiano)"]
    )
    if idioma_escolhido != st.session_state.idioma:
        st.session_state.idioma = idioma_escolhido
        st.rerun()

# --- TÍTULO E BOAS-VINDAS CONSOANTE O IDIOMA ---
st.title("🤖 Impossível")

if st.session_state.idioma == "English (Inglês)":
    st.write(f"Hello, {st.session_state.user_name}! I am Impossível, your intelligent assistant.")
    placeholder_text = "What do you want to say to Impossível?"
elif st.session_state.idioma == "Español (Espanhol)":
    st.write(f"¡Hola, {st.session_state.user_name}! Soy Impossível, tu asistente inteligente.")
    placeholder_text = "¿Qué le quieres decir a Impossível?"
elif st.session_state.idioma == "Italiano (Italiano)":
    st.write(f"Ciao, {st.session_state.user_name}! Sono Impossível, il tuo assistente intelligente.")
    placeholder_text = "Cosa vuoi dire a Impossível?"
else:
    st.write(f"Olá, {st.session_state.user_name}! Eu sou o Impossível, o teu assistente inteligente.")
    placeholder_text = "O que você quer dizer ao Impossível?"

# --- MOSTRAR O HISTÓRICO DE MENSAGENS (MEMÓRIA) ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CAIXA DE TEXTO ---
if prompt := st.chat_input(placeholder_text):
    # Guardar e mostrar a mensagem do utilizador
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    prompt_lower = prompt.lower()
    resposta_conteudo = None
    
    try:
        limpo = prompt_lower.replace("quanto é", "").replace("quanto vale", "").replace("calcule", "").replace("=", "").strip()
        
        # 1. Deteção de Raízes
        if "raiz" in limpo or "root" in limpo or "radice" in limpo:
            numeros_encontrados = re.findall(r'\d+', limpo)
            if numeros_encontrados:
                num = float(numeros_encontrados[0])
                if "cubica" in limpo or "cúbica" in limpo or "cubic" in limpo:
                    resultado = num ** (1/3)
                    resposta_conteudo = f"A raiz cúbica de `{num}` é aproximadamente **{resultado:.4f}**."
                else:
                    resultado = math.sqrt(num)
                    resposta_conteudo = f"A raiz quadrada de `{num}` é **{resultado}**."
        
        # 2. Deteção de Potências
        elif "^" in limpo or "elevado" in limpo or "potência" in limpo or "power" in limpo or "potenza" in limpo:
            expressao = limpo.replace("elevado a", "**").replace("elevado", "**").replace("^", "**").replace("power", "**")
            expressao_limpa = "".join([c for c in expressao if c in "0123456789*(). "])
            if "**" in expressao_limpa:
                resultado = eval(expressao_limpa)
                resposta_conteudo = f"O resultado da potência `{expressao_limpa.strip()}` é **{resultado}**."
        
        # 3. Operações Matemáticas Básicas
        else:
            expressao = limpo.replace("vezes", "*").replace("×", "*").replace("multiplicado por", "*").replace("times", "*").replace("per", "*")
            expressao = re.sub(r'\bex\b|\bx\b', '*', expressao)
            expressao = expressao.replace("mais", "+").replace("menos", "-").replace("dividido por", "/").replace("plus", "+").replace("minus", "-")
            
            if any(op in expressao for op in ["+", "-", "*", "/"]):
                expressao_limpa = "".join([c for c in expressao if c in "0123456789+-*/(). "])
                if expressao_limpa.strip():
                    resultado = eval(expressao_limpa)
                    resposta_conteudo = f"O resultado exato de `{expressao_limpa.strip()}` é **{resultado}**."
    except:
        pass

    # --- RESPOSTAS COM TRADUÇÃO DINÂMICA CONSOANTE O IDIOMA ---
    if resposta_conteudo:
        response = f"🧮 {st.session_state.user_name}, analisei a tua questão com rigor absoluto!\n\n{resposta_conteudo}"
    
    elif "verbo" in prompt_lower or "verb" in prompt_lower or "verbo" in prompt_lower:
        if st.session_state.idioma == "English (Inglês)":
            response = f"📖 {st.session_state.user_name}, a **verb** is a word that expresses an action, state, or nature phenomenon (e.g., *run*, *be*, *rain*)."
        elif st.session_state.idioma == "Español (Espanhol)":
            response = f"📖 {st.session_state.user_name}, un **verbo** es la clase de palabra que indica acción, estado o proceso (ej: *correr*, *ser*, *llover*)."
        elif st.session_state.idioma == "Italiano (Italiano)":
            response = f"📖 {st.session_state.user_name}, un **verbo** è una parola che indica un'azione, uno stato o un evento (es. *correre*, *essere*)."
        else:
            response = f"📖 {st.session_state.user_name}, o **verbo** é a classe de palavras que indica **ação, estado ou fenómeno da natureza** (ex: *correr*, *ficar*, *chover*)."
            
    elif "advérbio" in prompt_lower or "adverb" in prompt_lower or "adverbio" in prompt_lower:
        if st.session_state.idioma == "English (Inglês)":
            response = f"📖 {st.session_state.user_name}, an **adverb** modifies a verb, adjective, or another adverb, indicating circumstances like time, place, or manner."
        else:
            response = f"📖 {st.session_state.user_name}, o **advérbio** é a palavra invariável que modifica o verbo, adjetivo ou outro advérbio (ex: *rapidamente*, *ontem*, *muito*)."
            
    elif "notícia" in prompt_lower or "news" in prompt_lower or "noticia" in prompt_lower:
        if st.session_state.idioma == "English (Inglês)":
            response = f"📰 {st.session_state.user_name}, **news** is an informative journalistic text genre aiming to report a real and current public event."
        else:
            response = f"📰 {st.session_state.user_name}, uma **notícia** é um género jornalístico que relata um acontecimento real e de interesse público."
            
    elif "poesia" in prompt_lower or "poetry" in prompt_lower or "poesia" in prompt_lower:
        if st.session_state.idioma == "English (Inglês)":
            response = f"诗 {st.session_state.user_name}, **poetry** is an artistic and literary expression using rhythmic and symbolic language to evoke emotions."
        else:
            response = f"诗 {st.session_state.user_name}, a **poesia** é uma manifestação artística que utiliza a palavra em sua dimensão estética e rítmica."
            
    elif any(word in prompt_lower for word in ["robô", "tecnologia", "computer", "technology", "tecnología", "computer"]):
        response = f"🤖 {st.session_state.user_name}, os sistemas processam dados com total exatidão!"
    else:
        response = f"💡 Entendi o que mencionaste, {st.session_state.user_name}. Vamos continuar a evoluir o nosso projeto!"

    # Guardar e mostrar a resposta na memória do chat
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
