def assistente_impossivel():
    print("Assistente Impossível iniciado...")
    
    while True:
        entrada_usuario = input("Tu: ").strip().lower()
        
        # Condição para sair do chat
        if entrada_usuario in ["sair", "fechar", "exit"]:
            print("Impossível: Até logo! Continuação de um bom trabalho.")
            break
            
        # Cumprimentos personalizados
        elif entrada_usuario in ["olá", "ola", "oi", "opa", "e aí", "e ai"]:
            print("Impossível: Olá, eu sou a Impossível. O que posso te ajudar hoje?")
            
        # Detetar cálculos matemáticos simples
        elif any(op in entrada_usuario for op in ["+", "-", "*", "/"]):
            try:
                # Remove espaços e calcula a expressão matemática de forma segura
                resultado = eval(entrada_usuario)
                print(f"Impossível: O resultado da conta é {resultado}")
            except Exception:
                print("Impossível: Hum, vi que tentaste fazer uma conta, mas não consegui calcular bem. Podes escrever de outra forma?")
            
        else:
            print("Impossível: Entendi o que disseste, vamos continuar a melhorar a nossa IA!")

# Para correr a função
if __name__ == "__main__"
