#game about x and 0
#this is our starting board, it is empty
the_board = { 'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
              'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
              'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#function for printing our board
def print_board(board):
    print('\n      ' + board['top-L'] + '|' + board['top-M'] + '|'+ board['top-R'])
    print('      -+-+-')
    print('      ' + board['mid-L'] + '|' + board['mid-M'] + '|'+ board['mid-R'])
    print('      -+-+-')
    print('      ' + board['low-L'] + '|' + board['low-M'] + '|'+ board['low-R'] + '\n')

#this function checks if input symbol is correct(there menu with symbols from 1 to 9)
def check_num():
    while True:
        print('Turn for ' + turn + '. Move on which space?')
        try:
            move = int(input())
            if move not in range(1,10):
                print('\nchoose number from 1 to 9\n')
            else:
                break
        except ValueError:
            print('\nchoose number from 1 to 9\n')
            continue
    return move

#func for checking if someone vin
def victory_check(board):
    win_x = ['X','X','X']
    win_0 = ['0', '0', '0']
    board_situation = list(board.values())
    win_list = []
    win_list.append(board_situation[:3])
    win_list.append(board_situation[3:6])
    win_list.append(board_situation[6:])
    win_list.append(board_situation[:7:3])
    win_list.append(board_situation[1:8:3])
    win_list.append(board_situation[2::3])
    win_list.append(board_situation[::4])
    win_list.append(board_situation[2:7:2])
    if win_x in win_list:
        print('\nX player win!\n')
        return True
    elif win_0 in win_list:
        print('\n0 player win!\n')
        return True

#there are variables turn(it is x or 0) and titles(keys from our board)
titles = list(the_board.keys())
turn = 'X'


# our menu
print('''You can set your symbol on 9 tiles:
    1 - top-left corner
    2 - top-mid
    3 - top-right corner
    4 - mid-left corner
    5 - mid-mid 
    6 - mid-rigt corner
    7 - low-left corner
    8 - low-mid 
    9 - low-right corner''')

#main part, here board is getting full
for i in range(9):
    print_board(the_board)
    while True:
        move = check_num()
        if the_board[titles[move - 1]] == ' ':
            the_board[titles[move -1]] = turn
            break
        else:
            print('\nTitle has a symbol, please select another title\n')
    #here we start checking if someone win
    if i > 3 and i < 8:
        if victory_check(the_board):
            break
    elif i == 8:
        if victory_check(the_board):
            break
        else:
            print('\nIt`s a draw...\n')
    #chage of turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'   

#print final result of game
print_board(the_board)