# Naïve Bayes classifier

- A naïve Bayes classifier is a type of probabilistic classifier that applies Bayes' theorem with strong (naïve) independence assumptions between the features.
- Bayes' theorem states that the conditional probability of a class label given a feature vector is proportional to the prior probability of the class label and the likelihood of the feature vector given the class label.
- Mathematically, the naïve Bayes classifier can be expressed as:

$$P(C_k \mid x) = \frac{P(C_k) P(x \mid C_k)}{P(x)}$$

where $C_k$ is a class label, $x$ is a feature vector, $P(C_k)$ is the prior probability of $C_k$, $P(x \mid C_k)$ is the likelihood of $x$ given $C_k$, and $P(x)$ is the evidence or marginal probability of $x$.

- The naïve Bayes classifier makes the simplifying assumption that the features are conditionally independent given the class label, i.e., $P(x \mid C_k) = P(x_1 \mid C_k) P(x_2 \mid C_k) \cdots P(x_n \mid C_k)$, where $x_i$ is the $i$-th feature in $x$.
- This assumption reduces the computational complexity and data requirements of the classifier, but may also introduce some errors if the features are not truly independent.
- The naïve Bayes classifier can be applied to different types of data by choosing an appropriate likelihood function for each feature. Some common types of naïve Bayes classifiers are:

  - **Gaussian naïve Bayes**: Assumes that the features are normally distributed given the class label, i.e., $P(x_i \mid C_k) = \frac{1}{\sqrt{2 \pi \sigma_{k,i}^2}} \exp \left( - \frac{(x_i - \mu_{k,i})^2}{2 \sigma_{k,i}^2} \right)$, where $\mu_{k,i}$ and $\sigma_{k,i}$ are the mean and standard deviation of the $i$-th feature in class $k$.
  - **Multinomial naïve Bayes**: Assumes that the features are discrete counts of events or words, i.e., $P(x_i \mid C_k) = \frac{N_{k,i} + \alpha}{N_k + \alpha n}$, where $N_{k,i}$ is the number of times the $i$-th feature occurs in class $k$, $N_k$ is the total number of features in class $k$, $n$ is the number of possible values for each feature, and $\alpha$ is a smoothing parameter to avoid zero probabilities.
  - **Bernoulli naïve Bayes**: Assumes that the features are binary indicators of the presence or absence of events or words, i.e., $P(x_i \mid C_k) = p_{k,i}^{x_i} (1 - p_{k,i})^{(1 - x_i)}$, where $p_{k,i}$ is the probability of the $i$-th feature being 1 in class $k$.

- The naïve Bayes classifier can be trained by estimating the prior and likelihood probabilities from the training data using maximum likelihood estimation or Bayesian estimation methods.
- The naïve Bayes classifier can be used to predict the class label of a new feature vector by choosing the class label that maximizes the posterior probability, i.e., $\hat{C} = \arg \max_k P(C_k \mid x)$.
- The naïve Bayes classifier is a simple and efficient technique for classification problems, especially for text and document classification. It can handle large-scale and high-dimensional data with ease and speed. However, it may not perform well if the independence assumption is violated or if the data is not well represented by the chosen likelihood function.