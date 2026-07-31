# Unit 1 - Introduction

## Learning Objectives

- Define machine learning and its applications
- Understand the perspectives and issues of machine learning
- Explain the concept learning and version space
- Describe the inductive bias and its role in learning
- Compare and contrast different types of machine learning
- Apply decision tree learning algorithm to a given problem
- Evaluate the performance of machine learning models

## Machine Learning

- Machine learning is the study of computer algorithms that improve automatically through experience and by the use of data.
- Machine learning algorithms build a mathematical model based on sample data, known as “training data”, in order to make predictions or decisions without being explicitly programmed to do so.
- Machine learning has many applications, such as natural language processing, computer vision, speech recognition, recommender systems, self-driving cars, etc.

## Perspectives and Issues of Machine Learning

- Machine learning can be viewed from different perspectives, such as computational, statistical, cognitive, and biological.
- Computational perspective focuses on the design and analysis of efficient algorithms for learning from data.
- Statistical perspective emphasizes the probabilistic models and methods for inference and estimation from data.
- Cognitive perspective studies the psychological and neural mechanisms of learning and reasoning in humans and animals.
- Biological perspective investigates the molecular and cellular processes of learning and adaptation in living systems.
- Machine learning also faces many issues and challenges, such as scalability, robustness, interpretability, privacy, ethics, etc.

## Concept Learning and Version Space

- Concept learning is a form of machine learning where the learner is given a set of examples that belong to a certain concept and a set of examples that do not belong to that concept, and the learner has to induce a general definition of the concept that is consistent with the given examples.
- Version space is a representation of the set of all possible hypotheses that are consistent with the given examples. It is defined by the most specific and the most general hypotheses that are consistent with the examples, known as the lower and upper bound of the version space, respectively.
- Candidate elimination is an algorithm that maintains the version space by eliminating the hypotheses that are inconsistent with each new example. It outputs the lower and upper bound of the version space after each example.

## Inductive Bias

- Inductive bias is the set of assumptions that a learner uses to make predictions or generalizations from a finite set of data. It is necessary for learning because without any bias, the learner cannot prefer one hypothesis over another that is equally consistent with the data.
- Inductive bias can be explicit or implicit, depending on whether the learner explicitly states its assumptions or not. For example, decision tree learning has an implicit bias of preferring shorter and simpler trees over longer and more complex ones.
- Inductive bias can also be classified into two types: restriction bias and preference bias. Restriction bias limits the hypothesis space to a subset of all possible hypotheses, while preference bias orders or ranks the hypotheses within the hypothesis space. For example, candidate elimination has a restriction bias of eliminating inconsistent hypotheses, while decision tree learning has a preference bias of choosing the best attribute to split the data at each node.

## Types of Machine Learning

- Machine learning can be broadly categorized into three types: supervised learning, unsupervised learning, and reinforcement learning.
- Supervised learning is the type of machine learning where the learner is given a set of labeled examples, where each example consists of an input and a desired output, and the learner has to learn a function that maps the inputs to the outputs. The goal of supervised learning is to minimize the prediction error on new unseen examples. Examples of supervised learning are classification, regression, and ranking.
- Unsupervised learning is the type of machine learning where the learner is given a set of unlabeled examples, where each example consists of only an input, and the learner has to discover some structure or pattern in the data. The goal of unsupervised learning is to maximize the data representation or compression. Examples of unsupervised learning are clustering, dimensionality reduction, and anomaly detection.
- Reinforcement learning is the type of machine learning where the learner is not given any examples, but instead interacts with an environment and learns from its own actions and feedback. The goal of reinforcement learning is to maximize the cumulative reward over time. Examples of reinforcement learning are control, navigation, and game playing.

## Decision Tree Learning

- Decision tree learning is a supervised learning algorithm that learns a tree-like structure that represents a set of rules for classifying or predicting the output of a given input. Each node in the tree corresponds to a test on an attribute of the input, and each branch corresponds to a possible outcome of the test. Each leaf node