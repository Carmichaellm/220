"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""


def build_board():
    coords = [1,2,3,4,5,6,7,8,9]


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if not ((board[position] == 'x') or (board[position] == 'o')):
        return True
    return False


def fill_spot(board, position, character):
    character = character.strip()
    character = character.lower()
    board[position] = character


def winning_game(board, shape):
    if board[0] == shape and board[1] == shape and board[2] == shape:
        return True
    if board[0] == shape and board[4] == shape and board[8] == shape:
        return True
    if board[0] == shape and board[3] == shape and board[6] == shape:
        return True
    if board[1] == shape and board[4] == shape and board[7] == shape:
        return True
    if board[2] == shape and board[4] == shape and board[6] == shape:
        return True
    if board[2] == shape and board[5] == shape and board[8] == shape:
        return True
    if board[3] == shape and board[4] == shape and board[5] == shape:
        return True
    if board[6] == shape and board[7] == shape and board[8] == shape:
        return True
    return False


def game_over(board):
    for i in range(len(board)):
        if type(board[i]) == type(0):
            return False
    return True


def get_winner(board):
    winner = ''
    if winning_game(board, 'x'):
        winner = 'x'
        return winner
    if winning_game(board,'o'):
        winner = 'o'
        return winner
    return None


def play(board):
    end = False
    while not end:
        print_board(board)
        xmoved = False
        while xmoved == False:
            position = eval(input("x's choose a position: "))
            if is_legal(board, position):
                fill_spot(board,position,'x')
                xmoved = True
        omoved = False
        while omoved == False:
            position = eval(input("o's choose a position: "))
            if is_legal(board, position):
                fill_spot(board, position, 'o')
                omoved = True
        winner = get_winner(board)
        if winning_game(board, winner):
            print("{}'s win!".format(winner))
            end = True
        if game_over(board):
            end = True




def main():
    ans = 'y'
    while ans[0] == 'y':
        board = build_board()
        play(board)
        ans = input('play again?')


if __name__ == '__main__':
    main()
