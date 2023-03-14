### Shannon Entropy

Shannon entropy is a measure of the uncertainty and the information content in the state of a physical system. It is named after Claude Shannon, who introduced it in his seminal paper "A Mathematical Theory of Communication" in 1948. Shannon entropy quantifies the average amount of information that can be extracted from a random variable or a message source.

Shannon entropy is defined as follows:

$$
H(X) = -\sum_{x \in \mathcal{X}} p(x) \log p(x),
$$

where $X$ is a discrete random variable with a finite or countable alphabet $\mathcal{X}$, and $p(x)$ is the probability mass function of $X$. The logarithm can be taken with any base, but the most common choices are base 2 (bits), base e (nats), or base 10 (dits). The unit of Shannon entropy depends on the base of the logarithm.

Shannon entropy has several important properties:

- It is non-negative: $H(X) \geq 0$ for any $X$.
- It is bounded: $0 \leq H(X) \leq \log |\mathcal{X}|$ for any $X$, where $|\mathcal{X}|$ is the size of the alphabet. The lower bound is attained when $X$ is a constant, and the upper bound is attained when $X$ is uniformly distributed over $\mathcal{X}$.
- It is invariant under permutations: $H(X) = H(f(X))$ for any bijective function $f$.
- It is additive for independent random variables: $H(X,Y) = H(X) + H(Y)$ if $X$ and $Y$ are independent.
- It is subadditive for any random variables: $H(X,Y) \leq H(X) + H(Y)$, with equality if and only if $X$ and $Y$ are independent.
- It is concave: $H(\lambda X + (1-\lambda) Y) \geq \lambda H(X) + (1-\lambda) H(Y)$ for any $0 \leq \lambda \leq 1$ and any random variables $X$ and $Y$.

Shannon entropy can be interpreted as the minimum number of bits (or other units) needed to encode the outcomes of $X$ on average, using an optimal code. It can also be seen as the expected value of the self-information or surprisal of $X$, which is defined as $I(x) = -\log p(x)$ for each outcome $x$. The self-information measures how surprising or informative an outcome is, and the Shannon entropy measures the average surprise or information of the source.

Shannon entropy can be generalized to continuous random variables, using differential entropy, or to joint or conditional random variables, using joint entropy or conditional entropy. It can also be extended to measure the mutual information or the relative entropy between two random variables, which quantify the amount of information that one variable reveals about another, or the distance between two probability distributions, respectively.

Shannon entropy is a central concept in classical information theory, which studies the fundamental limits and optimal methods of communication, compression, encryption, and inference of information. Shannon entropy has many applications in various fields, such as cryptography, data compression, statistical physics, thermodynamics, complexity theory, machine learning, and artificial intelligence.