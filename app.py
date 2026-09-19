print("Bem-vindo ao assistente de IA do Derick!")
print("Digite 'sair' a qualquer momento para encerrar a conversa.\n")

while True:
    pergunta_usuario = input("Você: ")
    
    # Condição para encerrar o programa
    if "sair" in pergunta_usuario.lower():
        print("Assistente: Até logo, Derick! Foi ótimo conversar com você.")
        break
        
    # Verifica o que foi digitado para dar uma resposta inteligente
    elif "olá" in pergunta_usuario.lower():
        print("Assistente: Olá, Derick! Como posso ajudar nos teus estudos ou projetos hoje?")
    elif "matemática" in pergunta_usuario.lower():
        print("Assistente: Matemática é excelente! Quer resolver alguma expressão ou equação?")
    else:
        print("Assistente: Entendi o que disseste. Vamos continuar a evoluir este assistente passo a passo!")
