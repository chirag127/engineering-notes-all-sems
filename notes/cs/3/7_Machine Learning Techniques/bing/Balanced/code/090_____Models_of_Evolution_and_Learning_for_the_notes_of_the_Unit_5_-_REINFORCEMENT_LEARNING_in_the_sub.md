# Models of Evolution and Learning for Reinforcement Learning

- Reinforcement learning (RL) is a machine learning technique that enables an agent to learn from its own actions and rewards in an environment.
- Evolutionary algorithms (EAs) are a class of optimization methods that mimic the principles of natural selection and variation to find solutions to complex problems.
- Evolutionary reinforcement learning (ERL) is a hybrid approach that combines RL and EA to leverage the advantages of both methods.
- ERL can be divided into two main categories: evolutionary-driven RL and evolutionary RL.

## Evolutionary-Driven Reinforcement Learning (evo-RL)

- Evo-RL embeds the RL algorithm in an evolutionary cycle, where the agent's behavior is influenced by both its learnable parameters (such as neural network weights) and its evolvable parameters (such as hyperparameters or network architecture).
- Evo-RL aims to balance exploration and exploitation by using the population diversity of EA to provide varied data to train the RL agent, and by reinserting the RL agent into the EA population periodically to inject gradient information into the EA.
- Evo-RL can be applied to different RL algorithms, such as Q-learning, policy gradient, or actor-critic methods.
- Evo-RL can improve the sample efficiency, robustness, and generalization of RL agents, as well as discover novel and diverse behaviors.
- An example of evo-RL is the Deep Evolutionary Reinforcement Learning (DERL) framework, which can evolve diverse agent morphologies to learn challenging locomotion and manipulation tasks in physics-based simulations.

## Evolutionary Reinforcement Learning (ERL)

- ERL uses EA to evolve the RL agent itself, rather than its parameters or behavior. The agent's genotype encodes the RL algorithm that the agent uses to learn from its environment.
- ERL aims to discover new, analytically interpretable, and generalizable RL algorithms by using a graph representation and applying optimization techniques from the AutoML community.
- ERL can generate RL algorithms that outperform existing ones on various benchmarks, such as Atari games, MuJoCo tasks, and gridworlds.
- ERL can also reveal novel insights into the design principles and trade-offs of RL algorithms, such as the role of exploration, memory, and credit assignment.
- An example of ERL is the Evolving Reinforcement Learning Algorithms (ERLA) framework, which can evolve RL algorithms that are comparable or superior to human-designed ones.

: [2007.04725] EVO-RL: Evolutionary-Driven Reinforcement Learning - arXiv.org
: Evolutionary Reinforcement Learning: A Survey - Semantic Scholar
: Design, Evaluation and Comparison of Evolution and Reinforcement Learning Models - ResearchGate
: Embodied intelligence via learning and evolution - Nature
: Evolving Reinforcement Learning Algorithms – Google AI Blog