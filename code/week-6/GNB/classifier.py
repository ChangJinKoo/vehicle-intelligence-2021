import numpy as np
import random
from math import sqrt, pi, exp

def gaussian_prob(obs, mu, sig):
    # Calculate Gaussian probability given
    # - observation
    # - mean
    # - standard deviation
    num = (obs - mu) ** 2
    denum = 2 * sig ** 2
    norm = 1 / sqrt(2 * pi * sig ** 2)
    return norm * exp(-num / denum)

# Gaussian Naive Bayes class
class GNB():
    # Initialize classification categories
    def __init__(self):
        self.classes = ['left', 'keep', 'right']

    # Given a set of variables, preprocess them for feature engineering.
    def process_vars(self, vars):
        # The following implementation simply extracts the four raw values
        # given by the input data, i.e. s, d, s_dot, and d_dot.
        s, d, s_dot, d_dot = vars
        return s, d, s_dot, d_dot

    # Train the GNB using a combination of X and Y, where
    # X denotes the observations (here we have four variables for each) and
    # Y denotes the corresponding labels ("left", "keep", "right").
    def train(self, X, Y):
        '''
        Collect the data and calculate mean and standard variation
        for each class. Record them for later use in prediction.
        '''
        # TODO: implement code.
        
        temp = {}
        self.dataset = {}
        
        for i, c in enumerate(Y):
            if c not in temp:
                temp[c] = []
                self.dataset[c] = {}
            temp[c].append(X[i])

        self.dataset = {label:{} for label in self.classes}
        
        for label in self.dataset:
            self.dataset[label]['mean'] = np.mean(temp[label], axis = 0)
            self.dataset[label]['std'] = np.std(temp[label], axis = 0)


    # Given an observation (s, s_dot, d, d_dot), predict which behaviour
    # the vehicle is going to take using GNB.
    def predict(self, observation):
        '''
        Calculate Gaussian probability for each variable based on the
        mean and standard deviation calculated in the training process.
        Multiply all the probabilities for variables, and then
        normalize them to get conditional probabilities.
        Return the label for the highest conditional probability.
        '''
        # TODO: implement code.
        
        probs = []

        for label in self.dataset : 
            prob = 1

            for i in range(len(observation)) : 
                prob *= gaussian_prob(observation[i],\
                        self.dataset[label]['mean'][i],\
                        self.dataset[label]['std'][i])

            probs.append(prob)

        return list(self.dataset.keys())[np.argmax(probs)] 
