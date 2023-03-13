### Markov Processes for Speech Modeling

- A Markov process is a stochastic process that has the property of memorylessness, meaning that the future state of the system depends only on the current state and not on the previous states.
- A Markov chain is a sequence of random variables that follow a Markov process, where each variable can take a finite number of possible values called states.
- A Markov model is a mathematical representation of a Markov chain, where the probabilities of state transitions are specified by a matrix or a graph.
- Markov models are widely used in speech recognition and natural language processing, as they can capture the statistical regularities and variations of speech signals and linguistic units  .
- A hidden Markov model (HMM) is a special type of Markov model, where the states are not directly observable, but are inferred from a sequence of observable symbols or features.
- HMMs are commonly used to model the acoustic features of speech signals, where each state corresponds to a phoneme or a sub-phoneme, and the observable symbols are the spectral vectors extracted from the speech frames .
- HMMs can also be used to model the linguistic units of natural language, such as words, phrases, sentences, or parts of speech, where the states are the hidden linguistic categories and the observable symbols are the words or tokens.
- HMMs can perform three basic tasks: evaluation, decoding, and learning .
  - Evaluation is the task of computing the probability of an observed sequence given a model.
  - Decoding is the task of finding the most likely sequence of hidden states given an observed sequence and a model.
  - Learning is the task of estimating the model parameters from a set of observed sequences.
- HMMs can be trained using various algorithms, such as the forward-backward algorithm, the Viterbi algorithm, the Baum-Welch algorithm, or the expectation-maximization algorithm .
- HMMs have some limitations, such as the assumption of independence between the observable symbols and the states, the assumption of stationarity of the state transition probabilities, and the difficulty of modeling long-term dependencies and context information .
- HMMs can be extended or modified to overcome some of these limitations, such as using n-gram models, context-dependent models, continuous-density models, or deep neural network models .