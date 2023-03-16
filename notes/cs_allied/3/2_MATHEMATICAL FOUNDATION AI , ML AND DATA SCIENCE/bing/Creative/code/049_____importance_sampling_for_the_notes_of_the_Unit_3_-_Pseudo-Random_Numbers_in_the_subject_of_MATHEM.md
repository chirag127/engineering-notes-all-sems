### Importance sampling

Importance sampling is a technique that can be used to estimate the expected value of a function of a random variable, or the probability of an event, by using samples from a different distribution than the original one. It can be useful when:

- The original distribution is difficult or impossible to sample from.
- The original distribution has a high variance or a heavy tail, which means that many samples are needed to get a good approximation.
- The function or the event of interest is rare or has a low probability under the original distribution, which means that most samples are irrelevant or have a negligible contribution.

The basic idea of importance sampling is to choose a sampling distribution that is easy to sample from, and that assigns more weight or probability to the regions where the function or the event of interest is large or likely. Then, the samples from the sampling distribution are weighted by a ratio of the original distribution and the sampling distribution, which is called the importance weight. The weighted samples are used to estimate the expected value or the probability of interest.

The formula for importance sampling is:

$$\mathbb{E}_{X \sim P}[f(X)] = \mathbb{E}_{X \sim Q} \left[ \frac{P(X)}{Q(X)} f(X) \right]$$

where $P$ is the original distribution, $Q$ is the sampling distribution, and $f$ is the function of interest.

The formula for estimating the probability of an event $A$ using importance sampling is:

$$\mathbb{P}_{X \sim P}(A) = \mathbb{E}_{X \sim Q} \left[ \frac{P(X)}{Q(X)} \mathbb{I}(A) \right]$$

where $\mathbb{I}(A)$ is the indicator function that is 1 if $X$ belongs to $A$ and 0 otherwise.

The advantages of importance sampling are:

- It can reduce the variance of the estimator, which means that fewer samples are needed to achieve a given accuracy.
- It can handle rare events or functions that are zero almost everywhere, which would otherwise require a large number of samples to observe.

The disadvantages of importance sampling are:

- It requires choosing a good sampling distribution that is close to the original distribution in the regions of interest, and that is easy to sample from and evaluate. This can be challenging or impossible in some cases.
- It can introduce a large bias or error if the sampling distribution is not well chosen, or if the importance weights are very large or very small. This can lead to unreliable or inaccurate estimates.