### Acceptance-Rejection Method

- The acceptance-rejection method is a technique for generating pseudorandom numbers from a target distribution, given a proposal distribution that is easy to sample from and that covers the target distribution.
- The basic idea is to generate a pair of random numbers, one from the proposal distribution and one from a uniform distribution, and accept the first one as a sample from the target distribution if it satisfies a certain criterion, otherwise reject it and repeat the process.
- The criterion is based on comparing the ratio of the target density and the proposal density with the uniform random number, which acts as a threshold. The higher the ratio, the more likely the sample is to be accepted.
- The acceptance-rejection method requires a constant c such that f(x)/g(x) <= c for all x, where f and g are the target and proposal densities, respectively. The constant c determines the efficiency of the method, as the expected number of trials to obtain one accepted sample is c. Therefore, it is desirable to choose c as small as possible, ideally equal to the maximum value of f(x)/g(x).
- The acceptance-rejection method can be summarized as follows:

  1. Generate a random number U from the uniform distribution on [0,1].
  2. Generate a random number X from the proposal distribution with density g(x).
  3. Compute the ratio r = f(X)/g(X), where f(x) is the target density.
  4. If U <= r/c, accept X as a sample from the target distribution, otherwise reject X and go back to step 1.

- The acceptance-rejection method can be used to generate random numbers from various distributions, such as exponential, normal, gamma, beta, etc., by choosing appropriate proposal distributions, such as uniform, exponential, normal, etc.