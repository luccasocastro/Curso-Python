def efidexis(x: float) -> float:
    return (x**3)+(6*(x**2))+(2*x+1)

def efidexis_linha(x: float) -> float:
    return (3*(x**2))+(12*x)+2

def func(xn: float, f1: float, f2: float) -> float:
    return xn - (f1/f2)

def epsulon(dif: float) -> bool:
    if dif < 10**-1:
        return True
    else:
        return False

xn = -5.75527
resfunc = func(xn, efidexis(xn), efidexis_linha(xn))
ep = epsulon(0.07442)
resfx = efidexis(resfunc)

print(f'Resfunc: {resfunc:.5f} Resfx: {resfx:.5f} Epsulon: {ep}')