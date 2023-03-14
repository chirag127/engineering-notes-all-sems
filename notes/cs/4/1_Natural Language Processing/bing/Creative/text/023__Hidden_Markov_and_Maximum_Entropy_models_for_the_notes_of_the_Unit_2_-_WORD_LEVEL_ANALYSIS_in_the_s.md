### Hidden Markov and Maximum Entropy models for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions)  .
- HMM is based on the assumption that the hidden state at a given time depends only on the previous hidden state (Markov property) and the emission at a given time depends only on the current hidden state (conditional independence) .
- HMM can be represented by a 5-tuple (Q, V, A, B, π), where Q is the set of hidden states, V is the set of emissions, A is the state transition matrix, B is the emission probability matrix, and π is the initial state distribution .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, speech recognition, sentence segmentation, and grapheme-to-phoneme conversion .
- HMM can be trained using the Baum-Welch algorithm, which is a special case of the Expectation-Maximization algorithm, and can be used to find the most likely sequence of hidden states using the Viterbi algorithm, which is a dynamic programming algorithm .
- Maximum Entropy Model (MaxEnt) is a discriminative model that assigns a probability distribution over a set of classes given a set of features or contextual evidence .
- MaxEnt is based on the principle of maximum entropy, which states that the best model is the one that makes the fewest assumptions or has the highest entropy, subject to the constraints imposed by the observed data .
- MaxEnt can be represented by a log-linear model, where the probability of a class given a feature vector is proportional to the exponential of the weighted sum of the features .
- MaxEnt can be trained using the Generalized Iterative Scaling algorithm, which is an iterative algorithm that adjusts the weights of the features to maximize the likelihood of the observed data .
- MaxEnt can be used for various natural language processing tasks, such as text classification, sentiment analysis, named entity recognition, and information extraction .
- Maximum Entropy Markov Model (MEMM) is a variant of MaxEnt that incorporates the Markov property, which means that the class at a given time depends only on the previous class (or a fixed number of previous classes) .
- MEMM is a sequence classifier that extends a standard MaxEnt classifier by assuming that the classes are connected in a Markov chain rather than being conditionally independent of each other .
- MEMM can be represented by a directed graphical model, where the nodes are the classes and the edges are the features .
- MEMM can be trained using the same algorithm as MaxEnt, but with the additional constraint that the sum of the probabilities of all possible classes at each time step must be one .
- MEMM can be used for the same tasks as HMM, but with the advantage of being able to incorporate more complex and overlapping features .