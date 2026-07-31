### Acceptance-Rejection Method

- The acceptance-rejection method is a technique for generating pseudorandom numbers from a target distribution, given a proposal distribution that is easy to sample from and that covers the target distribution.
- The basic idea is to generate a pair of random numbers, one from the proposal distribution and one from the uniform distribution, and accept the first one as a sample from the target distribution if it satisfies a certain condition, otherwise reject it and repeat the process.
- The condition is based on the ratio of the probability density functions (pdfs) of the target and proposal distributions, and a constant c that bounds this ratio from above.
- The algorithm is as follows:

  1. Choose a proposal distribution g(x) such that f(x) <= c g(x) for all x, where f(x) is the target distribution and c is a constant.
  2. Generate a random number u from the uniform distribution U(0,1) and a random number x from the proposal distribution g(x).
  3. If u <= f(x) / (c g(x)), accept x as a sample from f(x), otherwise reject x and go back to step 2.

- The acceptance-rejection method has the following properties:

  - The expected number of iterations to generate one sample is c, which is the inverse of the acceptance probability.
  - The efficiency of the method depends on the choice of c and g(x), which should be as close as possible to f(x) to minimize the rejection rate.
  - The method can be generalized to generate random numbers from multivariate distributions, using a proposal distribution that covers the target distribution in the multidimensional space.