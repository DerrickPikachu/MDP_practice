# My agent use MDP to learn to play the game define in game.py
# I will use Value Iteration to learn the best policy,
# reward is returned when the game is finished.
import matplotlib.pyplot as plt


class MDP:
    def __init__(self, prob):
        self.headProb = prob
        self.coinLimit = 100
        self.value = [.0] * (self.coinLimit + 1)
        self.policy = [0] * (self.coinLimit + 1)
        self.value[100] = 1
        self.terminateCondition = 1e-30

    def __evaluate(self, state, stacked):
        # (1-prob)*stateLose + prob*stateWin
        if state + stacked > self.coinLimit:
            return 0
        return (1 - self.headProb) * self.value[state - stacked] + self.headProb * self.value[state + stacked]

    def valueIteration(self):
        delta = -1
        xlabel = range(self.coinLimit + 1)
        _, ax = plt.subplots()
        iteration = 1

        # Agent learn the value function
        while delta == -1 or delta > self.terminateCondition:
            delta = 0
            print('iteration: {}'.format(iteration))
            for i in range(1, self.coinLimit):
                state = i
                bestValue = 0
                for j in range(1, min(state + 1, self.coinLimit - state + 1)):
                    evaluateVal = self.__evaluate(state, j)
                    bestValue = max(bestValue, evaluateVal)
                delta = max(delta, abs(self.value[i] - bestValue))
                self.value[i] = bestValue
            ax.plot(xlabel, self.value, label=str(iteration))
            iteration += 1
            print('delta = {}'.format(delta))
            print('------------------')

        ax.legend()
        plt.show()

        # Find the best policy
        for i in range(1, self.coinLimit):
            state = i
            bestValue = 0
            for j in range(1, min(state + 1, self.coinLimit - state + 1)):
                evaluateVal = self.__evaluate(state, j)
                if bestValue < evaluateVal:
                    bestValue = evaluateVal
                    self.policy[i] = j

        _, ax = plt.subplots()
        ax.plot(xlabel, self.policy)
        ax.legend()
        plt.show()

    def getAction(self, state):
        return self.policy[state]
