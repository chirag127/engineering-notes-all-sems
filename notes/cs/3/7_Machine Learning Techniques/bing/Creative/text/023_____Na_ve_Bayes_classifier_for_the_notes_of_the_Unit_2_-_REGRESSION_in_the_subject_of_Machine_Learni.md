### Naïve Bayes classifier

- A naïve Bayes classifier is a probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions between the features.
- Bayes' theorem states that the conditional probability of a class label given a feature vector is proportional to the prior probability of the class label and the likelihood of the feature vector given the class label.
- Mathematically, P(C|F) = P(C)P(F|C)/P(F), where C is the class label, F is the feature vector, P(C) is the prior probability of C, P(F|C) is the likelihood of F given C, and P(F) is the evidence or marginal probability of F.
- A naïve Bayes classifier assumes that the features are conditionally independent given the class label, that is, P(F|C) = P(F1|C)P(F2|C)...P(Fn|C), where F1, F2, ..., Fn are the n features in F.
- This assumption simplifies the computation of the likelihood and reduces the number of parameters to estimate from the training data.
- A naïve Bayes classifier can handle both discrete and continuous features, depending on the distribution assumed for the likelihood. For example, a multinomial naïve Bayes classifier assumes that the features are discrete and follow a multinomial distribution, while a Gaussian naïve Bayes classifier assumes that the features are continuous and follow a normal distribution.
- A naïve Bayes classifier can be trained by estimating the prior and likelihood probabilities from the training data using maximum likelihood estimation or Bayesian estimation.
- A naïve Bayes classifier can be used to predict the most probable class label for a new feature vector by applying the Bayes' rule and choosing the class label that maximizes the posterior probability.
- A naïve Bayes classifier is a simple, fast, and effective technique for classification problems, especially for text and document classification. However, it may not perform well if the independence assumption is violated or if the features have strong correlations.