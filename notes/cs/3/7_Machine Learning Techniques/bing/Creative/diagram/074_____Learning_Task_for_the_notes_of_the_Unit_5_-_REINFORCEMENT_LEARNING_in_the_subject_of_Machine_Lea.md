# Learning Task for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

## Introduction

- Reinforcement learning (RL) is a machine learning training method based on rewarding desired behaviors and/or punishing undesired ones .
- RL is about learning the optimal behavior in an environment to obtain maximum reward. This optimal behavior is learned through interactions with the environment and observations of how it responds, similar to children exploring the world around them and learning the actions that lead to positive outcomes.
- RL is a learning paradigm that learns to optimize sequential decisions, which are decisions that are taken recurrently across time steps, for example, daily stock replenishment decisions taken in inventory control.
- RL can be used in large environments in the following situations:
  - A model of the environment is known, but an analytic solution is not available
  - Only a simulation model of the environment is given (the subject of simulation-based optimization)
  - The only way to collect information about the environment is to interact with it

## Elements of RL

- RL elements are as follows:
  - Policy: A policy defines the learning agent's way of behaving at a given time. It is a mapping from perceived states of the environment to actions to be taken when in those states.
  - Reward function: A reward function defines the goal of a reinforcement learning problem. It maps each perceived state (or state-action pair) of the environment to a numerical value, called reward, which indicates the intrinsic desirability of that state. The agent's objective is to maximize the total reward it receives in the long run.
  - Value function: A value function specifies what is good in the long run. It is the expected total amount of reward an agent can accumulate over the future, starting from a given state. A value function is a prediction of future reward and is used to evaluate the goodness/badness of states and to select actions that lead to good states.
  - Model of the environment: A model of the environment is a representation of how the environment behaves. It predicts what the next state and reward will be, given the current state and action. A model can be used for planning, by which we mean any way of deciding on a course of action by considering possible future situations before they are actually experienced.