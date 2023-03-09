palavra = ""
user_pa = input("Entre com uma palavra: ")
user_pa = user_pa.upper()

for letra in user_pa:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palavra += letra
        
print(palavra)        