### Optimum (Bayes) Statistical Classifiers

- Optimum (Bayes) statistical classifiers are classifiers that use the Bayes' theorem to make predictions based on the posterior probabilities of the classes given the features of a new example .
- The Bayes' theorem states that the posterior probability of a class C given a feature vector x is proportional to the product of the prior probability of the class P(C) and the likelihood of the feature vector given the class P(x|C):
  - P(C|x) ∝ P(C)P(x|C)
- The optimum (Bayes) classifier chooses the class that has the highest posterior probability for a given feature vector, i.e., the class that maximizes P(C|x). This is also known as the maximum a posteriori (MAP) estimation.
  - C* = argmax P(C|x)
- The optimum (Bayes) classifier is also called the Bayes optimal classifier, the Bayes optimal learner, the Bayes optimal decision boundary, or the Bayes optimal discriminant function .
- The optimum (Bayes) classifier is a theoretical model that assumes the true probabilities of the classes and the features are known or can be estimated from the training data. In practice, this is often not the case, and various approximation methods are used to implement the Bayes classifier, such as the naive Bayes classifier, the linear discriminant analysis, or the quadratic discriminant analysis .
- The optimum (Bayes) classifier is a useful benchmark for evaluating the performance of other classification methods, as it represents the lowest possible error rate that can be achieved for a given problem. The difference between the error rate of the optimum (Bayes) classifier and the error rate of another classifier is called the excess risk.