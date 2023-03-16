# Acceptance-Rejection Method for Pseudo-Random Numbers

- The acceptance-rejection method is a technique for generating pseudo-random numbers from a target distribution, given a proposal distribution that is easy to sample from and that covers the target distribution.
- The basic idea is to generate a pair of random numbers, one from the proposal distribution and one from a uniform distribution, and then accept or reject the first number based on a comparison with the second number and the ratio of the target and proposal densities.
- The algorithm is as follows:

  1. Choose a proposal distribution with density or pmf $g$ and a constant $c$ such that $f(x) \leq c g(x)$ for all $x$, where $f$ is the target density or pmf.
  2. Generate a random number $Y$ from the proposal distribution and a random number $U$ from the uniform distribution on $[0,1]$.
  3. If $U \leq \frac{f(Y)}{c g(Y)}$, accept $Y$ as a sample from the target distribution. Otherwise, reject $Y$ and repeat the process.

- The acceptance-rejection method produces an empirical distribution of pseudo-random numbers that converges the most rapidly to the target distribution if $c$ is chosen to be the maximum possible value of $\frac{f(x)}{g(x)}$ over the common support of $f$ and $g$.
- The acceptance-rejection method can be used to generate pseudo-random numbers from various distributions, such as exponential, normal, gamma, beta, etc., by choosing appropriate proposal distributions, such as uniform, exponential, normal, etc.  .