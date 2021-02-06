[] Exploring Hidden Markov Models
    [X] Keys
        [f] function
        [a] arguments 
    [X] Definition of Markov chain
        [X] Almost like a drunk person walking on a road
        [X] Discrete state space
        [X] Probability distribution is equal 
        [X] Current state only depends on previous state
    [X] Implementation
        [X] Start with dictionary implementation
            [X] init(f)
                [X] transition_prob_dict(a)
            [X] next_state(f)
                [X] current_state(a)
            [X] generate_state(f)
                [X] current_state(a)
                [X] no of steps forward(a)
        [X] Change it to matrix implementation
            [X] init(f)
                [X] transition_matrix(a)
                [X] states(a)
            [X] next_state(f)
                [X] current_state(a)
            [X] generate_state(f)
                [X] current_state(a)
                [X] no of steps forward(a)
    [X] Properties of Markov Chains
        [X] Irreducibility
            [X] All states are connected
        [X] Periodicity
            [X] State i is said to have period k if any possible
                path to return to state i would be a multiple of k steps
            [X] k is the GCD of the number of steps of all possible
                paths from state i to itself
            [X] Undefined if no path back
            [X] Aperiodic if k = 1
        [X] Transience and recurrence
            [X] Transient if
                [X] There is a non-zero probability that we will never 
                    return to state i
            [X] Recurrence
                [X] Probability of returning to state i after n steps 
                [X] Mean recurrence/ hitting time
                    [X] Expected time to return to state i
                    [X] If finite, 'positive recurrent', else 'null recurrent'
                [X] Expected number of visits
                [X] Absorbing states
                    [X] Impossible to leave once you enter the state
        [X] Ergodicity
            [X] If recurrent, has a period 1 and a finite mean recurrence time
            [X] If there is a number N, such that any state in the system
                can be reached from any other state in any number of states 
                greater than or equal to the number N
            [X] Fulfilled in a fully connected matrix where all transutuinns have 
                a non-zero probability
    [X] Steady state analysis and limiting distributions
        [X] Stationary if probability distributions remain unchanged 
