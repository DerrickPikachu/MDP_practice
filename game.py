# This script is to implement the game which I want to practice MDP
# The game is about a easy flip coin problem:
# The game always start with flip a coin.
# If it comes up heads, we get all the money we stacked on that flip
# Otherwise, we lose all the money we stack on that flip
from random import random, randint


class Game:
    def __init__(self, userProb: float):
        self.headProb = userProb
        self.playerMoney = randint(10, 40)
        self.stackedMoney = 0
        self.gameOver = False
        self.reward = 0

    def flipCoin(self) -> bool:
        if self.gameOver:
            print('Game has been stopped')
        shoot = random()
        isWin = True if shoot <= self.headProb else False

        # Check is head or not, and setup the reward.
        # The reward is according to the winning money of this play
        if isWin:
            self.playerMoney += self.stackedMoney
        else:
            self.playerMoney -= self.stackedMoney

        # Check the game over condition
        if self.playerMoney >= 100 or self.playerMoney == 0:
            self.gameOver = True
            if self.playerMoney == 0:
                self.reward = -1
            else:
                self.reward = 1

        # Reset the staked money, prepare for next play
        self.stackedMoney = 0
        return isWin

    # Please always setup stack function before flipping coin
    def stack(self, money):
        # Check for validation
        if money > self.playerMoney:
            print('stack too much money!!')
        else:
            self.stackedMoney = money

    def showState(self) -> int:
        return self.playerMoney
