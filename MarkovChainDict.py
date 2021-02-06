import numpy as np

class MarkovChain():
    def __init__(self,transition_prob):
        self.transition_prob = transition_prob
        self.states = list(transition_prob.keys())

    def next_state(self, current_state):
        probs = [self.transition_prob[current_state][next_state] 
            for next_state in self.states]
        #print(self.states,probs)
        return np.random.choice(self.states,p = probs)
            

    def generate_states(self, current_state, no = 1):
        future_states = []

        for i in range(no):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state

        return future_states


transition_prob = {
    'Sunny' : {'Sunny' : 0.8, 'Rainy' : 0.19, 'Snowy' : 0.01},
    'Snowy' : {'Sunny' : 0.1, 'Rainy' : 0.2, 'Snowy' : 0.7},
    'Rainy' : {'Sunny' : 0.2, 'Rainy' : 0.7, 'Snowy' : 0.1}
}

weather_chain = MarkovChain(transition_prob = transition_prob)
next_state = weather_chain.next_state(current_state = 'Sunny')
print(next_state)