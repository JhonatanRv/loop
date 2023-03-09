#Exemplo 1
contador = 1
while  contador  < 5:
    print(contador)
    contador += 1 
    
#Exemplo 2
num = 0
while num < 10:
    if num == 0:
        print("O número é zero ", num)
    elif num % 2 == 0:
        print("O número é par ", num)
    else:
        print("O número é impar ", num)
    num +=1    

#Exemplo 3
for i in range(10):
    print("O valor de i atualmente é: ", i)
    
#Exemplo 4   
for var1 in range (1, 6):
    print(var1)

#Exemplo 5
for var2 in range (2, 8, 3):
    print("O valor de var é: ", var2)