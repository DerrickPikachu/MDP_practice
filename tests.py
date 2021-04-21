from game import Game
import matplotlib.pyplot as plt

if __name__ == "__main__":
    labels = ['True', 'False']
    widths = 0.4
    counter = [0, 0]

    coin = Game(0.8)
    for i in range(1000):
        if coin.flipCoin():
            counter[0] += 1
        else:
            counter[1] += 1

    _, ax = plt.subplots()
    ax.bar(labels, counter, widths)
    ax.set_ylabel('Amount')
    ax.set_title('Probability distribution')
    ax.legend()

    plt.show()
