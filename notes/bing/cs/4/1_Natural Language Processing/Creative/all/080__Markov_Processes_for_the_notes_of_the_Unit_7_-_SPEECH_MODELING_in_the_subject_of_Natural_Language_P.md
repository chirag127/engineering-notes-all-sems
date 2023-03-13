### Markov Processes for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- A Markov process is a stochastic process that has the property of memorylessness, meaning that the future state of the system depends only on the current state and not on the previous states.
- A Markov process can be used to model the dynamics of a system that changes over time in a probabilistic way, such as speech signals, weather patterns, stock prices, etc.
- A Markov process can be represented by a state diagram, where each node is a possible state of the system and each edge is a transition probability between states.
- A Markov process can be classified into two types: discrete-time and continuous-time, depending on whether the state changes occur at fixed intervals or at random times.
- A Markov process can also be classified into two types: observable and hidden, depending on whether the state of the system is directly measurable or not.
- An observable Markov process is also called a Markov chain, and it can be used to generate a sequence of symbols or events that follow a certain probability distribution, such as words in a sentence, letters in a word, etc.
- A hidden Markov process is also called a hidden Markov model (HMM), and it can be used to infer the underlying state of the system from a sequence of observations that are related to the state, such as speech signals, DNA sequences, etc.
- A hidden Markov model consists of three components: a set of states, a set of observations, and a set of parameters that define the transition probabilities between states and the emission probabilities of observations from states.
- A hidden Markov model can be used for various tasks in speech and language processing, such as speech recognition, speech synthesis, language modeling, part-of-speech tagging, named-entity recognition, etc .
- A hidden Markov model can be trained using various algorithms, such as the forward-backward algorithm, the Viterbi algorithm, the Baum-Welch algorithm, etc, to estimate the optimal parameters that maximize the likelihood of the observed data.
- A hidden Markov model can be evaluated using various metrics, such as the accuracy, the perplexity, the word error rate, the F-measure, etc, to measure the performance of the model on a given task or dataset.

Some mnemonics and learning tricks for Markov processes are:

- To remember the difference between discrete-time and continuous-time Markov processes, think of a clock: a discrete-time Markov process changes state only when the clock ticks, while a continuous-time Markov process can change state at any time.
- To remember the difference between observable and hidden Markov processes, think of a coin: an observable Markov process is like flipping a coin and seeing the outcome, while a hidden Markov process is like flipping a coin and hearing the sound.
- To remember the components of a hidden Markov model, think of a game: a set of states is like the possible moves, a set of observations is like the possible outcomes, and a set of parameters is like the rules of the game.
- To remember the tasks that hidden Markov models can be used for, think of the acronym SLAP: Speech recognition, Language modeling, Part-of-speech tagging, and Named-entity recognition.