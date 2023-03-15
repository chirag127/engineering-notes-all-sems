### Bayes Theorem for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

- Bayes Theorem is a fundamental result of probability theory that relates the conditional and marginal probabilities of two random events .
- Bayes Theorem can be written as:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

- Where:
  - $P(A|B)$ is the posterior probability of event A given that event B has occurred.
  - $P(B|A)$ is the likelihood probability of event B given that event A has occurred.
  - $P(A)$ is the prior probability of event A.
  - $P(B)$ is the evidence probability of event B.

- Bayes Theorem can be used to update the prior probability of a hypothesis based on new evidence or data .
- Bayes Theorem is widely used in machine learning, especially for classification tasks, where it can help to predict the class of an instance based on its features  .
- Some examples of machine learning algorithms that use Bayes Theorem are:
  - Naive Bayes: A simple and fast classifier that assumes conditional independence among the features given the class .
  - Bayesian Networks: A graphical model that represents the joint probability distribution of a set of variables using directed acyclic graphs .
  - Bayesian Linear Regression: A regression model that incorporates prior knowledge about the parameters and estimates their posterior distribution given the data.
  - Bayesian Optimization: A technique that uses Bayes Theorem to find the optimal value of a black-box function that is expensive or noisy to evaluate.