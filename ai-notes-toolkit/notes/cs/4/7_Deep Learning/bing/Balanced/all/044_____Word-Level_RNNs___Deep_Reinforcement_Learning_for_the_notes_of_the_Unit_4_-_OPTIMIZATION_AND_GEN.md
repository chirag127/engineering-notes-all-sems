# Word-Level RNNs & Deep Reinforcement Learning

- Word-level RNNs are recurrent neural networks that operate on sequences of words, rather than characters or subwords.
- Word-level RNNs can be used for various natural language processing tasks, such as language modeling, text generation, machine translation, text summarization, sentiment analysis, etc.
- Word-level RNNs typically consist of an embedding layer, a recurrent layer (such as LSTM or GRU), and an output layer (such as softmax or linear).
- The embedding layer maps each word in the input sequence to a low-dimensional vector representation, which captures some semantic and syntactic information about the word.
- The recurrent layer processes the embedded word vectors sequentially, and maintains a hidden state that encodes the information from the previous words in the sequence.
- The output layer produces a prediction for each word in the sequence, such as the next word (for language modeling), the corresponding word in another language (for machine translation), or a label (for sentiment analysis).
- Word-level RNNs can be trained using various loss functions, such as cross-entropy, negative log-likelihood, or reinforcement learning.

## Deep Reinforcement Learning

- Deep reinforcement learning (DRL) is a branch of machine learning that combines deep neural networks with reinforcement learning, which is a framework for learning from trial and error.
- DRL can be used for various tasks that involve sequential decision making under uncertainty, such as game playing, robotics, self-driving cars, etc.
- DRL typically consists of an agent, an environment, a policy, a value function, and a reward function.
- The agent is the learner and decision maker, which interacts with the environment through actions and observations.
- The environment is the external system that responds to the agent's actions and provides feedback in the form of rewards and new observations.
- The policy is a function that maps the agent's observations to actions, which can be deterministic or stochastic.
- The value function is a function that estimates the expected return (cumulative discounted reward) for each state or state-action pair, which can be used to guide the agent's actions.
- The reward function is a function that assigns a scalar value to each state or state-action pair, which reflects the desirability of the outcome.
- DRL can be categorized into two types: model-free and model-based.
- Model-free DRL does not rely on a model of the environment, but directly learns the policy or value function from experience, using algorithms such as Q-learning, SARSA, policy gradient, actor-critic, etc.
- Model-based DRL uses a model of the environment, which can be learned from data or given by prior knowledge, to simulate the outcomes of actions and plan ahead, using algorithms such as Monte Carlo tree search, Dyna, etc.