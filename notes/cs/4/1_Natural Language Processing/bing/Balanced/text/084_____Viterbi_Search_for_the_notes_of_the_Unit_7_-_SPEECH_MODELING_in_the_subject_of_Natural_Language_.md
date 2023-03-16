### Viterbi Search for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Viterbi search is a dynamic programming algorithm that finds the most likely sequence of hidden states in a hidden Markov model (HMM) that generates a given sequence of observations.
- Viterbi search is widely used in speech recognition to find the most likely sequence of phonemes or words that corresponds to a given speech signal.
- Viterbi search consists of the following steps:
  - Initialize a state list with one cell for each state in the HMM and assign the initial probabilities to the starting states.
  - For each observation in the sequence, compute the transition probabilities from the previous states to the current states and multiply them by the emission probabilities of the observation given the current states. This gives the joint probabilities of the observation and the current states.
  - For each current state, select the previous state that has the highest joint probability and store it as the back pointer. Also, store the maximum joint probability as the new state probability.
  - Repeat steps 2 and 3 until all observations are processed.
  - Trace back the pointers from the final state with the highest probability to the initial state and obtain the most likely sequence of hidden states.
- Viterbi search can be extended to handle multiple sources of observations, such as speech signals from different directions or microphones, by using a 3-dimensional trellis space composed of source directions, input frames, and HMM states.
- Viterbi search can also be applied to other natural language processing tasks, such as part-of-speech tagging, where the hidden states are the tags and the observations are the words.