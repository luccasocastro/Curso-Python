import random

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
        elif computer == 'tesoura':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Jogador ganhooouuu!!!')

    elif player == 'papel':
        if computer == 'pedra':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Jogador ganhooouuu!!!')
        elif computer == 'tesoura':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Computador ganhooouuu!!!')

    elif player == 'tesoura':
        if computer == 'pedra':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Computador ganhooouuu!!!')
        elif computer == 'papel':
            print('Computador: ', computer)
            print('Jogador: ', player)
            print('Jogador ganhooouuu!!!')

    play_again = input('Deseja jogar novamente? (sim/nao): ').lower()

    if play_again != "sim":
        break

print('Até a próxima...')
