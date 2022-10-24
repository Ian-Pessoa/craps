import random


def menu1():
    n = input('Aperte "enter" para jogar os dados\n')
    if n == "":
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print("Primeiro dado = {}\tSegundo dado = {}\tResultado = {}".format(
            d1, d2, d1+d2))
        craps(d1, d2)


def menu2():
    print('\t\t\t\tINSTRUÇÕES\n\nO jogador lança um par de dados, obtendo um valor entre 2 e 12.\nNATURAL - Se, na primeira jogada, você tirar 7 ou 11, você tirou um "natural" e ganhou.\nCRAPS - Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.\nPONTO - Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.')


def craps(d1, d2):
    if d1+d2 == 7 or d1+d2 == 11:
        print('Parabéns! Você tirou um NATURAL e ganhou!')
    elif d1+d2 == 2 or d1+d2 == 3 or d1+d2 == 12:
        print('Ops... CRAPS! Você perdeu. :(')
    else:
        ponto = d1+d2
        print('Este é seu PONTO! Jogue novamente.\n')
        while (True):
            n = input('Aperte "enter" para jogar os dados\n')
            if n == "":
                d3 = random.randint(1, 6)
                d4 = random.randint(1, 6)
                print("Primeiro dado = {}\tSegundo dado = {}\tResultado = {}".format(
                    d3, d4, d3+d4))
                if d3+d4 == ponto:
                    print('Parabéns! Você tirou seu PONTO e venceu!')
                    break
                elif d3+d4 == 7:
                    print('Que pena! Você tirou 7 e perdeu! :(')
                    break
                else:
                    print('Jogue novamente.\n')


while (True):
    m = int(input(
        "Bem-vindo ao CRAPS !\n\tMENU\n1 - JOGAR\n2 - INSTRUÇÕES\n3 - ENCERRAR PROGRAMA\n"))
    if m == 1:
        menu1()
    elif m == 2:
        menu2()
    elif m == 3:
        break
    else:
        print('Insira um comando válido\n')
