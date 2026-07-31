### Markov chains

- A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.
- The defining characteristic of a Markov chain is that no matter how the process arrived at its present state, the possible future states are fixed. This is known as the **Markov property**.
- A Markov chain can be represented by a **transition matrix** that contains the probabilities of moving from one state to another. For example, the transition matrix for the weather example is:

| | Sunny | Rainy |
| --- | --- | --- |
| Sunny | 0.8 | 0.2 |
| Rainy | 0.4 | 0.6 |

- This means that if today is sunny, there is an 80% chance that tomorrow will be sunny and a 20% chance that tomorrow will be rainy. Similarly, if today is rainy, there is a 40% chance that tomorrow will be sunny and a 60% chance that tomorrow will be rainy.
- A Markov chain can also be represented by a **directed graph** where the nodes are the states and the edges are labeled with the transition probabilities. For example, the directed graph for the weather example is:

![weather markov chain](https://www.publichealth.columbia.edu/sites/default/files/markov_chain.png)

- A Markov chain can be used to model various phenomena that involve random transitions, such as text generation, finance modeling, cruise control systems, etc.