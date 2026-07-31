### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram models in natural language processing.
- Smoothing is a technique to assign non-zero probabilities to unseen n-grams and reduce the probabilities of seen n-grams.
- Interpolation and backoff are based on the idea of using lower-order n-grams when higher-order n-grams are unreliable or sparse.
- Interpolation is a method that combines the probabilities of n-grams of different orders using some weights. For example, the probability of a trigram can be interpolated as:

$$
P(w_i|w_{i-2}w_{i-1}) = \lambda_1 P(w_i|w_{i-2}w_{i-1}) + \lambda_2 P(w_i|w_{i-1}) + \lambda_3 P(w_i)
$$

where $\lambda_1 + \lambda_2 + \lambda_3 = 1$ and $\lambda_i \geq 0$ for $i = 1, 2, 3$.

- The weights $\lambda_i$ can be estimated using various methods, such as maximum likelihood estimation, expectation-maximization, or cross-validation.
- Interpolation has the advantage of using all the available information from different n-gram orders, but it also requires more parameters and computation.
- Backoff is a method that uses a higher-order n-gram only if it has sufficient frequency or evidence, otherwise it backs off to a lower-order n-gram. For example, the probability of a trigram can be computed as:

$$
P(w_i|w_{i-2}w_{i-1}) = \begin{cases}
P^*(w_i|w_{i-2}w_{i-1}) & \text{if } C(w_{i-2}w_{i-1}w_i) > 0 \\
\alpha(w_{i-2}w_{i-1})P(w_i|w_{i-1}) & \text{otherwise}
\end{cases}
$$

where $P^*(w_i|w_{i-2}w_{i-1})$ is a discounted probability of the trigram, $C(w_{i-2}w_{i-1}w_i)$ is the count of the trigram, and $\alpha(w_{i-2}w_{i-1})$ is a scaling factor to ensure that the probabilities sum to one.
- Backoff has the advantage of being simpler and faster than interpolation, but it also discards some information from higher-order n-grams when backing off.
- In general, interpolation works better than backoff, but both methods are widely used in natural language processing applications.