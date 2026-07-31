 Here is the content in markdown format without any emojis or external links and in formal tone:

### Viterbi Search

- Viterbi search is a dynamic programming algorithm for finding the most likely sequence of hidden states.
- It is used in Hidden Markov Models(HMMs) to predict the most probable sequence of states that results in a given sequence of observations.
- The steps involved in Viterbi search are:

1. Initialize the Viterbi path and Viterbi probability:
- Set the initial Viterbi probability for each state at t=1 to be the emission probability of the observation at t=1 and the initial state.
- Set the initial Viterbi path for each state to be a start state with probability 1.

2. Recursion: For t = 2 to T
- For each state, compute the Viterbi probability by taking the maximum of the previous Viterbi probability multiplied by the transition probability from the previous state to the current state and the emission probability of the current observation.
- Also, store the previous state that maximizes this probability as the Viterbi path for the current state.

3. Termination: After the recursion, the state corresponding to the maximum final Viterbi probability is the predicted state sequence. The predicted state sequence can be retrieved by following the Viterbi path backwards.

- The time complexity of Viterbi search is O(NK^2) where N is the length of the observation sequence and K is the number of states.
- Viterbi search is optimal as it finds the most likely state sequence. However, it only gives the single best path and discards other probable paths.