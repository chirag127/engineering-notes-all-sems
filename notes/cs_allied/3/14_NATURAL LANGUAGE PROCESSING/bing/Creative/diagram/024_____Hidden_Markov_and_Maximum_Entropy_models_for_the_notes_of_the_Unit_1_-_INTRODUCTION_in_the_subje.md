### Hidden Markov and Maximum Entropy models

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions) .
- HMM assumes that the hidden states follow a Markov chain, meaning that the current state depends only on the previous state .
- HMM can be represented by a 5-tuple: (S, V, A, B, π), where S is the set of hidden states, V is the set of emissions, A is the state transition matrix, B is the emission probability matrix, and π is the initial state distribution .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, speech recognition, named entity recognition, and machine translation  .
- The main problems that HMM can solve are: evaluation, decoding, and learning .
  - Evaluation: given an HMM and an observed sequence, compute the probability of the sequence given the model.
  - Decoding: given an HMM and an observed sequence, find the most likely hidden state sequence that generated the observed sequence.
  - Learning: given an observed sequence (or a set of sequences), find the optimal parameters of the HMM that maximize the likelihood of the data.
- The main algorithms that HMM can use are: forward, backward, Viterbi, and Baum-Welch .
  - Forward: a dynamic programming algorithm that computes the probability of an observed prefix given the current state.
  - Backward: a dynamic programming algorithm that computes the probability of an observed suffix given the current state.
  - Viterbi: a dynamic programming algorithm that finds the most likely hidden state sequence given an observed sequence and an HMM.
  - Baum-Welch: an expectation-maximization algorithm that iteratively estimates the parameters of the HMM given a set of observed sequences.

- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learnt are connected in a Markov chain rather than being conditionally independent of each other .
- MEMM is a conditional model that directly models the probability of a hidden state given an observed state and the previous hidden state, without modeling the joint distribution of the hidden and observed states .
- MEMM can be represented by a set of feature functions and a set of weights, where each feature function maps a hidden state, an observed state, and a previous hidden state to a real value, and each weight reflects the importance of the corresponding feature .
- MEMM can be used for natural language processing tasks, such as part-of-speech tagging and information extraction  .
- The main problem that MEMM can solve is: decoding, which is finding the most likely hidden state sequence given an observed sequence and an MEMM .
- The main algorithm that MEMM can use is: entropic forward-backward, which is a variant of the Viterbi algorithm that incorporates the entropy of the hidden state distribution at each step .