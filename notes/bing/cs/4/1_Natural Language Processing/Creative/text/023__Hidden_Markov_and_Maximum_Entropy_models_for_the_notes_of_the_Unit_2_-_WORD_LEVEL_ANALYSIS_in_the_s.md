### Hidden Markov and Maximum Entropy models for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions) .
- HMM assumes that the hidden states follow a Markov chain, which means that the current state depends only on the previous state, and the emissions depend only on the current state .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, named entity recognition, speech recognition, and text segmentation  .
- HMM can be trained using the Viterbi algorithm, which finds the most likely sequence of hidden states given the observed sequence, or the Baum-Welch algorithm, which uses the expectation-maximization technique to estimate the model parameters  .
- Maximum Entropy Markov Model (MEMM) is a variant of HMM that uses a maximum entropy classifier to model the conditional probability of each hidden state given the previous state and the current observation .
- MEMM overcomes the limitation of HMM that it cannot incorporate arbitrary features of the observations, such as word shape, capitalization, suffix, etc. .
- MEMM can also be used for natural language processing tasks, such as part-of-speech tagging, named entity recognition, and text segmentation  .
- MEMM can be trained using the iterative scaling algorithm, which maximizes the conditional likelihood of the hidden states given the observations and the features .