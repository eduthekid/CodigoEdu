import random

def adivinhe_o_numero():
    print("Bem Vindo ao jogo 'Adivinhe o Número'!")
    print("Escolhe um número entre 1 e 100")
    print("Vamos começar!\n")
    
    numero_secreto = random.randint(1,100)
    tentativas = 0
    
    while True:
        try:
            
            palpite = int(input("Digite seu palpite (1-100): "))
            
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
            
            tentativas += 1
            
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativa(s)!" )
                break
            elif palpite < numero_secreto:
                print("O número secreto é maior que o seu palpite.")
            else:
                print("O número secreto é menor que o seu palpite.")
        
        except ValueError:
            print("Por favor, digite um número inteiro.")
    
    print("\nFim de jogo! Obrigado por jogar!")
    
adivinhe_o_numero()