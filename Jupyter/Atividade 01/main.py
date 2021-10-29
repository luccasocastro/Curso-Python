windows = 0
linux = 0
unix = 0
netware = 0
macos = 0
outro = 0
total = 0
op = 1
while(op != 0):
    op = int(input('Em qual SO deseja votar?\n1 - Windows\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\nDigite 0 para sair...'))
    
    if op == 1:
        windows += 1
    elif op == 2:
        unix += 1
    elif op == 3:
        linux += 1
    elif op == 4:
        netware += 1
    elif op == 5:
        macos += 1
    elif op == 6:
        outro += 1

