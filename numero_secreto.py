import random

numero_secreto = random.randint(1, 5)
num_tentativas = 0

print("Bem-vindo ao jogo de adivinhação!\nTente adivinhar o número secreto entre 1 e 5.")

while True:
    palpite = int(input("Digite um número: "))
    print(type(palpite))
    num_tentativas += 1

    if (palpite == numero_secreto):
        print("👏👏👏👏👏👏👏👏👏👏👏👏")
        break

    elif (palpite < numero_secreto):
        print("O número secreto é maior!")
        
    else:
        print("O número secreto é menor!")
