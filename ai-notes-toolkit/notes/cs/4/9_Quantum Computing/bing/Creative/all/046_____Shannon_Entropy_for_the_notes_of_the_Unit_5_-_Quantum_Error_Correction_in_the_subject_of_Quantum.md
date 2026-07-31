# Shannon Entropy

Shannon entropy is a measure of the uncertainty and the information content in the state of a physical system. It is named after Claude Shannon, who introduced it in his 1948 paper "A Mathematical Theory of Communication" . Shannon entropy can be applied to both classical and quantum information theory, but with some differences and generalizations.

## Shannon entropy in classical information theory

In classical information theory, Shannon entropy quantifies the average amount of information that can be extracted from a random variable or a message source. It is defined as follows:

$$
H(X) = -\sum_{x \in \mathcal{X}} p(x) \log p(x)
$$

where $X$ is a discrete random variable with a finite or countable set of possible values $\mathcal{X}$, and $p(x)$ is the probability mass function of $X$. The logarithm can be taken with any base, but the most common choices are 2 (for bits), e (for nats), and 10 (for dits). The unit of Shannon entropy depends on the base of the logarithm.

Shannon entropy can be interpreted as the minimum number of bits (or other units) needed to encode the outcomes of $X$ on average, using an optimal code. It can also be seen as the expected value of the self-information or surprisal of $X$, which is defined as $I(x) = -\log p(x)$. The self-information measures how surprising or informative an outcome is, and it is higher for less probable outcomes.

Shannon entropy can also be used to measure the uncertainty or randomness of a system. A system with higher entropy has more possible states and less predictability, while a system with lower entropy has fewer possible states and more order. For example, a fair coin has higher entropy than a biased coin, and a uniform distribution has higher entropy than a peaked distribution.

Shannon entropy satisfies some important properties, such as:

- Non-negativity: $H(X) \geq 0$ for any $X$, and $H(X) = 0$ if and only if $X$ is a constant (i.e., $p(x) = 1$ for some $x \in \mathcal{X}$).
- Chain rule: $H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)$, where $H(X,Y)$ is the joint entropy of $X$ and $Y$, and $H(Y|X)$ is the conditional entropy of $Y$ given $X$.
- Subadditivity: $H(X,Y) \leq H(X) + H(Y)$, with equality if and only if $X$ and $Y$ are independent.
- Maximum entropy: $H(X) \leq \log |\mathcal{X}|$, with equality if and only if $X$ has a uniform distribution over $\mathcal{X}$.

Shannon entropy can be extended to continuous random variables by using differential entropy, which is defined as:

$$
h(X) = -\int_{\mathcal{X}} f(x) \log f(x) dx
$$

where $X$ is a continuous random variable with a probability density function $f(x)$ over a set $\mathcal{X}$. However, differential entropy is not invariant under changes of variables, and it can be negative. Therefore, it is not a true measure of information or uncertainty, and it should be used with caution.

## Shannon entropy in quantum information theory

In quantum information theory, Shannon entropy can be generalized to quantum systems, where the state of a system is described by a density matrix $\rho$ instead of a probability distribution. The quantum analogue of Shannon entropy is called von Neumann entropy, and it is defined as follows:

$$
S(\rho) = -\mathrm{Tr}(\rho \log \rho)
$$

where $\mathrm{Tr}$ denotes the trace operator, and the logarithm is taken in the matrix sense. The base of the logarithm can be chosen arbitrarily, but the most common choice is 2 (for qubits).

Von Neumann entropy can be interpreted as the average amount of information that can be extracted from a quantum system by performing a measurement on it. It can also be seen as the expected value of the quantum self-information or quantum surprisal of $\rho$, which is defined as $S(x) = -\log \rho_x$, where $\rho_x$ is the probability of obtaining the outcome $