# Markov Processes for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- A Markov process is a stochastic process that models the evolution of a system that changes its state over time, depending on the current state and some probabilistic rules .
- A Markov process has the property of **memorylessness**, which means that the future state of the system only depends on the present state, and not on the past history .
- A Markov process can be represented by a **state diagram**, which shows the possible states of the system and the transition probabilities between them .
- A Markov process can be classified into two types: **discrete** and **continuous** .
  - A discrete Markov process has a finite or countable number of states, and the transitions occur at discrete time intervals .
  - A continuous Markov process has an infinite or uncountable number of states, and the transitions occur continuously over time .
- Markov processes are widely used in natural language processing (NLP) to model the patterns and dependencies in natural language, such as characters, words, sentences, and speech  .
- Markov processes can be used to generate natural language, by sampling from the transition probabilities of the states, and producing sequences of characters or words that follow the patterns of the natural language .
- Markov processes can also be used to analyze natural language, by estimating the transition probabilities of the states from a given corpus of natural language, and using them to compute the likelihood or probability of a given sequence of characters or words  .
- Markov processes can be extended to **hidden Markov models (HMMs)**, which are Markov processes that have two layers of states: **hidden states** and **observed states**  .
  - Hidden states are the states of the underlying system that are not directly observable, but influence the observed states  .
  - Observed states are the states of the system that are directly observable, but depend on the hidden states  .
  - HMMs can be represented by a **state diagram** that shows the transition probabilities between the hidden states, and the emission probabilities between the hidden states and the observed states  .
- HMMs are widely used in NLP to model the relationship between the hidden structure and the observed surface of natural language, such as the syntax and the words, or the phonemes and the speech   .
- HMMs can be used to generate natural language, by sampling from the transition and emission probabilities of the states, and producing sequences of observed states that follow the patterns of the natural language  .
- HMMs can also be used to analyze natural language, by estimating the transition and emission probabilities of the states from a given corpus of natural language, and using them to perform tasks such as **tagging**, **parsing**, **recognition**, and **translation**   .