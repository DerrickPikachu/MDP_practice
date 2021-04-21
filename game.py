# This script is to implement the game which I want to practice MDP
# The game is about a easy flip coin problem:
# The game always start with flip a coin.
# If it comes up heads, we get all the money we stacked on that flip
# Otherwise, we lose all the money we stack on that flip
from random import random


class Game:
    def __init__(self, userProb: float) -> object:
        self.headProb = userProb

    def flipCoin(self) -> bool:
        shoot = random()
        return True if shoot <= self.headProb else False
