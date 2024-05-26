import random
rock = "Rock"
pepper = "Pepper"
scissor = "Scissor"
computer_move = ""

player_move = input("Choose [r]ock, [p]epper or [s]cissor: ")
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = pepper
elif player_move == "s":
    player_move = scissor
else:
    raise SystemExit("Invalid input.Try again...!")
computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = pepper
elif computer_random_number == 3:
    computer_move = scissor
if (player_move == rock and computer_move == scissor) or \
        (player_move == pepper and computer_move == rock) or \
        (player_move == scissor and computer_move == pepper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")
