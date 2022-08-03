from pynput.keyboard import Listener
import console
from console import *

#=======================DECLARAÇÃO DE VARIAVES MUTAVEIS==========================

class variaveis_globais: 
    x = 0
    y = 20
    jogo = [
    ' ',' ',' ',
    ' ',' ',' ',
    ' ',' ',' ' 
    ]
    menu = True
    game = False
    botao_menu = ['Jogar','História do jogo e creditos','Sair']
    player1 = True
    player2 = False
    vez = 'PLAYER 1'
    espera = 'PLAYER 2'
    msg = ''
    start = 0
    end_game = '  '

#=======FUNÇÕES QUE SÓ SERAÕ UTILIZADAS ESPECIFICAMENTE SEM CONEXAO COM O JOGO========print('SE MOVA COM WASD')
class funçoes_especificas: 
    def menu():
        gotoxy(0,10)
        print(' '* 48 +'   _                            _                       _  _            ')
        print(' '* 48 +'  (_)  ___    __ _   ___     __| |  __ _  __   __  ___ | || |__    __ _')
        print(' '* 48 +"  | | / _ \  / _` | / _ \   / _` | / _` | \ \ / / / _ \| || '_ \  / _` |'")
        print(' '* 48 +'  | || (_) || (_| || (_) | | (_| || (_| |  \ V / |  __/| || | | || (_| |')
        print(' '* 48 +' _/ | \___/  \__, | \___/   \__,_| \__,_|   \_/   \___||_||_| |_| \__,_|')
        print(' '* 48 +'|__/         |___/                                                      ')
        gotoxy(48,20)
        print(variaveis_globais.botao_menu[0])
        gotoxy(48,25)
        print(variaveis_globais.botao_menu[1])
        gotoxy(48,30)
        print(variaveis_globais.botao_menu[2])
        
    def history():
        console.clear()
        gotoxy(10,5)
        print("""
        
       ▄█    █▄     ▄█     ▄████████     ███      ▄██████▄     ▄████████  ▄█     ▄████████ 
      ███    ███   ███    ███    ███ ▀█████████▄ ███    ███   ███    ███ ███    ███    ███ 
      ███    ███   ███▌   ███    █▀     ▀███▀▀██ ███    ███   ███    ███ ███▌   ███    ███ 
     ▄███▄▄▄▄███▄▄ ███▌   ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀ ███▌   ███    ███ 
    ▀▀███▀▀▀▀███▀  ███▌ ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀   ███▌ ▀███████████ 
      ███    ███   ███           ███     ███     ███    ███ ▀███████████ ███    ███    ███ 
      ███    ███   ███     ▄█    ███     ███     ███    ███   ███    ███ ███    ███    ███ 
      ███    █▀    █▀    ▄████████▀     ▄████▀    ▀██████▀    ███    ███ █▀     ███    █▀  
                                                              ███    ███                   

        
        O jogo se popularizou na Inglaterra do século 19, quando mulheres se reuniam        CONTROLES:
    nos finais de tarde para conversar e bordar. Porém, as mais idosas, por não             W A S D = MOVIMENTAÇÃO
    conseguirem mais bordar em razão de suas vistas fracas, se entretiam com o              ENTER = COMFIRMAR
    jogo. que passou a ser chamado de Noughts and Crosses (nós e cruzes, em português.      F = VOLTAR AO MENU
    Uma referência ao bordado). E como era jogado por mulheres inglesas                     R = RECOMEÇAR JOGO
    idosas, quando o jogo veio para o Brasil, ficou conhecido como Jogo da Velha.           ESC = FECHAR JOGO


        Mas a origem do jogo é muito mais antiga... escavações realizadas no templo de
    Kurna, no Egito, encontraram referências a ele que datavam do século 14 antes
    de Cristo, mas outros achados arqueológicos comprovam que o Jogo da Velha e
    muitos outros passatempos similares foram desenvolvidos independentemente
    nas mais diferentes regiões do planeta: ele também era jogado na China antiga,
    na América pré-colombiana e no Império Romano, entre outros.


        Em 1952, foi desenvolvido o jogo OXO para computador EDSAC, onde o jogador
    desafiava o computador em partidas de Jogo da Velha. Assim, surgia um dos
    primeiros jogos de vídeo game do qual se tem notícia.



    Código feito e idealizado por Vitor Roberto Gomes Queiroz ♥
""")

#=============================FUNÇOES QUE MOVEM O JOGO=========================
class funçoes_gerais(): 
    def mapa():
        gotoxy(110,10)
        print(f'VEZ DO {variaveis_globais.vez}')
        gotoxy(110,12)
        print(variaveis_globais.msg)
        for i in range(3):
            gotoxy(69,10*i+10)
            print(f'         ║         ║         ')
            gotoxy(69,10*i+11)
            print(f'         ║         ║         ')
            gotoxy(69,10*i+12)
            print(f'         ║         ║         ')
            gotoxy(69,10*i+13)
            print(f'         ║         ║         ')
            gotoxy(69,10*i+14)
            print(f'    {variaveis_globais.jogo[i*3]}    ║    {variaveis_globais.jogo[(i*3)+1]}    ║    {variaveis_globais.jogo[(i*3)+2]}    ')
            gotoxy(69,10*i+15)
            print(f'         ║         ║         ')
            gotoxy(69,10*i+16)
            print(f'         ║         ║         ')
            gotoxy(69,10*i+17)
            print(f'         ║         ║         ')
            gotoxy(69,10*i+18)
            print(f'         ║         ║         ')
            if i == 0 or i == 1:
                gotoxy(69,10*i+19)
                print(f'═════════╬═════════╬═════════')
    def cursor(x,y):
        if variaveis_globais.menu:
            gotoxy(45,y)
            print('->')
        elif variaveis_globais.game:
            gotoxy(x+71,y+14)
            print('>')
            gotoxy(x+75,y+14)
            print('<')
            variaveis_globais.msg = ''
    
    def comfirmar(x,y):
        x = int(x/10)
        y = int(y/10)
        if variaveis_globais.jogo[x+(3*y)] != ' ':
            variaveis_globais.msg = 'LUGAR OCUPADO!!'
        elif variaveis_globais.player1 == True:
            variaveis_globais.jogo[x+(3*y)] = 'X'
            variaveis_globais.player1 = False
            variaveis_globais.player2 = True
            variaveis_globais.vez = 'PLAYER 2'
            variaveis_globais.espera = 'PLAYER 1'
        elif variaveis_globais.player2 == True:
            variaveis_globais.jogo[x+(3*y)] = 'O'
            variaveis_globais.player2 = False
            variaveis_globais.player1 = True
            variaveis_globais.vez = 'PLAYER 1'
            variaveis_globais.espera = 'PLAYER 2'
    
    def marcaçao():
        
        if list(variaveis_globais.end_game)[1] == 'D':
            if (variaveis_globais.end_game)[0] == '1':
                for i in range(29):
                    if not i in (4,9,14,19,24):
                        gotoxy(69+i,10+i)
                        print("\\")
            else:
                for i in range(29):
                    if not i in (4,9,14,19,24):
                        gotoxy(97-i,10+i)
                        print("/")
        elif list(variaveis_globais.end_game)[1] == 'H':
            for i in range(29):
                if not i in (4,9,14,19,24):
                    gotoxy(69+i,14+10*int(list(variaveis_globais.end_game)[0]))
                    print('-')
        elif list(variaveis_globais.end_game)[1] == 'V':
            for i in range(29):
                if not i in (4,9,14,19,24):
                    gotoxy(73+int(list(variaveis_globais.end_game)[0])*10,10+i)
                    print('|')
    def checar():
        for i in range(3):
            if (variaveis_globais.jogo[i*3] == variaveis_globais.jogo[(i*3)+1] == variaveis_globais.jogo[(i*3)+2]) and variaveis_globais.jogo[i*3] != ' ':
                variaveis_globais.msg = f'{variaveis_globais.espera} VENCEU!!      APERTE R PARA REINICIAR'
                variaveis_globais.game = False
                variaveis_globais.end_game = f'{i}H'
            elif (variaveis_globais.jogo[i] == variaveis_globais.jogo[i+3] == variaveis_globais.jogo[i+6]) and variaveis_globais.jogo[i] != ' ':
                variaveis_globais.msg = F'{variaveis_globais.espera} VENCEU!!      APERTE R PARA REINICIAR'
                variaveis_globais.game = False
                variaveis_globais.end_game = f'{i}V'
        if (variaveis_globais.jogo[0] == variaveis_globais.jogo[4] == variaveis_globais.jogo[8]) and variaveis_globais.jogo[8] != ' ':
            variaveis_globais.msg = F'{variaveis_globais.espera} VENCEU!!      APERTE R PARA REINICIAR'
            variaveis_globais.game = False
            variaveis_globais.end_game = '1D'
        elif (variaveis_globais.jogo[2] == variaveis_globais.jogo[4] == variaveis_globais.jogo[6]) and variaveis_globais.jogo[6] != ' ':
            variaveis_globais.msg = F'{variaveis_globais.espera} VENCEU!!      APERTE R PARA REINICIAR'
            variaveis_globais.game = False
            variaveis_globais.end_game = '2D'
        elif len([i for i in variaveis_globais.jogo if i != ' ']) == 9:
            variaveis_globais.msg = 'DEU VELHA!!      APERTE R PARA REINICIAR'
            variaveis_globais.game = False
            variaveis_globais.end_game = 'NN'

console.clear()
variaveis_globais.y = 20
variaveis_globais.menu = True
variaveis_globais.game = False
funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
funçoes_especificas.menu()

#==============================MOVIMENTO DAS TECLAS==============================
def press(key):
    if str(key) == "'w'":
        
        if variaveis_globais.menu:
            console.clear()
            variaveis_globais.y -= 5
            if variaveis_globais.y < 20:
                variaveis_globais.y = 30
            funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
            funçoes_especificas.menu()

        if variaveis_globais.game:   
            
            if variaveis_globais.y >= 10:
                console.clear()
                variaveis_globais.y -= 10
                funçoes_gerais.mapa()
                funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)

    if str(key) == "'f'":
        
        console.clear()
        variaveis_globais.start = 0
        variaveis_globais.y = 20
        variaveis_globais.menu = True
        variaveis_globais.game = False
        funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
        funçoes_especificas.menu()

    if str(key) == "'s'":
        
        if variaveis_globais.menu:
            console.clear()
            variaveis_globais.y += 5
            if variaveis_globais.y > 30:
                variaveis_globais.y = 20
            funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
            funçoes_especificas.menu()
        
        if variaveis_globais.game:
            
            if variaveis_globais.y <= 10:
                console.clear()
                variaveis_globais.y += 10
                funçoes_gerais.mapa()
                funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
    
    if str(key) == "'d'":

        if variaveis_globais.game:

            if variaveis_globais.x < 20:
                console.clear()
                variaveis_globais.x += 10
                funçoes_gerais.mapa()
                funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
    
    if str(key) == "'a'":

        if variaveis_globais.game:

            if variaveis_globais.x >= 10:
                console.clear()
                variaveis_globais.x -= 10
                funçoes_gerais.mapa()
                funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
    
    if str(key) == "'r'":
        if variaveis_globais.game:
            variaveis_globais.jogo = [' ' for i in range(9)]
            variaveis_globais.game = True
            console.clear()
            variaveis_globais.msg = ''
            funçoes_gerais.mapa()
            funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
            variaveis_globais.end_game = '  '
    if str(key) == "Key.esc":
        console.clear()
        quit()
    
    if str(key) == "Key.enter":

        if variaveis_globais.menu:

            if variaveis_globais.y/5 == 4:
                console.clear()
                variaveis_globais.y = 0
                variaveis_globais.menu = False
                variaveis_globais.game = True
                variaveis_globais.start += 1
                funçoes_gerais.mapa()
                funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)

            if variaveis_globais.y/5 == 5:
        
                console.clear()
                variaveis_globais.menu = False
                funçoes_especificas.history()

            if variaveis_globais.y/5 == 6:
                console.clear()
                quit()
        if variaveis_globais.game and variaveis_globais.start > 1:
            console.clear()
            funçoes_gerais.comfirmar(variaveis_globais.x,variaveis_globais.y)
            funçoes_gerais.checar()
            funçoes_gerais.mapa()
            funçoes_gerais.cursor(variaveis_globais.x,variaveis_globais.y)
            funçoes_gerais.marcaçao()
        if variaveis_globais.game:
            variaveis_globais.start += 1


def release(key):
    pass

with Listener(on_press=press, on_release=release) as l:
    l.join()

