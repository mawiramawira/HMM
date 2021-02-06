import numpy as np

class MarkovChain():
    def __init__(self,transition_matrix,states):
        self.transition_matrix = np.atleast_2d(transition_matrix)
        self.states = states
        self.index_dict = {self.states[index] :
            index for index in range(len(self.states))}
        self.state_dict = {index: self.states[index]
            for index in range(len(self.states))}
        print(self.transition_matrix, self.index_dict, self.state_dict, sep = '\n')

    def next_state(self, current_state):
        probs = self.transition_matrix[self.index_dict[current_state],:]
        #print(self.states,probs)
        return np.random.choice(self.states,p = probs)
            

    def generate_states(self, current_state, no = 10):
        future_states = []

        for i in range(no):
            next_state = self.next_state(current_state)
            future_states.append(next_state)
            current_state = next_state

        return future_states


transition_matrix = [
    [0.8,0.19,0.01],
    [0.1,0.2, 0.7],
    [0.2,0.7, 0.1]
]

weather_chain = MarkovChain(transition_matrix = transition_matrix, states = ['Sunny', 'Snowy', 'Rainy'])
next_states = weather_chain.generate_states(current_state = 'Sunny')
print(next_states)