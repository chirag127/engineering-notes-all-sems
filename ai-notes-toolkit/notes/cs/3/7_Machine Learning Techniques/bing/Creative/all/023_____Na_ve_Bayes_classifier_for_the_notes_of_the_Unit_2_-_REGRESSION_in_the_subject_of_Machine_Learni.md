# Naïve Bayes classifier

- A naïve Bayes classifier is a type of probabilistic classifier that applies Bayes' theorem with strong (naïve) independence assumptions between the features.
- Bayes' theorem states that the conditional probability of a class label given a feature vector is proportional to the prior probability of the class label and the likelihood of the feature vector given the class label.
- Mathematically, the naïve Bayes classifier can be written as:

$$P(C_k \mid x) = \frac{P(C_k) P(x \mid C_k)}{P(x)}$$

where $C_k$ is the class label, $x$ is the feature vector, $P(C_k)$ is the prior probability of the class label, $P(x \mid C_k)$ is the likelihood of the feature vector given the class label, and $P(x)$ is the evidence or marginal probability of the feature vector .

- The naïve Bayes classifier makes the simplifying assumption that the features are conditionally independent given the class label, which means that the likelihood can be factorized as:

$$P(x \mid C_k) = \prod_{i=1}^n P(x_i \mid C_k)$$

where $n$ is the number of features and $x_i$ is the $i$-th feature .

- The naïve Bayes classifier can handle different types of features, such as categorical, binary, or continuous, by using different models for the likelihood term, such as multinomial, Bernoulli, or Gaussian distributions .
- The naïve Bayes classifier can be trained by estimating the prior and likelihood probabilities from the training data, using methods such as maximum likelihood estimation or Bayesian estimation .
- The naïve Bayes classifier can be used for various classification tasks, such as text classification, spam filtering, sentiment analysis, document categorization, etc  .
- The naïve Bayes classifier has several advantages, such as simplicity, efficiency, scalability, and robustness to noise and irrelevant features  .
- The naïve Bayes classifier also has some limitations, such as the unrealistic independence assumption, the sensitivity to zero-frequency problems, and the inability to capture feature interactions and dependencies  .