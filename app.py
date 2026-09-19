print("Bem-vindo ao assistente de IA do Derick!")

pergunta_usuario = input("Digite alguma coisa para conversar: ")

# Verifica o que foi digitado para dar uma resposta inteligente
if "olá" in pergunta_usuario.lower():
    print("Assistente: Olá, Derick! Como posso ajudar nos teus estudos ou projetos hoje?")
elif "matemática" in pergunta_usuario.lower():
    print("Assistente: Matemática é excelente! Quer resolver alguma expressão ou equação?")
else:
    print("Assistente: Entendi o que disseste. Vamos continuar a evoluir este assistente passo a passo!")
