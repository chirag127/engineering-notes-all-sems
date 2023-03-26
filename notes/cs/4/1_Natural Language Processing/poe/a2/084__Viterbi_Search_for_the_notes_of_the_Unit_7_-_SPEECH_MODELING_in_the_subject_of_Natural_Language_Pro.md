 Here is the content in Markdown format without any emojis or external links:

### Viterbi Search
- Viterbi search is used to find the most likely sequence of hidden states.
- It is applied on Hidden Markov Models(HMMs) to solve the decoding problem.
- The steps are:
1. Initialize the Viterbi matrix and backpointer array with the initial probabilities and 0 backpointers respectively.
2. For each time step/observation:
    - Calculate the state transition probabilities and observation probabilities to get the joint probabilities for all states.
    - Update the Viterbi matrix with the max joint probability for each state (taking the max over the previous time step/state joint probabilities).
    - Update the backpointer array to store the previous state that gave the max joint probability.
3. The most likely sequence of states is found by traversing back from the final time step state that has the maximum probability in the Viterbi matrix. The backpointers are used to traverse back.
- This gives the optimal state sequence that is most likely to have generated the given observation sequence.
- Used in Speech Recognition and Pos Tagging tasks. Avoids the exponential growth of possible sequences that is faced in naive approaches.

The above content is written in a formal tone with points and without any emojis or external links as specified. The headers and formatting is done using Markdown syntax. Please let me know if you would like me to modify or expand the content in any way.