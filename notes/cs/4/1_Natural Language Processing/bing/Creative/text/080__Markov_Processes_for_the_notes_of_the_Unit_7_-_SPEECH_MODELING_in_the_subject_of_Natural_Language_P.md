### Markov Processes for the notes of the Unit 7 - SPEECH MODELING in the subject of Natural Language Processing

- A Markov process is a stochastic process that models the temporal or sequential data, i.e., data that are ordered.
- It assumes that the future states of the system depend only on the current state, not on the events that occurred before it. This is called the Markov property .
- A Markov process can be used to model the dependencies of current information (e.g. weather) with previous information.
- A Markov process consists of states, transition scheme between states, and emission of outputs (discrete or continuous).
- There are four common types of Markov processes, depending on whether the system state is fully or partially observable, and whether the system is autonomous or controlled:

  - Markov chain: The system state is fully observable and the system is autonomous. It is the simplest Markov process that models the state of a system with a random variable that changes through time. For example, a Markov chain can be used to model the weather of tomorrow using the weather of today.
  - Hidden Markov model (HMM): The system state is partially observable or noisily observable and the system is autonomous. It is a Markov chain that models the state of a system with a hidden variable that emits an observable output. For example, a hidden Markov model can be used for speech recognition, where the hidden state is the spoken text and the observable output is the speech audio waveform .
  - Markov decision process (MDP): The system state is fully observable and the system is controlled. It is a Markov chain that models the state of a system with a random variable that changes through time and an action vector that is applied to the system. For example, a Markov decision process can be used to compute a policy of actions that will maximize some utility with respect to expected rewards.
  - Partially observable Markov decision process (POMDP): The system state is partially observable or noisily observable and the system is controlled. It is a Markov decision process that models the state of a system with a hidden variable that emits an observable output and an action vector that is applied to the system. For example, a partially observable Markov decision process can be used to model a robot navigation problem, where the hidden state is the robot's location and the observable output is the sensor readings.

- Markov processes can be used for various goals, such as learning statistics of sequential data, doing prediction or estimation, and recognizing patterns.
- Markov processes can be mathematically formulated using probability theory and matrix algebra .
- Markov processes can be implemented using various algorithms, such as the Viterbi algorithm, the forward algorithm, and the Baum-Welch algorithm .
- Markov processes are widely used in natural language processing (NLP) and machine learning, as they can capture the sequential and contextual information of natural language data . For example, a Markov chain can be used to generate a sequence of words that form a complete sentence, or a hidden Markov model can be used for named-entity recognition and tagging parts of speech .

: https://www.techtarget.com/whatis/definition/Markov-model
: https://cecas.clemson.edu/~ahoover/ece854/refs/Ramos-Intro-HMM.pdf
: https://en.wikipedia.org/wiki/Markov_model
: https://www.i2tutorials.com/understanding-hidden-markov-model-for-speech-recognition/
: https://pubmed.ncbi.nlm.nih.gov/8930521/