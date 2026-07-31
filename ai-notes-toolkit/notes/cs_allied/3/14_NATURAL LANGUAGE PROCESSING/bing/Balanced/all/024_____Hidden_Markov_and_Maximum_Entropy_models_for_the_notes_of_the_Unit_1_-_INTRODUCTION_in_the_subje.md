# Hidden Markov and Maximum Entropy models

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions) .
- HMM assumes that the hidden states follow a Markov chain, which means that the current state depends only on the previous state, and the emissions depend only on the current state .
- HMM can be represented by a 5-tuple: (S, V, A, B, π), where S is the set of hidden states, V is the set of emissions, A is the state transition matrix, B is the emission probability matrix, and π is the initial state distribution .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, speech recognition, named entity recognition, and machine translation  .
- The main problems that HMM can solve are: evaluation, decoding, and learning .
  - Evaluation: given an HMM and a sequence of emissions, compute the probability of the sequence under the model.
  - Decoding: given an HMM and a sequence of emissions, find the most likely sequence of hidden states that generated the emissions.
  - Learning: given a set of sequences of emissions, estimate the parameters of the HMM that best fit the data.
- The common algorithms that HMM can use are: forward-backward, Viterbi, and Baum-Welch .
  - Forward-backward: a dynamic programming algorithm that computes the probabilities of all possible hidden states at each position in the sequence, using the forward and backward passes.
  - Viterbi: a dynamic programming algorithm that finds the most likely sequence of hidden states, using the maximum probability path at each position in the sequence.
  - Baum-Welch: an expectation-maximization algorithm that iteratively updates the parameters of the HMM, using the expected counts of state transitions and emissions from the forward-backward algorithm.

- Maximum Entropy Model (MEM) is a discriminative model that learns a probability distribution over a set of classes, given a set of features that describe the input .
- MEM assumes that the probability distribution is the one that maximizes the entropy, which is a measure of uncertainty or randomness, subject to the constraints imposed by the features .
- MEM can be represented by a log-linear function: P(c|x) = exp(∑i λifi(x,c)) / Z(x), where c is the class, x is the input, fi is the feature function, λi is the feature weight, and Z(x) is the normalization factor .
- MEM can be used for various natural language processing tasks, such as text classification, sentiment analysis, information extraction, and natural language generation .
- The main problem that MEM can solve is: classification, which is to assign the most likely class to a given input .
- The common algorithm that MEM can use is: iterative scaling, which is an optimization algorithm that iteratively updates the feature weights, using the gradient of the log-likelihood function .

- Maximum Entropy Markov Model (MEMM) is a discriminative model that extends a standard MEM by assuming that the classes are connected in a Markov chain, rather than being conditionally independent of each other .
- MEMM can be represented by a log-linear function: P(c|x, c') = exp(∑i λifi(x,c,c')) / Z(x, c'), where c is the current class, c' is the previous class, x is the input, fi is the feature function, λi is the feature weight, and Z(x, c') is the normalization factor .
- MEMM can be used for natural language processing tasks that involve sequential labeling, such as part-of-speech tagging and information extraction  .
- The main problems that MEMM can solve are: evaluation, decoding, and learning .
  - Evaluation: given an MEMM and a sequence of inputs, compute the probability of the sequence under the model.
  - Decoding: given an MEMM and a sequence of inputs, find the most likely sequence of classes that generated the inputs.
  - Learning: given a set of sequences of inputs and classes, estimate the parameters of the MEMM that best fit the