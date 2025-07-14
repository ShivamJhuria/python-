import random

# Snake and Ladder positions
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

# Initial positions
player1_pos = 0
player2_pos = 0

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Game loop
while True:
    # Player 1 turn
    input("Player 1, press Enter to roll the dice.")
    dice = roll_dice()
    print("You rolled:", dice)
    if player1_pos + dice <= 100:
        player1_pos += dice
    if player1_pos in snakes:
        print("Oops! Snake bite 🐍")
        player1_pos = snakes[player1_pos]
    elif player1_pos in ladders:
        print("Yay! You got a ladder 🪜")
        player1_pos = ladders[player1_pos]
    print("Player 1 is at:", player1_pos)
    if player1_pos == 100:
        print("🎉 Player 1 wins!")
        break

    # Player 2 turn
    input("Player 2, press Enter to roll the dice.")
    dice = roll_dice()
    print("You rolled:", dice)
    if player2_pos + dice <= 100:
        player2_pos += dice
    if player2_pos in snakes:
        print("Oops! Snake bite 🐍")
        player2_pos = snakes[player2_pos]
    elif player2_pos in ladders:
        print("Yay! You got a ladder 🪜")
        player2_pos = ladders[player2_pos]
    print("Player 2 is at:", player2_pos)
    if player2_pos == 100:
        print("🎉 Player 2 wins!")
        break
