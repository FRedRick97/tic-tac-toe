# tic tac toe

mylist = [[0 for x in range(3)] for x in range(3)]
options = []
end_game,player_dict = True, {}
posi_list = {}

def reset_board():
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            mylist[i][j] = ' '

def print_board():
    print(f'{mylist[0][0]} | {mylist[0][1]} | {mylist[0][2]}')
    print('_' *10)
    print(f'{mylist[1][0]} | {mylist[1][1]} | {mylist[1][2]}')
    print('_' *10)
    print(f'{mylist[2][0]} | {mylist[2][1]} | {mylist[2][2]}')

def sideways(row, col, symbol):
    temp = 0
    for i in range(3):
        if(mylist[row][i] == symbol):
            temp = temp + 1
        else:
            temp = 0
    if temp != 3:
        for i in range(3):
            if(mylist[i][col] == symbol):
                temp = temp + 1
            else:
                temp = 0
                break

    if(temp == 3):
        return 1
    else:
        return 0


def diagnol(row, col, symbol):
    temp = 0
    if(row == col):
        j = 0
        for i in range(3):
            if(mylist[i][j] == symbol):
                temp = temp + 1
                j = j + 1
            else:
                temp = 0
                break
    if(abs(row - col ) == 2 or (row == col == 1)):
        j = 2
        for i in range(3):
            if(mylist[i][j] == symbol):
                temp = temp + 1
                j = j - 1
            else:
                temp = 0
                break
    if(temp == 3):
        return 1
    else:
        return 0

def check(row,col, symbol):
    temp, temp2 = sideways(row, col,symbol), diagnol(row, col,symbol)
    if(temp):
        return temp
    elif (temp2):
        return temp2
    else:
        return temp


def turn(player):
    flag = True
    posi = int(input('Choose position to enter ::\n'))
    while (flag):
        if posi in posi_list:
            move = update(posi, player)
            flag = False
        else:
            posi = int(input("Incorrect or filled position. Try Again!!!\n"))
    if(len(posi_list) <= 4):
        win = check(move[0],move[1], mylist[move[0]][move[1]])
        if (win == 0):
            if(len(posi_list) == 0):
                print('*************** ITS A DRAW ***************')
                last_code()
            pass
        else:
            print('\n' * 10)
            print('*' *10, end= ' ')
            print(f'{player_dict[player]} Wins :) xD ', '*' *10 )
            last_code()

def last_code():
    global player_dict
    player_dict = {}
    print("Do you wish to play again ?")
    res = input("Press 'y' or 'n' to answer.\n")
    if(res == 'y' or res == 'Y'):
        main_game()
    else:
        print('Thank You for playing. Have a nice day!')
        exit()

def update(x, symbol):
    a,b = posi_list[x][0], posi_list[x][1]
    mylist[a][b] = symbol
    posi_list.pop(x)
    print_board()
    return [a,b]

def main_game():
    global options
    global posi_list
    options = ['X', '0']
    posi_list = dict(zip([i for i in range(1,10)],[([x,i]) for x in range(3) for i in range(3)]))
    reset_board()
    print_board()
    p1,p2 = 0, 0
    x = True
    while (x):
        p1 = input("\n\nChoose 'X' or '0' for player 1\n")
        if(p1.upper() in options):
            options.remove(p1.upper())
            player_dict.update({p1: 'PLAYER 1', options[0]: 'PLAYER 2'})
            x = False
            p2 = options[0]
        else:
            print('Incorrect Value. Try Again\n\n\n')
    while (end_game):
        print('********* PLAYER 1 TURN *********')
        turn(p1)
        print('********* PLAYER 2 TURN *********')
        turn(p2)

main_game()