#!/usr/bin/env python3
import numpy as np
'''

Problem State:
 Boxes : red ( 3 apple, 4 orange, 3 limes),
         green ( 3 apple, 3 orange, 4 limes),
         blue ( 1 apple, 1 orange, 0 limes)

 prob. : p(r) = 0.2, p(g) = 0.6, p(b) = 0.2

 piece of fruit is removed (same prob of selecting any of the items in the box)

 (a) What is the prob of selecting an apple?
 (b) If we observe that the selected fruit is in fact an orange,
     what is the probability that it came from the green box?

'''

class Question2():
    def __init__(self):
        self.prob = {}
        self.box = {}
        self.prob['red'] = 0.2 # Red Prob.
        self.prob['green'] = 0.6 # Green Prob
        self.prob['blue'] = 0.2 # Blue Prob
        self.box['red'] = {'apple': 3, 'orange':4, 'lime':3}
        self.box['green'] = {'apple': 3, 'orange':3, 'lime':4}
        self.box['blue'] = {'apple': 1, 'orange':1, 'lime':0}

    def cal_prob(self, fruits):
        # From Red
        self.prob_from_red = self.prob['red'] * (self.box['red'][fruits] / sum(self.box['red'].values()))
        # From Green
        self.prob_from_green = self.prob['green'] * (self.box['green'][fruits] / sum(self.box['green'].values()))
        # From Blue
        self.prob_from_blue = self.prob['blue'] * (self.box['blue'][fruits] / sum(self.box['blue'].values()))
        total_prob = self.prob_from_red + self.prob_from_blue + self.prob_from_green
        return total_prob
    def cal_posterior_prob(self, obs_fruits, results_box):
        '''
            Using P(A|B) = P(B|A)P(A)
        '''
        #TODO(1) : P(B|A) : Prob. select observed fruits from results Box
        self.prob_obs_from_results = self.prob[results_box] * (self.box[results_box][obs_fruits] / sum(self.box[results_box].values()))

        #TODO(2) : P(A) : Prob. Select Green Box
        self.prob_results_box = self.prob[results_box]
        #TODO(3) : P(B) : Prob. Select Orange
        self.prob_obs_fruits = self.cal_prob('orange')
        #TODO(4) : P(A|B) :
        self.results_prob = self.prob_obs_from_results*self.prob_results_box/self.prob_obs_fruits
        return self.results_prob

    def run(self):
        #TODO(4): (a) Selecting Apple
        apple_prob = self.cal_prob('apple')
        print(f'The probability of Selecting apple is {apple_prob*100}%')
        obs_orange_from_green = self.cal_posterior_prob('orange', 'green')
        print(f"The probability that observed orange came from green box is: {obs_orange_from_green*100}%")

if __name__ == '__main__':
    run = Question2()
    run.run()
