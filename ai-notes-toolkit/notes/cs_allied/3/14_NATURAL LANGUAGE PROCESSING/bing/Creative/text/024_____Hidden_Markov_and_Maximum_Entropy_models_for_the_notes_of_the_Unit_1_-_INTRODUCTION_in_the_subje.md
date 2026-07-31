### Hidden Markov and Maximum Entropy models for natural language processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions) .
- HMM assumes that the hidden states follow a Markov chain, which means that the current state depends only on the previous state, and the emissions depend only on the current state .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, speech recognition, named entity recognition, and machine translation  .
- HMM can be represented by five parameters: the set of hidden states, the set of emissions, the initial state probabilities, the state transition probabilities, and the emission probabilities .
- HMM can be trained using the Baum-Welch algorithm, which is a special case of the Expectation-Maximization algorithm, and can be used to find the most likely sequence of hidden states using the Viterbi algorithm, which is a dynamic programming technique .
- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learnt are connected in a Markov chain rather than being conditionally independent of each other .
- MEMM can also be used for natural language processing tasks, such as part-of-speech tagging and information extraction  .
- MEMM can overcome some of the limitations of HMM, such as the inability to incorporate rich features and the label bias problem, which occurs when some states have very low transition probabilities and tend to dominate the predictions  .
- MEMM can be represented by a set of features and weights, which are used to calculate the conditional probability of a state given an observation and a previous state .
- MEMM can be trained using the Generalized Iterative Scaling algorithm or the Improved Iterative Scaling algorithm, which are both iterative methods that adjust the weights to maximize the likelihood of the training data .
- MEMM can be used to find the most likely sequence of states using the Viterbi algorithm, but with some modifications to account for the conditional probabilities .