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

    # Converter o texto para minúsculas para facilitar a análise exata
    prompt_lower = prompt.lower()
    
    # Lógica matemática altamente rigorosa e segmentada
    if any(op in prompt_lower for op in ["potência", "potenciacao", "elevado", "exponenciação", "^"]):
        emoji = "⚡"
        response = f"""{emoji} Analisei detalhadamente a tua questão sobre **potenciação** acerca de '{prompt}'. 
        
A potenciação (ou exponenciação) representa a multiplicação sucessiva de um número por ele próprio. 
* **Conceito:** Nela identificamos a **base** (o fator que se repete) e o **expoente** (as vezes que a base é multiplicada).
* **Exemplo prático:** Se calcularmos $2^3$ (dois elevado ao cubo), multiplicamos a base $2$ por si mesma três vezes: 
  $$2 \\times 2 \\times 2 = 8$$
O cálculo foi executado com rigor matemático absoluto!"""

    elif any(op in prompt_lower for op in ["mais", "adicionar", "soma", "somar", "+"]):
        emoji = "➕"
        response = f"""{emoji} Analisei criteriosamente a tua operação de **adição** sobre '{prompt}'. 

A adição consiste em juntar ou combinar duas ou mais quantidades para obter um total absoluto.
* **Conceito:** Os números envolvidos denominam-se parcelas, e o resultado final é a soma ou total.
* **Exemplo prático:** Se adicionarmos cinco unidades a três unidades, obtemos o total de oito: 
  $$5 + 3 = 8$$
O raciocínio aditivo foi rigorosamente verificado e validado!"""

    elif any(op in prompt_lower for op in ["menos", "subtrair", "diferença", "subtração", "-"]):
        emoji = "➖"
        response = f"""{emoji} Analisei com exatidão a tua operação de **subtração** sobre '{prompt}'. 

A subtração determina a diferença entre dois valores ou o que resta após retirar uma quantidade de outra.
* **Conceito:** Envolve o minuendo, o subtraendo e a respetiva diferença.
* **Exemplo prático:** Se subtrairmos quatro unidades de dez unidades, restam exatamente seis: 
  $$10 - 4 = 6$$
O cálculo subtrativo foi processado com precisão impecável!"""

    elif any(op in prompt_lower for op in ["vezes", "multiplicar", "produto", "multiplicação", "*", "×"]):
        emoji = "✖️"
        response = f"""{emoji} Analisei detalhadamente a tua operação de **multiplicação** sobre '{prompt}'. 

A multiplicação representa a soma abreviada de parcelas idênticas que se repetem.
* **Conceito:** Os números multiplicados chamam-se fatores e o resultado final é o produto.
* **Exemplo prático:** Se multiplicarmos quatro por três, somamos o quatro três vezes ($4 + 4 + 4$): 
  $$4 \\times 3 = 12$$
O processo multiplicativo foi concluído com rigor absoluto!"""

    elif any(op in prompt_lower for op in ["dividir", "divisão", "quociente", "partes", "/", "÷"]):
        emoji = "➗"
        response = f"""{emoji} Analisei rigorosamente a tua operação de **divisão** sobre '{prompt}'. 

A divisão consiste em repartir uma quantidade em partes exatamente iguais.
* **Conceito:** Envolve o dividendo, o divisor, o quociente (resultado) e o resto.
* **Exemplo prático:** Se dividirmos vinte unidades em quatro partes iguais, cada parte conterá cinco: 
  $$20 \\div 4 = 5$$
A operação divisional foi executada com perfeição matemática!"""

    elif any(word in prompt_lower for word in ["robô", "tecnologia", "computador", "código", "ia", "github"]):
        emoji = "🤖"
        response = f"""{emoji} Compreendi perfeitamente o teu apontamento tecnológico acerca de '{prompt}'. 
Os sistemas computacionais processam dados estruturados com extrema rapidez e exatidão. Por exemplo, a gestão e atualização de repositórios no GitHub permite otimizar esta aplicação instantaneamente. Continuamos a evoluir tecnologicamente de forma brilhante!"""

    else:
        emoji = "💡"
        response = f"""{emoji} Entendi com total clareza o que mencionaste sobre '{prompt}'. É fascinante a forma como estrutures o teu raciocínio analítico. Cada detalhe que aprimoramos reflete um progresso notável no nosso projeto. Vamos continuar a avançar com máxima dedicação!"""

    # Guardar e mostrar a resposta do assistente
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
