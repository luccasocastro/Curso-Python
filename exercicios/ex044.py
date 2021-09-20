frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A frase "{frase}" é um palíndromo!')
    print(junto)
    print(inverso)
else:
    print(f'A frase "{frase}" não é um palíndromo')
    print(junto)
    print(inverso)

