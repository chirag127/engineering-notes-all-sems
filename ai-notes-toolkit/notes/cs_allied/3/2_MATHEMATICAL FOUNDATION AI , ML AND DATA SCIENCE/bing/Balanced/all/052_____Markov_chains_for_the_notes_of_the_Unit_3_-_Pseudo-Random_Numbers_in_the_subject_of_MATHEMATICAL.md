# Markov Chains

- A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.
- The defining characteristic of a Markov chain is that no matter how the process arrived at its present state, the possible future states are fixed. This is known as the **Markov property** or **memorylessness**.
- A Markov chain can be represented by a **state space**, a set of possible states that the system can be in, and a **transition matrix**, a matrix that specifies the probability of moving from one state to another .
- A Markov chain can also be represented by a **directed graph**, where the nodes are the states and the edges are labeled with the transition probabilities.
- A Markov chain is one example of a Markov model, but other examples exist. One other example commonly used in the field of artificial intelligence is the **Hidden Markov model**, which is a Markov chain for which the state is not directly observable.

## Examples of Markov Chains

- One simple and often used example of a Markov chain is the board game “Chutes and Ladders.” The state space is the set of squares on the board, and the transition matrix is determined by the dice roll and the presence of chutes and ladders on the board.
- Another example of a Markov chain is the weather prediction. The state space is the set of possible weather conditions, such as sunny, cloudy, rainy, etc. The transition matrix is based on historical data or meteorological models that estimate the probability of changing from one weather condition to another.
- A third example of a Markov chain is the eating habits of a person who eats only fruits, vegetables, or meat. The state space is the set of food types, and the transition matrix is governed by the following rules: The person eats only one time in a day. If the person eats fruits today, they will eat fruits with 0.3 probability, vegetables with 0.5 probability, and meat with 0.2 probability tomorrow. If the person eats vegetables today, they will eat fruits with 0.4 probability, vegetables with 0.2 probability, and meat with 0.4 probability tomorrow. If the person eats meat today, they will eat fruits with 0.5 probability, vegetables with 0.3 probability, and meat with 0.2 probability tomorrow.