import random

num_secreto = random.randint(0, 10)
tentativa = 1

while tentativa <= 3:
    palpite = int(input("Adivinhe o número secreto: "))
    if palpite == num_secreto:
        print("Você acertou o número!")
        break
    else:
        if palpite > num_secreto:
            print("O número secreto é menor do que ", palpite)
        else:
            print("O número secreto é maior do que", palpite)
    tentativa += 1
    if tentativa > 3:
        print("Suas tentivas acabaram o número era: ", num_secreto)
        