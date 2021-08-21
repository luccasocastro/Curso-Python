nome = str(input('Digite seu nome completo: ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
semEspaços = nome.replace(" ", "")
qntdLetras = len(semEspaços)
quebrado = nome.split()
print('Nome em maiúsculo: {}'.format(maiusculo))
print('Nome em minúsculo: {}'.format(minusculo))
print('Nome sem espaços: {}'.format(semEspaços))
print('Qntd de letras do nome: {}'.format(qntdLetras))
print('Nome quebrado: {}'.format(quebrado))
print('Seu primeiro nome é {}, e ele tem {} letras'.format(quebrado[0], len(quebrado[0])))


