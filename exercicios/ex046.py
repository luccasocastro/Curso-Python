sum = 0
maior_homem = 0
nome_velho = ' '
cont_mulheres = 0
for i in range(1,5):
    print(f'=-=-=-{i}º PESSOA-=-=-=')
    nome = str(input('Informe seu nome:')).strip()
    idade = int(input('Informe a sua idade:'))
    sexo = str(input('Informe o seu sexo:')).strip()
    sum += idade

    if i == 1 and sexo in 'Mm':
        maior_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_homem:
        maior_homem = idade
        nome_velho = nome
    
    if sexo in 'Ff':
        if idade < 20:
            cont_mulheres += 1

media_idade = idade/4
print(f'A média de idades entre todos é de {media_idade} anos')
print(f'{nome_velho} é o homem mais velho com {maior_homem} anos de idade')
if cont_mulheres == 1:
    print(f'{cont_mulheres} mulher possui idade menor que 20 anos')
else:
    print(f'{cont_mulheres} mulheres possuem idade menor que 20 anos')