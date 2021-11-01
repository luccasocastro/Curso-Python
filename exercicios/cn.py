def y_chapeu(xi: float) -> float:
    return (0.795+0.301)*xi

def di(yi: float, ychapeu: float) -> float:
    return yi - ychapeu

def dzao(lista) -> float:
    cont = 0
    for i in lista:
        cont = cont + i**2
    return cont

v = [-0.32,0.37,-1.44,-1.75,-2.63]
res = dzao(v)
print(f'{res:.2f}')