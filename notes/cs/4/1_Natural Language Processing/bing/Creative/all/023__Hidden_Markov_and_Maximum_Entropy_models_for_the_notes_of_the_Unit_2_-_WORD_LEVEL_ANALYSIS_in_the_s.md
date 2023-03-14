### Hidden Markov and Maximum Entropy models for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Hidden Markov Model (HMM) is a probabilistic graphical model that allows us to calculate a sequence of unknown or unobserved variables (hidden states) from a set of observed variables (emissions)  . For example, predicting weather conditions (hidden states) on the basis of types of clothes worn by someone (emissions) is a simple example of HMM.
- HMM is based on the assumption that the hidden state at time t depends only on the hidden state at time t-1, and the emission at time t depends only on the hidden state at time t. This is called the Markov property .
- HMM can be represented by a 5-tuple (Q, V, A, B, π), where Q is the set of hidden states, V is the set of emissions, A is the transition matrix, B is the emission matrix, and π is the initial state distribution .
- HMM can be used for various natural language processing tasks, such as part-of-speech tagging, speech recognition, sentence segmentation, and grapheme-to-phoneme conversion . HMM can be trained using the Baum-Welch algorithm, which is a special case of the Expectation-Maximization algorithm . HMM can be used to find the most likely sequence of hidden states given a sequence of emissions using the Viterbi algorithm, which is a dynamic programming algorithm .
- Maximum Entropy Model (MaxEnt) is a discriminative model that assigns a probability distribution over a set of classes given a set of features . MaxEnt is based on the principle of maximum entropy, which states that the best model is the one that makes the least assumptions and is consistent with the observed data .
- MaxEnt can be used for various natural language processing tasks, such as text classification, sentiment analysis, and named entity recognition . MaxEnt can be trained using the Generalized Iterative Scaling algorithm, which iteratively adjusts the weights of the features to maximize the likelihood of the observed data .
- Maximum Entropy Markov Model (MEMM) is a variant of MaxEnt that extends it to sequence labeling tasks . MEMM assumes that the class at time t depends on the class at time t-1 and the features at time t, forming a Markov chain . MEMM can be trained using the same algorithm as MaxEnt, and can be used to find the most likely sequence of classes given a sequence of features using the Viterbi algorithm .
- MEMM is different from HMM in that it is a discriminative model, not a generative model, and it can use arbitrary features, not just emissions . MEMM can overcome some of the limitations of HMM, such as the sparsity of the emission matrix and the independence assumption of the emissions .

: Jurafsky, D. and Martin, J. (2007). Hidden Markov and Maximum Entropy Models. In Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition. Draft of September 18, 2007. https://www.cs.jhu.edu/~jason/papers/jurafsky+martin.bookdraft07.ch6.pdf

: Ratnaparkhi, A. (1997). A Simple Introduction to Maximum Entropy Models for Natural Language Processing. IRCS Technical Report No. IRCS-97-08. https://repository.upenn.edu/cgi/viewcontent.cgi?article=1083&context=ircs_reports

: Maximum-entropy Markov model. (2021, October 27). In Wikipedia. https://en.wikipedia.org/wiki/Maximum-entropy_Markov_model

: Statistical Natural Language Processing: Models and Methods (CS775). (n.d.). Retrieved October 31, 2021, from https://www.cs.cornell.edu/courses/cs775/2001sp/default.html

: Singh, S., & Singh, S. (2020). Review on Usage of Hidden Markov Model in Natural Language Processing. In S. Satapathy, V. Bhateja, A. Joshi, & D. Das (Eds.), Advances in Intelligent