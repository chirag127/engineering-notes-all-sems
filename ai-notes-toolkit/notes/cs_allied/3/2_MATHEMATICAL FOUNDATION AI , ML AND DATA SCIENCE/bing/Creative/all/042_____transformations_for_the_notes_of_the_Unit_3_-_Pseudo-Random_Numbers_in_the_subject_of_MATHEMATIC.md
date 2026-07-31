# Transformations for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI, ML AND DATA SCIENCE

- A transformation is a method for generating pseudo-random numbers from a given probability distribution using a uniform pseudo-random number generator.
- A uniform pseudo-random number generator is a function that produces a sequence of numbers in the interval [0, 1] that are approximately independent and uniformly distributed.
- There are different types of transformations, such as:
  - The probability integral transform, which uses the inverse of the cumulative distribution function of the target distribution to map uniform pseudo-random numbers to the desired distribution.
  - The rejection method, which generates pseudo-random numbers from a proposal distribution and accepts or rejects them based on a criterion that ensures the desired distribution.
  - The convolution method, which generates pseudo-random numbers from the sum of independent pseudo-random numbers with known distributions.
  - The composition method, which generates pseudo-random numbers from a mixture of different distributions with known probabilities.
- Some examples of transformations are:
  - The linear congruential generator, which is a simple and widely used transformation for generating uniform pseudo-random numbers. It uses the recurrence relation: Xn+1 = (aXn + c) mod m, where Xn is the nth pseudo-random number, m is the modulus, a is the multiplier, c is the increment, and X0 is the seed.
  - The Box-Muller method, which is a transformation for generating pseudo-random numbers from the standard normal distribution. It uses two independent uniform pseudo-random numbers U1 and U2 and applies the formulas: Z1 = sqrt(-2 log U1) cos(2 pi U2) and Z2 = sqrt(-2 log U1) sin(2 pi U2), where Z1 and Z2 are two independent standard normal pseudo-random numbers.
  - The exponential distribution, which is a transformation for generating pseudo-random numbers from the exponential distribution with parameter lambda. It uses the probability integral transform and applies the formula: X = -log U / lambda, where U is a uniform pseudo-random number and X is an exponential pseudo-random number.