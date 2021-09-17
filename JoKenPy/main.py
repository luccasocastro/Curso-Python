import random

cont_player = 0
cont_pc = 0

while True:

    choices = ['pedra', 'papel', 'tesoura']
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('Pedra, papel ou tesoura?: ').lower()

    if player == computer:
        print('Computador: ',computer)
        print('Jogador: ',player)
        print('Empatooouu!!!')
    elif player == 'pedra':
        if computer == 'papel':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Computador ganhooouuu!!!')
            cont_pc += 1
        elif computer == 'tesoura':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Jogador ganhooouuu!!!')
            cont_player += 1

    elif player == 'papel':
        if computer == 'pedra':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Jogador ganhooouuu!!!')
            cont_player += 1
        elif computer == 'tesoura':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Computador ganhooouuu!!!')
            cont_pc += 1

    elif player == 'tesoura':
        if computer == 'pedra':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Computador ganhooouuu!!!')
            cont_pc += 1
        elif computer == 'papel':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Jogador ganhooouuu!!!')
            cont_player += 1

    play_again = input('Deseja jogar novamente? (sim/nao): ').lower()

    if play_again != "sim":
        break

print('=-=-=-=-=-=-=-=-=-=-=-=-')
print(f'Pontos computador: {cont_pc}')
print(f'Pontos jogador: {cont_player}')
if cont_pc > cont_player:
    print('Computador venceu essa disputa!!!')
elif cont_player > cont_pc:
    print('Jogador venceu essa disputa!!!')
else:
    print('A disputa termina com empate!!!')
print('Até a próxima...')
