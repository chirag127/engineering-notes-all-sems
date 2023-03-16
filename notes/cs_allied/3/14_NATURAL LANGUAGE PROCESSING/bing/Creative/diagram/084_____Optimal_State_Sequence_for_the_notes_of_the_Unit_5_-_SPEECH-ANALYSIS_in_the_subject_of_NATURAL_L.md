### Optimal State Sequence for HMM

- A hidden Markov model (HMM) is a probabilistic model that can be used to represent the sequential and stochastic nature of speech signals.
- An HMM consists of a set of hidden states, a set of observable symbols, and a set of transition and emission probabilities that govern the state transitions and symbol emissions.
- The goal of speech recognition is to find the most likely sequence of words that corresponds to a given speech signal. This can be done by finding the most likely sequence of hidden states that generated the speech signal, and then mapping the states to words using a lexicon.
- The optimal state sequence can be found using the Viterbi algorithm, which is a dynamic programming algorithm that computes the maximum likelihood path through the HMM .
- The Viterbi algorithm works by keeping track of the most likely state and the most likely previous state for each time step, and then backtracking from the final state to the initial state to obtain the optimal state sequence .
- The optimal state sequence can be used to estimate the model parameters, such as the transition and emission probabilities, using the maximum likelihood or the maximum a posteriori criterion.
- The optimal state sequence can also be used to perform speech analysis tasks, such as speaker diarization, speaker recognition, and spoken language understanding, by extracting relevant features from the state sequence and applying classification or clustering techniques .

: [13.10 - Optimal State Sequence for HMM | STAT 508](https://online.stat.psu.edu/stat508/lesson/13/13.10)
: [Decoding optimal state sequence with smooth state likelihoods](https://ieeexplore.ieee.org/document/540307/)
: [Introduction to Automatic Speech Recognition (ASR) - GitHub Pages](https://maelfabien.github.io/machinelearning/speech_reco/)
: [Speech Parameter - an overview | ScienceDirect Topics](https://www.sciencedirect.com/topics/computer-science/speech-parameter)