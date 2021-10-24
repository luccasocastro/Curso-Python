num = int(input('Digite um numero:'))
div = num/10
cont = 1

while(div >= 0):
    div = div/10
    cont = cont+1

print(f'{num} foi dividido por 10 {cont} vezes')