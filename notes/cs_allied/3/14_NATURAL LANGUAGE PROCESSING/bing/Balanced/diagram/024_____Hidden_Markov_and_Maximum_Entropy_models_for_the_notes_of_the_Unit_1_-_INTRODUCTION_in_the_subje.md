### Hidden Markov and Maximum Entropy models

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions).
- HMM assumes that the hidden states follow a Markov chain, meaning that the current state depends only on the previous state, and the emissions depend only on the current state.
- HMM can be used for natural language processing tasks such as part-of-speech tagging, speech recognition, named entity recognition, etc.
- HMM can be represented by a 5-tuple: (Q, V, A, B, π), where Q is the set of hidden states, V is the set of emissions, A is the state transition matrix, B is the emission matrix, and π is the initial state distribution.
- HMM can be trained using the Baum-Welch algorithm, which is a special case of the Expectation-Maximization algorithm, to estimate the parameters A, B, and π from a set of observed sequences.
- HMM can be used for decoding, which is finding the most likely sequence of hidden states given a sequence of emissions, using the Viterbi algorithm, which is a dynamic programming algorithm that exploits the Markov property of the hidden states.
- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learnt are connected in a Markov chain rather than being conditionally independent of each other.
- MEMM can be used for natural language processing tasks such as part-of-speech tagging and information extraction, where the goal is to assign a label to each word or token in a sentence or document.
- MEMM can be represented by a conditional probability distribution P(y|x), where y is the label sequence and x is the input sequence, and the probability of each label depends on the previous label and the input features.
- MEMM can be trained using the Generalized Iterative Scaling algorithm, which is a gradient-based algorithm that maximizes the conditional likelihood of the training data, subject to a set of constraints that ensure the model is consistent with the empirical distribution of the features.
- MEMM can be used for decoding, which is finding the most likely label sequence given an input sequence, using the Viterbi algorithm, which is modified to account for the conditional nature of the model.