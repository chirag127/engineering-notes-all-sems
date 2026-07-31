### Importance sampling

- Importance sampling is a **variance reduction technique** that can be used in the **Monte Carlo method**.
- The idea behind importance sampling is that certain values of the input random variables in a simulation have more impact on the parameter being estimated than others.
- Importance sampling can be used to evaluate properties of a particular distribution, while only having samples generated from a different distribution than the distribution of interest.
- The basic idea of importance sampling is to sample the states from a different distribution to lower the variance of the estimation of E[X;P], or when sampling from P is difficult.
- This is accomplished by first choosing a random variable L such that E[L;P] = 1 and that L > 0 P-almost everywhere.
- Then, the expectation of interest can be written as E[X;P] = E[XL;P] = E[X/L;Q], where Q is the distribution of L.
- The last equality follows from the fact that E[XL;P] = E[XL/L;Q] = E[X/L;Q], since L is independent of X.
- The distribution Q is called the **importance sampling distribution** and the ratio L = P/Q is called the **importance sampling ratio**.
- The advantage of importance sampling is that it can reduce the variance of the estimator by choosing a Q that is more concentrated around the values of X that contribute more to the expectation.
- The disadvantage of importance sampling is that it can introduce a large bias if the Q is not chosen carefully or if the sample size is too small.
- Importance sampling can be applied to various problems, such as estimating rare event probabilities, computing tail probabilities, evaluating integrals, and estimating posterior distributions .

: Importance sampling - Wikipedia
: Importance Sampling - University of Michigan
: Importance sampling | Explanation, formulae, example - Statlect