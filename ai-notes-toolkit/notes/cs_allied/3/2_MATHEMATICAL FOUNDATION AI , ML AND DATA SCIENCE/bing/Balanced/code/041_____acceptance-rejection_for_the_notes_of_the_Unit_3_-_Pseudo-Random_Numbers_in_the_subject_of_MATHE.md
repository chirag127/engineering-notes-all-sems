### Acceptance-Rejection Method for Pseudo-Random Numbers

- The acceptance-rejection method is a technique for generating pseudo-random numbers from a target distribution, given a proposal distribution that is easy to sample from and that covers the target distribution.
- The basic idea is to generate a pair of random numbers, one from the proposal distribution and one from a uniform distribution, and then accept or reject the first number based on the second number and a comparison function.
- The comparison function is usually the ratio of the target density and the proposal density, scaled by a constant factor that ensures the ratio is always less than or equal to one.
- The algorithm is as follows:

  1. Choose a proposal distribution with density or pmf g and a constant c such that f(x) <= c g(x) for all x, where f is the target density or pmf.
  2. Generate a random number X from the proposal distribution and a random number U from the uniform distribution on [0, 1].
  3. If U <= f(X) / (c g(X)), accept X as a sample from the target distribution. Otherwise, reject X and repeat from step 2.

- The acceptance-rejection method produces an empirical distribution of pseudo-random numbers that converges the most rapidly to the target distribution if the constant c is chosen to be the maximum possible value of f(x) / g(x) over the common support of f and g.
- The acceptance-rejection method can be used to generate pseudo-random numbers from various distributions, such as exponential, normal, gamma, beta, etc., by choosing appropriate proposal distributions, such as uniform, exponential, etc.  .