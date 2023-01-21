import random

def main():
    board = [['.' for x in range(3)] for y in range(3)]
    letter_list = ['O', 'X']
    letter = random.choice(letter_list)
    player_1, player_2 = choose_players()
    player = random.choice([player_1, player_2])
    while True:
        print("--"*35)
        print(f"{player} with the letter {letter} turn.")
        board_nums = board_numbers()
        for row in board_nums:
            print('|'.join(row))

        print("\nPlease use the above numbers to place yor letter on the board below.")

        for row in board:
            print('|'.join(row))
        print("--"*35)

        if player == 'Human': 
            choice = get_human_move(board)
        elif player == 'AI':
            choice = get_computer_move(board)

        # available, so update
        board = board_update(choice, board, letter)

        if winner(board):
            print(f'{player} player with letter {letter} WON!')
            break

        if board_has_no_moves(board):
            print('It is a DRAW')
            break

        if letter == 'O': letter = 'X'
        else: letter = 'O'
        if player == player_1: player = player_2
        else: player = player_1 
    
    for row in board:
        print('|'.join(row))
    
    next_game=(input("Do you want to play next game? (y)")).lower()
    if next_game == 'y':
        main()
    else: 
        exit()


def get_computer_move(board):
    available_moves = []
    for place in range(1,10):
        if if_place_available(place, board):
            available_moves.append(place)
    choice = random.choice(available_moves)
    return choice

def get_human_move(board):
    while True:
        try:
            choice = int(input("Please enter a number: "))
        except ValueError:
            print("It is not a number, please try again.")
            continue       
        if choice < 1 or choice > 9:
            print("Wrong number, please try again.")
            continue
        if if_place_available(choice, board):
            return choice
        else: 
            print("Place already taken, please try again")
            continue
        
def choose_players():
    print("Please choose a type of game:")
    print("1. Human vs Human.")
    print("2. Human vs AI.")
    print("3. AI vs AI")
    game_choice = input("..: ")
    if game_choice not in ['1', '2', '3']:
        print("Please choose 1, 2 or 3")
        choose_players()
    else:
        if game_choice == '1':
            player_1 = 'Human'
            player_2 = 'Human'
        elif game_choice == '2':
            player_1 = 'Human'
            player_2 = 'AI'
        elif game_choice == '3':
            player_1 = 'AI'
            player_2 = 'AI'
        return player_1, player_2

def board_has_no_moves(board):
    board_check = [place for row in board for place in row]
    if board_check.count('.') == 0:
        return True
    return False

def winner(board):
    board_check = [place for row in board for place in row]
    for x in (0,3,6):
        if board_check[x] == board_check[x+1] == board_check[x+2] and board_check[x] != '.':
            return True
    for x in (0,1,2):
        if board_check[x] == board_check[x+3] == board_check[x+6] and board_check[x] != '.':
            return True       
    if board_check[0] == board_check[4] == board_check[8] and board_check[4] != '.':
        return True 
    if board_check[2] == board_check[4] == board_check[6] and board_check[4] != '.':
        return True 
    return False     

def if_place_available(choice, board):
    board_check = [place for row in board for place in row]
    index = choice-1
    if board_check[index] == '.':
        return True
    return False

def board_update(choice, board, letter):
    board_check = [place for row in board for place in row]
    index = choice-1
    board_check[index] = letter
    board = [[board_check[y] for y in range(x*3,(x*3)+3)] for x in range(3)]
    return board

    # board = []
    # for x in range(3):
    #     board.append([])
    #     for y in range(x*3,(x*3)+3):
    #         board[x].append(board_check[y])


def board_numbers():
    return [['1','2','3'], ['4','5','6'], ['7','8','9']]

if __name__ == '__main__':
    main()