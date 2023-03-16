### Unit 3 - Pseudo-Random Numbers
#### Importance Sampling
- Importance sampling is a technique used in Monte Carlo methods to reduce the variance of the estimator.
- It is used when the probability density function (PDF) of the random variable being sampled is difficult or impossible to sample from directly.
- Instead, a different PDF, called the proposal distribution, is used to generate samples.
- The proposal distribution is chosen such that it is easy to sample from and is close to the target distribution.
- The samples generated from the proposal distribution are then reweighted according to the ratio of the target and proposal PDFs.
- This reweighting allows for the estimation of expectations with respect to the target distribution, even though the samples were generated from the proposal distribution.
- Importance sampling can significantly reduce the variance of the estimator, leading to more accurate results with fewer samples.
- It is commonly used in applications such as rare event simulation, Bayesian inference, and computational finance.