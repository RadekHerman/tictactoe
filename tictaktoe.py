import random
import os

def main():
    board = [["." for x in range(3)] for y in range(3)]
    letter = random.choice(["O", "X"])
    player_1, player_2 = choose_players()
    player = random.choice([player_1, player_2])

    while True:
        print("--" * 35)
        print(f"{player} Player with the letter {letter} turn.")
        board_nums = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        for row in board_nums:
            print("|".join(row))

        print(
            f"\nPlease use the above numbers to place your >> {letter} << on the board below."
        )

        for row in board:
            print("|".join(row))
        print("--" * 35)

        if player == "Human":
            choice = get_human_move(board)
        elif player == "Random":
            choice = get_random_move(board)
        elif player == "AI":
            if letter == "O":
                choice = get_ai_move(board, "O", "X", True)
            else:
                choice = get_ai_move(board, "X", "O", True)

        board = board_update(choice, board, letter)

        if winner(board, letter):
            print(f"{player} Player with letter {letter} WINS!")
            break

        if board_has_no_moves(board):
            print("It is a DRAW")
            break

        if letter == "O":
            letter = "X"
        else:
            letter = "O"
        if player == player_1:
            player = player_2
        else:
            player = player_1

    for row in board:
        print("|".join(row))

    next_game = (input("Do you want to play next game (y)? ")).lower()
    if next_game == "y":
        main()
    else:
        exit()


def minimax(board, letter, opponent_letter, max_player):

    if winner(board, letter):
        return 1
    if winner(board, opponent_letter):
        return -1
    elif board_has_no_moves(board):
        return 0

    if max_player:
        max_evaluation = -1000
        for place in range(1, 10):
            if if_place_available(place, board):
                board = board_update(place, board, letter)
                current_evaluation = minimax(board, letter, opponent_letter, False)
                max_evaluation = max(max_evaluation, current_evaluation)
                board = board_update(place, board, ".")
        return max_evaluation

    else:
        min_evaluation = 1000
        for place in range(1, 10):
            if if_place_available(place, board):
                board = board_update(place, board, opponent_letter)
                current_evaluation = minimax(board, letter, opponent_letter, True)
                min_evaluation = min(min_evaluation, current_evaluation)
                board = board_update(place, board, ".")
        return min_evaluation


# one function for both players 'O', 'X'
# this implementation of ai move and minimax
# forced by random choice of letters and players at the beginning of the game
def get_ai_move(board, letter, opponent_letter, max_player):
    best_score = -1000 if max_player else 1000
    for place in range(1, 10):
        if if_place_available(place, board):
            board = board_update(place, board, letter)
            score = minimax(board, letter, opponent_letter, False)
            board = board_update(place, board, ".")
            if max_player:
                if score > best_score:
                    best_score = score
                    best_choice = place
            else:
                if score < best_score:
                    best_score = score
                    best_choice = place
    return best_choice


def get_random_move(board):
    available_moves = []
    for place in range(1, 10):
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
    os.system('clear')
    print("Please choose a type of game:")
    print("The player who starts the game and they letter will be chosen in random.")
    print("1. Human vs Human")
    print("2. Human vs Random Computer")
    print("3. Human vs AI")
    print("4. AI vs AI")
    print("5. Random Computer vs AI")
    print("6. Random Computer vs Random Computer")
    game_choice = input("..: ")
    if game_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Please choose 1, 2, 3, 4, 5, 6")
        choose_players()
    else:
        if game_choice == "1":
            player_1 = "Human"
            player_2 = "Human"
        elif game_choice == "2":
            player_1 = "Human"
            player_2 = "Random"
        elif game_choice == "3":
            player_1 = "Human"
            player_2 = "AI"
        elif game_choice == "4":
            player_1 = "AI"
            player_2 = "AI"
        elif game_choice == "5":
            player_1 = "Random"
            player_2 = "AI"
        elif game_choice == "6":
            player_1 = "Random"
            player_2 = "Random"
        return player_1, player_2


def board_has_no_moves(board):
    board_check = [place for row in board for place in row]
    if board_check.count(".") == 0:
        return True
    return False


def winner(board, player):
    board_check = [place for row in board for place in row]
    for x in (0, 3, 6):
        if (
            board_check[x] == board_check[x + 1] == board_check[x + 2]
            and board_check[x] == player
        ):
            return True
    for x in (0, 1, 2):
        if (
            board_check[x] == board_check[x + 3] == board_check[x + 6]
            and board_check[x] == player
        ):
            return True
    if board_check[0] == board_check[4] == board_check[8] and board_check[4] == player:
        return True
    if board_check[2] == board_check[4] == board_check[6] and board_check[4] == player:
        return True
    return False


def if_place_available(choice, board):
    board_check = [place for row in board for place in row]
    index = choice - 1
    if board_check[index] == ".":
        return True
    return False


def board_update(choice, board, player):
    board_check = [place for row in board for place in row]
    index = choice - 1
    board_check[index] = player
    board = [[board_check[y] for y in range(x * 3, (x * 3) + 3)] for x in range(3)]
    return board


if __name__ == "__main__":
    main()
