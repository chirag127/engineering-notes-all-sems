Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Markov inequality for the notes of the Unit 1 - Descriptive Statistics in the subject of Mathematical Foundation AI, ML and Data Science.

### Markov inequality

- Markov inequality is a mathematical theorem that gives an upper bound on the probability that a non-negative random variable is greater than or equal to some positive constant.
- Formally, if X is a non-negative random variable and a > 0 is a positive constant, then Markov inequality states that:

$$
P(X \geq a) \leq \frac{E[X]}{a}
$$

- where E[X] is the expected value or mean of X.
- Markov inequality can be used to estimate the tail probabilities of a distribution, that is, the probabilities of rare or extreme events.
- Markov inequality is also known as the first moment inequality, because it only involves the first moment or mean of the distribution.
- Markov inequality is a general and simple result, but it is often not very tight or informative. For example, it does not depend on the variance or higher moments of the distribution, and it does not take into account the shape or symmetry of the distribution.
- Markov inequality can be derived from the definition of expected value and the property that a non-negative random variable is always greater than or equal to zero. The proof is as follows:

$$
\begin{aligned}
E[X] &= \sum_{x \geq 0} x P(X = x) \quad \text{(by definition of expected value)} \\
&\geq \sum_{x \geq a} x P(X = x) \quad \text{(by discarding the terms where } x < a) \\
&\geq \sum_{x \geq a} a P(X = x) \quad \text{(by replacing } x \text{ with } a \text{ in the summation)} \\
&= a \sum_{x \geq a} P(X = x) \quad \text{(by factoring out } a) \\
&= a P(X \geq a) \quad \text{(by definition of probability)} \\
\end{aligned}
$$

- Dividing both sides by a, we get:

$$
P(X \geq a) \leq \frac{E[X]}{a}
$$

- which is the Markov inequality.