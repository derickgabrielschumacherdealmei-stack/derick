print("Bem-vindo ao assistente de IA do Derick!")
print("Digite 'sair' a qualquer momento para encerrar a conversa.\n")

while True:
    pergunta_usuario = input("Você: ")
    
    # Condição para encerrar o programa
    if "sair" in pergunta_usuario.lower():
        print("Assistente: Até logo, Derick! Foi ótimo conversar com você.")
        break
        
    # Cumprimento
    elif "olá" in pergunta_usuario.lower():
        print("Assistente: Olá, Derick! Como posso ajudar nos teus estudos ou projetos hoje?")
        
    # Explicações de Português
    elif "verbo" in pergunta_usuario.lower():
        print("Assistente: Um verbo é a palavra que indica ação, estado ou fenômeno da natureza (ex: correr, ser, chover).")
    elif "advérbio" in pergunta_usuario.lower():
        print("Assistente: Um advérbio é a palavra que modifica o sentido de um verbo, de um adjetivo ou de outro advérbio, indicando circunstâncias como tempo, modo ou lugar (ex: rapidamente, aqui, ontem).")
        
    # Deteta se o usuário digitou uma operação matemática (+, -, *, /, **)
    elif any(op in pergunta_usuario for op in ["+", "-", "*", "/", "**"]):
        try:
            # Calcula a expressão matemática digitada
            resultado = eval(pergunta_usuario)
            print(f"Assistente: O resultado de {pergunta_usuario} é {resultado}")
        except:
            print("Assistente: Hmm, ocorreu um erro ao calcular. Tente digitar a conta usando números e operadores válidos (ex: 5 + 5).")
            
    else:
        print("Assistente: Entendi o que disseste. Vamos continuar a evoluir este assistente passo a passo!")
