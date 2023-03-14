### Viterbi Search for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Viterbi Search is a dynamic programming algorithm for finding the most likely sequence of hidden states that results in a sequence of observed events, especially in the context of Hidden Markov Models (HMMs).
- Viterbi Search is widely used in speech recognition, speech synthesis, diarization, keyword spotting, computational linguistics, and bioinformatics.
- Viterbi Search is named after Andrew Viterbi, who proposed it in 1967 as a decoding algorithm for convolutional codes over noisy digital communication links.
- Viterbi Search can be applied to HMM-based speech recognition, where the acoustic signal is the observed sequence of events, and a string of text is the hidden cause of the acoustic signal. The Viterbi algorithm finds the most likely string of text given the acoustic signal.
- Viterbi Search can also be applied to statistical parsing, where a dynamic programming algorithm can be used to discover the single most likely context-free derivation (parse) of a string, which is commonly called the "Viterbi parse"   .
- Viterbi Search can also be applied to target tracking, where the track is computed that assigns a maximum likelihood to a sequence of observations.
- Viterbi Search can also be extended to 3-dimensional trellis space composed of talker directions, input frames, and HMM states, which can be used for hands-free speech recognition based on a microphone array  .

The basic steps of the Viterbi Search algorithm are as follows:

- Initialize a state list with one cell for each state in the system, and assign the initial probabilities for each state at time t = 0.
- For each time step t from 1 to T, where T is the length of the observation sequence, do the following:
  - Clear the state list for time t.
  - For each state s in the state list, compute the transition probabilities from the previous states at time t-1 to the current state s at time t, and multiply them by the emission probabilities of the observed event at time t given the current state s. This gives the joint probabilities of the state and observation sequences up to time t ending with state s.
  - For each state s in the state list, find the maximum joint probability among all the previous states, and store it as the score for state s at time t. Also store a back pointer to the previous state that gives the maximum joint probability.
- At the end of the observation sequence, find the state s with the maximum score at time T, and trace back the pointers from s to the initial state, which gives the most likely state sequence that explains the observation sequence. This is called the Viterbi path.

A possible mnemonic for remembering the Viterbi Search algorithm is:

- Viterbi Search finds the best path
- Through a trellis of states and events
- By multiplying transitions and emissions
- And keeping the max and the back