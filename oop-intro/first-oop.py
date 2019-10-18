#!/usr/bin/env python3

from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []

    def get_dice(self):
        return self.dice





player1 = Player()
player2 = Player()

player1.roll()
player2.roll()

print(f"Player 1 rolled {str(player1.get_dice())}")
print(f"Player 2 rolled {str(player2.get_dice())}")


if sum (player1.get_dice()) == sum(player2.get_dice()):
    print("Draw")

elif sum(player1.get_dice()) > sum(player2.get_dice()):
    print("PLayer 1 wins")

else:
    print("player 2 wins")
