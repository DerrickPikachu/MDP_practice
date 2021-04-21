from game import Game
from random import randint

if __name__ == "__main__":
    coinGame = Game(0.5)

    print('initial status:')
    print('player money = {}'.format(coinGame.showState()))
    print('------------------------')
    print('game start')

    while not coinGame.gameOver:
        stackCoin = randint(0, coinGame.showState())
        coinGame.stack(stackCoin)
        reward = coinGame.flipCoin()
        print('stack {} coins'.format(stackCoin))
        print('reward: {}'.format(reward))
        print('new state: {}'.format(coinGame.showState()))
        print('------------------------')

    print('game over!')
