try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'Problema encontrado: {erro.__class__}')
    
