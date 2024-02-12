def computer_move(n, m):
    return min(n, m) if n <= m else n % (m + 1) or m

def user_move(n, m):
    pieces = int(input('How many pieces will you remove? '))
    while not (0 < pieces <= m) or pieces > n:
        print("Oops! Invalid move! Try again.")
        pieces = int(input("\nHow many pieces will you remove? "))
    return pieces

def game():
    n = int(input('Enter the total number of pieces: '))
    m = int(input('Enter the maximum number of pieces per move: '))
    while m < 1:
        print('The number of pieces per move must be less than or equal to the total pieces')
        m = int(input('Enter the maximum number of pieces per move: '))
    pieces = 0
    turn = 0
    if n % (m + 1) == 0:
        print('You start!')
        turn = True
        while n > 0:
            player = "You" if turn else "The computer"
            pieces = user_move(n, m) if turn else computer_move(n, m)
            print(f"{player} removed {pieces}")
            n -= pieces
            print(f"There are {n} pieces left")
            turn = not turn  
        winner = 2 if turn else 1
        print(f"Game over! The {'computer' if winner == 2 else 'you'} won!\n")
        return winner
    else:
        print("Computer starts!")
        turn = 2 
        while n > 0:
            player = "The computer" if turn == 2 else "You"
            pieces = computer_move(n, m) if turn == 2 else user_move(n, m)
            print(f"{player} removed {pieces}")
            n -= pieces
            print(f"There are {n} pieces left")
            turn = 1 if turn == 2 else 2
        winner = 2 if turn == 1 else 1
        print(f"Game over! The {'computer' if winner == 2 else 'you'} won!")
        return winner
    
def tournament():
    rounds = 1
    computer_score = user_score = 0
    for rounds in range(1, 4):
        print("Round", rounds)
        if game() == 1:
            user_score += 1
        else:
            computer_score += 1
    print("Tournament over!")
    print("Score: You", user_score, "X", computer_score, "Computer")
    
def main():
    print("Welcome to the NIM game!")
    print("1 - to play a single game")
    print("2 - to play a tournament")
    choice = get_choice()
    options = {
        1: ("You chose a single game!", game),
        2: ("You chose a tournament!", tournament)
    }
    if choice in options:
        message, function = options[choice]
        print(message)
        function()
    else:
        print("Invalid option. The game will be terminated.")

def get_choice():
    while True:
        try:
            choice = int(input("Choice: "))
            if choice in [1, 2]:
                return choice
            else:
                print("Choose a valid option!")
                continue 
        except ValueError:
            print("Please, enter a valid number.")
main()

