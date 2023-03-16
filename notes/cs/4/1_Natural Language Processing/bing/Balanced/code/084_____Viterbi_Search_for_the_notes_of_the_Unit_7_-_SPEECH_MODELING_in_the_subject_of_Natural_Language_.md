```markdown
### Viterbi Search for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Viterbi search is a dynamic programming algorithm that finds the most likely sequence of hidden states in a hidden Markov model (HMM) that generates a given sequence of observations.
- Viterbi search is widely used in speech recognition, speech enhancement, and part-of-speech tagging, among other applications  .
- Viterbi search consists of the following steps:
  - Initialize a state list with one cell for each state in the HMM, and assign the initial probabilities to the initial states for time t = 0.
  - For each time step t from 1 to T, where T is the length of the observation sequence:
    - Clear the state list for time t.
    - For each state s in the HMM, compute the maximum probability of reaching s at time t, and the previous state that leads to this maximum probability, using the transition probabilities, the emission probabilities, and the state list for time t-1.
    - Update the state list for time t with the computed values and pointers.
  - Trace back the pointers from the state list for time T to find the most likely state sequence, called the Viterbi path.
- Viterbi search can be illustrated using a trellis diagram, where each column represents a time step, each row represents a state, and each cell contains the probability and pointer for that state at that time.
- Viterbi search can be extended to handle multiple observation streams, such as speech signals from different talker directions, by using a 3-dimensional trellis space composed of talker directions, input frames, and HMM states.
```