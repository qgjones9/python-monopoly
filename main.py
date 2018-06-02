from deeds import deeds

'''
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

'''

spice_mines = deeds('SPICE MINES', 28, 56, 150, 450, 100, 1200, 1400, 200, 200, 160, 176)
landing_platform = deeds('LANDING PLATFORM', 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165)
operations_center = deeds('OPERATIONS CENTER', 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165)

print('=============================================')
spice_mines.deed_details()
print('=============================================')
landing_platform.deed_details()
print('=============================================')
operations_center.deed_details()

