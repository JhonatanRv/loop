tentativa = 0 

while tentativa < 3:
    senha = input("digite a senha: ")
    if senha == "senha123":
        print("Acesso conedido")
        break
    else:
        print("Senha incorreta, tente novamente.")
        tentativa += 1
else:
    print("Você excedeu o número máximo de tentivas")
        