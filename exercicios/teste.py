def f1(a: int, b: int, c: int)->float:
    return (a*(-1))+(b*(-1))-3*1

def f2(a: int, b: int, c: int)->float:
    return (-2*(-1))-(b*(-1))+(c*1)

def f3(a: int, b: int, c: int)->float:
    return (a*(-1))+(3*(-1))-(c*1)

a = -5/3
b = 7/6
c = 7/6

print(f'f1:{f1(a,b,c)}, f2:{f2(a,b,c)}, f3:{f3(a,b,c)}')