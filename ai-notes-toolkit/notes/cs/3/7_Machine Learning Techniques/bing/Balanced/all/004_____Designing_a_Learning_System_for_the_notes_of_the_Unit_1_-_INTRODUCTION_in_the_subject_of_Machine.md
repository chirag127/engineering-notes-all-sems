# Designing a Learning System

## Unit 1 - INTRODUCTION

- A learning system is a system that can learn from data and improve its performance over time.
- Learning systems can be classified into different types based on the following criteria:

  - The type of learning task: supervised, unsupervised, semi-supervised, or reinforcement learning.
  - The type of learning model: parametric, non-parametric, or hybrid.
  - The type of learning algorithm: batch, online, or incremental.
  - The type of learning feedback: explicit, implicit, or none.

- Supervised learning is a type of learning task where the system is given a set of input-output pairs (also called training examples) and learns a function that maps the inputs to the outputs.
- Unsupervised learning is a type of learning task where the system is given a set of inputs (also called unlabeled data) and learns to discover patterns, structure, or hidden variables in the data.
- Semi-supervised learning is a type of learning task where the system is given a mixture of labeled and unlabeled data and learns to leverage both types of information.
- Reinforcement learning is a type of learning task where the system is given a goal and interacts with an environment through actions and rewards and learns a policy that maximizes the expected reward.

- Parametric learning models are models that have a fixed number of parameters that are learned from the data. Examples of parametric models are linear regression, logistic regression, and neural networks.
- Non-parametric learning models are models that do not have a fixed number of parameters and can grow or shrink depending on the data. Examples of non-parametric models are k-nearest neighbors, decision trees, and kernel methods.
- Hybrid learning models are models that combine parametric and non-parametric components. Examples of hybrid models are Gaussian processes, random forests, and deep belief networks.

- Batch learning algorithms are algorithms that process the entire data set at once and produce a single output. Batch learning algorithms are often computationally intensive and require a lot of memory.
- Online learning algorithms are algorithms that process the data one example at a time and update the output incrementally. Online learning algorithms are often computationally efficient and require less memory.
- Incremental learning algorithms are algorithms that process the data in small batches and update the output gradually. Incremental learning algorithms are often a compromise between batch and online learning algorithms.

- Explicit feedback is feedback that is directly provided by the user or the environment to the system. Examples of explicit feedback are ratings, labels, or rewards.
- Implicit feedback is feedback that is indirectly inferred from the user or the environment behavior. Examples of implicit feedback are clicks, views, or purchases.
- No feedback is the absence of any feedback from the user or the environment. Examples of no feedback are unsupervised learning tasks or exploration phases in reinforcement learning.