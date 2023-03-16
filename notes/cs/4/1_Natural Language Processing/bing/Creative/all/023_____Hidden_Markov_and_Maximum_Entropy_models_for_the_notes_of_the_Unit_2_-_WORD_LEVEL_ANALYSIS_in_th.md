# Hidden Markov and Maximum Entropy models for natural language processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions) .
- HMM assumes that the hidden states follow a Markov chain, which means that the current state depends only on the previous state, and the emissions depend only on the current state .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, named entity recognition, speech recognition, and machine translation  .
- HMM can be represented by five parameters: the set of hidden states, the set of emissions, the initial state probabilities, the state transition probabilities, and the emission probabilities .
- HMM can be trained using the Baum-Welch algorithm, which is a special case of the Expectation-Maximization algorithm, and can find the maximum likelihood estimates of the parameters .
- HMM can be used for decoding, which means finding the most likely sequence of hidden states given a sequence of emissions, using the Viterbi algorithm, which is a dynamic programming algorithm .

- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard maximum entropy classifier by assuming that the unknown values to be learnt are connected in a Markov chain rather than being conditionally independent of each other .
- MEMM can also be used for various natural language processing tasks, such as part-of-speech tagging and information extraction .
- MEMM can overcome some of the limitations of HMM, such as the inability to incorporate arbitrary features of the observations and the states, and the label bias problem, which means that the states with fewer outgoing transitions tend to be preferred  .
- MEMM can be represented by a set of features and weights, which are used to calculate the conditional probabilities of the states given the observations .
- MEMM can be trained using the Generalized Iterative Scaling algorithm, which is a gradient-based algorithm, and can find the maximum entropy estimates of the weights .
- MEMM can also be used for decoding, using the Viterbi algorithm, but with a modified calculation of the transition probabilities, which are conditioned on the observations .