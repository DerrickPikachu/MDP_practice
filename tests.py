from agent import MDP
from game import Game
from random import randint

def testGame():
    coinGame = Game(0.5)

    print('initial status:')
    print('player money = {}'.format(coinGame.showState()))
    print('------------------------')
    print('game start')

    while not coinGame.gameOver:
        stackCoin = randint(0, coinGame.showState())
        coinGame.stack(stackCoin)
        result = coinGame.flipCoin()
        print('stack {} coins'.format(stackCoin))
        print('result: {}'.format(result))
        print('new state: {}'.format(coinGame.showState()))
        print('------------------------')

    print('game over!')
    print('reward: {}'.format(coinGame.reward))


def testMDP():
    mdp = MDP(0.40)
    mdp.valueIteration()


if __name__ == "__main__":
    testMDP()
