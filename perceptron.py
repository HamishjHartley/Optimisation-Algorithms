import numpy as np
import math


class Perceptron():
    def __init__(self, n_inputs, learning_rate =0.1):
        #initializing the input weights, sampled from a Gaussian distribution
        self.weight = np.random.randn(n_inputs +1)/np.sqrt(n_inputs)
        #Initialising the learning rate
        self.learning_rate = learning_rate

    def sigmoid(x:int):
        return 1 / (1+math.exp(-x))