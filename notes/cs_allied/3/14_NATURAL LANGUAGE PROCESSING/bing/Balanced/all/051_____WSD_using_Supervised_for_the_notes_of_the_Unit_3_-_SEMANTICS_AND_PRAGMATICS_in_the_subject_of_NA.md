# WSD using Supervised

- Word Sense Disambiguation (WSD) is the task of identifying the correct meaning of a word in a given context, when the word has multiple possible meanings (i.e., it is ambiguous).
- Supervised WSD methods use manually sense-annotated corpora to train machine learning models that can classify the sense of a word based on its context.
- The advantages of supervised WSD methods are that they can achieve high accuracy and can handle fine-grained senses.
- The disadvantages of supervised WSD methods are that they require a lot of human effort to create sense-annotated corpora, and that they are limited by the coverage and quality of the available sense inventories (e.g., WordNet).
- Some examples of supervised WSD methods are:
  - Naive Bayes: A probabilistic model that assigns the most likely sense to a word based on the frequency of its co-occurring words in the training data. 
  - Support Vector Machines (SVMs): A linear model that finds the optimal hyperplane that separates the different sense classes in a high-dimensional feature space. 
  - Neural Networks: A nonlinear model that learns complex representations of the input features and can capture semantic and syntactic dependencies in the context.