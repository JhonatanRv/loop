maior_num = -999999999

#entra com o primeiro número
number = int(input("Entre com um número ou digite -1 para parar: "))

#se o número não for -1 continua

while number != -1:
    if number > maior_num:
        maior_num = number
        
    number = int(input("Entre com um número ou digite -1 para parar: "))
    
print("O maior número é: ", maior_num)    