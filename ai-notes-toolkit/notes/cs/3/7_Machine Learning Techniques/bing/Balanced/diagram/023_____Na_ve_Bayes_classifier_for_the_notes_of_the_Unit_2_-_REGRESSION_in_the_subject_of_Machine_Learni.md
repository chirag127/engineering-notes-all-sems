### Naïve Bayes classifier

- A naïve Bayes classifier is a probabilistic classifier based on applying Bayes' theorem with strong (naive) independence assumptions between the features.
- Bayes' theorem states that the conditional probability of a class label given a feature vector is proportional to the prior probability of the class label and the likelihood of the feature vector given the class label.
- Mathematically, P(C|F) = P(C)P(F|C)/P(F), where C is the class label, F is the feature vector, P(C) is the prior probability of C, P(F|C) is the likelihood of F given C, and P(F) is the evidence or marginal probability of F.
- A naïve Bayes classifier assumes that the features are conditionally independent given the class label, that is, P(F|C) = P(F1|C)P(F2|C)...P(Fn|C), where F1, F2, ..., Fn are the individual features in F.
- This assumption simplifies the computation of P(F|C) and reduces the number of parameters to estimate from the training data.
- A naïve Bayes classifier can handle different types of features, such as binary, categorical, or continuous, by using different models for the likelihood term, such as Bernoulli, multinomial, or Gaussian.
- A naïve Bayes classifier can be trained by estimating the prior and likelihood probabilities from the frequency counts of the class labels and feature values in the training data.
- A naïve Bayes classifier can be used to predict the most probable class label for a new feature vector by applying the maximum a posteriori (MAP) rule, that is, C* = argmax C P(C|F) = argmax C P(C)P(F|C).
- A naïve Bayes classifier is a simple, fast, and effective technique for classification problems, especially for text and document classification. However, it may not perform well when the independence assumption is violated or when the features have high correlation.