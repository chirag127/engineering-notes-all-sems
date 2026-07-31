# Importance sampling

- Importance sampling is a **variance reduction technique** that can be used in the **Monte Carlo method**.
- The idea behind importance sampling is that certain values of the input random variables in a simulation have more impact on the parameter being estimated than others.
- Importance sampling can be used to **evaluate properties of a particular distribution**, while only having samples generated from a **different distribution** than the distribution of interest.
- Importance sampling can also be used when sampling from the distribution of interest is **difficult** or **impossible**.
- The basic idea of importance sampling is to sample the states from a different distribution to lower the variance of the estimation of **E[X;P]**, where **X** is a random variable of interest and **P** is the distribution of interest.
- This is accomplished by first choosing a random variable **L** such that **E[L;P] = 1** and that **L > 0** **P**-almost everywhere.
- Then, the expectation of **X** under **P** can be written as **E[X;P] = E[XL;P] = E[X/L;Q]E[L;P]**, where **Q** is the distribution of **L**.
- The last equality follows from the **law of total expectation**.
- The advantage of this approach is that the variance of **X/L** under **Q** may be much smaller than the variance of **X** under **P**, leading to a more accurate estimation.
- The choice of **Q** is crucial for the performance of importance sampling. A good choice of **Q** should satisfy the following criteria:
  - It should be **easy to sample** from **Q**.
  - It should be **easy to compute** the ratio **L = P/Q**.
  - It should have a **similar shape** to **P** in the regions where **X** is large.
  - It should have a **larger tail** than **P** in the regions where **X** is large.
- An example of importance sampling is the estimation of the probability of a rare event. Suppose we want to estimate the probability that a standard normal random variable **Z** is greater than 5, i.e., **P(Z > 5)**. This probability is very small, and sampling directly from the normal distribution would require a large number of samples to get a reliable estimate. However, we can use importance sampling by choosing a different distribution **Q** that has a larger tail than the normal distribution, such as an exponential distribution with mean 5. Then, we can sample **Z** from **Q** and compute the ratio **L = P/Q**, which is the density of the normal distribution divided by the density of the exponential distribution. The estimate of **P(Z > 5)** is then given by the average of **L** over the samples. This estimate will have a smaller variance than the direct sampling method, since the samples from **Q** are more likely to be in the region where **Z** is large.