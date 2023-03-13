### Shannon Entropy

- Shannon entropy is a measure of the uncertainty or randomness of a random variable.
- It quantifies the average amount of information that can be obtained from observing the outcome of the random variable.
- It is defined as:

$$
H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)
$$

where $X$ is the random variable, $\mathcal{X}$ is the set of possible values of $X$, and $p(x)$ is the probability of $X$ taking the value $x$.
- Shannon entropy has the following properties:
  - It is non-negative: $H(X) \geq 0$ for any $X$.
  - It is zero if and only if $X$ is deterministic: $H(X) = 0$ if and only if there exists a $x_0 \in \mathcal{X}$ such that $p(x_0) = 1$ and $p(x) = 0$ for all $x \neq x_0$.
  - It is maximized when $X$ is uniformly distributed: $H(X) \leq \log_2 |\mathcal{X}|$ for any $X$, and the equality holds if and only if $p(x) = \frac{1}{|\mathcal{X}|}$ for all $x \in \mathcal{X}$.
  - It is additive for independent random variables: $H(X, Y) = H(X) + H(Y)$ if $X$ and $Y$ are independent, where $H(X, Y)$ is the joint entropy of $X$ and $Y$.
  - It is subadditive for dependent random variables: $H(X, Y) \leq H(X) + H(Y)$ for any $X$ and $Y$, where $H(X, Y)$ is the joint entropy of $X$ and $Y$.
  - It satisfies the chain rule: $H(X, Y) = H(X) + H(Y | X) = H(Y) + H(X | Y)$, where $H(Y | X)$ is the conditional entropy of $Y$ given $X$, and $H(X | Y)$ is the conditional entropy of $X$ given $Y$.
- Shannon entropy can be used to measure the amount of information that can be transmitted or stored by a communication channel or a memory device.
- It can also be used to measure the amount of information that can be extracted or learned from a data set or a statistical model.
- Shannon entropy is related to the concept of entropy in thermodynamics, which measures the disorder or randomness of a physical system.
- However, Shannon entropy is a purely mathematical and information-theoretic concept, and does not depend on the physical nature or interpretation of the random variable.