 Here is the content in markdown format:

### Markov Processes for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- Markov processes are models of random processes where the future state depends only on the present state and not on the sequence of events that led to the present state. They are used to model speech signals in speech recognition systems.
- In speech recognition, the speech signal is divided into small frames of 10-30 ms and the spectral characteristics of each frame are analyzed to predict the next sound. This can be modeled as a Markov process where the current spectral characteristics predict the next spectral characteristics.
- Examples of Markov processes used in speech recognition:
    - Discrete Markov process: The spectral characteristics can have discrete values like phonemes. The probability of transitioning from one phoneme to the next can be modeled as a discrete Markov process.
    - Continuous Markov process: The spectral characteristics can have continuous values. The probability distribution of the next spectral feature can be modeled as a continuous Markov process using Gaussian mixtures.
- Advantages:
    - Simple and efficient to compute probabilities of transitions.
    - Can model complex sequences such as speech signals.
- Disadvantages:
    - Assumption that the future only depends on the present and not the past is not always true. Long term dependencies are not captured.
    - As the number of states increase, computing the transition probabilities can become infeasible. Approximation techniques are required.
- Applications: Speech recognition, part-of-speech tagging, machine translation, etc.

Mnemonics:
- Think of the 'present' determining the 'future' in a Markov process. The future state depends only on the present state.
- The spectral characteristics of each frame are like the 'present state' and the next frame's characteristics are the 'future state'. The probability of the future state depends only on the present state.