import deeds

#  Record the name of player1
def player1():
    name = str(input("Player 1: Choose a player name: "))
    return name


def player2():
    name = str(input("Player 2: Choose a player name: "))
    return name


first_player = player1()
second_player = player2()
print(first_player + " roll the dice to determine who goes first")
print(first_player + " it is you turn to roll the dice to see who wins")

