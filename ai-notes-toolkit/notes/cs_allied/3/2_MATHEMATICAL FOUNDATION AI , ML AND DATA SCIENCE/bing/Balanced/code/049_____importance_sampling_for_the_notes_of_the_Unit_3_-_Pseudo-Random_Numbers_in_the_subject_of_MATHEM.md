### Importance sampling

- Importance sampling is a **variance reduction technique** that can be used in the **Monte Carlo method**.
- The idea behind importance sampling is that certain values of the input random variables in a simulation have more impact on the parameter being estimated than others.
- Importance sampling can be used to evaluate properties of a particular distribution, while only having samples generated from a different distribution than the distribution of interest.
- The basic steps of importance sampling are:
  - Choose a **sampling distribution** that is easy to sample from and has a similar shape to the **target distribution**.
  - Generate **importance samples** from the sampling distribution and assign them **importance weights** based on the ratio of the target and sampling densities.
  - Compute the **weighted average** of the function values at the importance samples as an approximation of the expected value of the function under the target distribution.
- The advantages of importance sampling are:
  - It can reduce the variance of the Monte Carlo estimator by assigning more weight to the samples that are more relevant to the estimation problem.
  - It can handle situations where the target distribution is difficult or impossible to sample from directly, such as when it is unnormalized or has a complicated form.
  - It can improve the efficiency and accuracy of the Monte Carlo method for estimating rare events, tail probabilities, or integrals over small regions.
- The disadvantages of importance sampling are:
  - It requires a good choice of the sampling distribution, which can be challenging or impractical in some cases.
  - It can introduce a large bias or variance if the sampling distribution is too different from the target distribution, especially if it has a smaller support or lower tails.
  - It can be sensitive to outliers or extreme values that have very high or low importance weights, which can dominate or distort the estimation result.