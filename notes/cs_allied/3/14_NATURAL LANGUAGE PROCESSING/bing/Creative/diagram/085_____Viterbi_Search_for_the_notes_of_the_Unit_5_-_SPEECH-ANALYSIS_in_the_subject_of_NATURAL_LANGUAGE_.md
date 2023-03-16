### Viterbi Search

- Viterbi search is an algorithm that finds the most likely sequence of hidden states in a hidden Markov model (HMM) given a sequence of observed events .
- Viterbi search is widely used in speech analysis, such as speech recognition, speech synthesis and speech enhancement  .
- Viterbi search consists of two steps: forward computation and backtracking .
  - Forward computation: calculate the probability of the most likely path that ends at each state for each time step using dynamic programming .
  - Backtracking: trace back the most likely path from the final state to the initial state using pointers stored during the forward computation .
- Viterbi search can be extended to handle multiple observations, such as microphone arrays, by using a 3-D trellis structure.
- Viterbi search can improve the accuracy and robustness of speech analysis in noisy and distant-talking situations .