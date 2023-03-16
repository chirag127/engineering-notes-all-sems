### Markov Inequality

- Markov inequality is a mathematical result that gives an upper bound on the probability that a non-negative random variable exceeds a certain value.
- Markov inequality can be stated as follows: Let X be a non-negative random variable and a be a positive constant. Then, P(X >= a) <= E(X) / a, where E(X) is the expected value of X.
- Markov inequality can be used to derive other inequalities, such as Chebyshev's inequality and Chernoff's bound, by applying suitable transformations to the random variable X.
- Markov inequality can be proved by using the definition of expected value and the indicator function. The proof is as follows:

  - Let I be the indicator function of the event {X >= a}, i.e., I = 1 if X >= a and I = 0 otherwise. Then, E(I) = P(X >= a).
  - Since X is non-negative, we have X >= XI for all values of X. Taking the expected value of both sides, we get E(X) >= E(XI).
  - By the linearity of expectation, we have E(XI) = E(X)E(I) = E(X)P(X >= a).
  - Dividing both sides by E(X), we get P(X >= a) <= E(X) / a, which is the Markov inequality.