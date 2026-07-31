### Transformations for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI, ML AND DATA SCIENCE

1. **Linear Congruential Generators (LCGs)**: These are a class of pseudorandom number generators that use a linear equation to generate a sequence of pseudorandom numbers. The equation is of the form Xn+1 = (aXn + c) mod m, where Xn is the nth number in the sequence, a, c, and m are constants, and mod is the modulo operator.

2. **Inverse Transform Method**: This method is used to generate random numbers from a non-uniform distribution. It involves computing the inverse of the cumulative distribution function (CDF) of the desired distribution and using it to transform uniformly distributed random numbers into random numbers from the desired distribution.

3. **Acceptance-Rejection Method**: This method is used to generate random numbers from a distribution that is difficult to sample from directly. It involves generating random numbers from a simpler distribution and then accepting or rejecting them based on a comparison with the desired distribution.

4. **Box-Muller Transform**: This method is used to generate pairs of independent, standard normally distributed random numbers. It involves generating two uniformly distributed random numbers and then transforming them into two normally distributed random numbers using a mathematical formula.

5. **Marsaglia's Polar Method**: This is an alternative to the Box-Muller transform for generating pairs of independent, standard normally distributed random numbers. It involves generating pairs of uniformly distributed random numbers and then transforming them into normally distributed random numbers using a different mathematical formula.

6. **Ziggurat Algorithm**: This is an efficient method for generating random numbers from a normal distribution. It involves dividing the area under the normal distribution curve into a series of horizontal slices and then using a combination of uniform random numbers and precomputed values to generate normally distributed random numbers.

7. **Mersenne Twister**: This is a widely used pseudorandom number generator that generates high-quality random numbers with a long period. It is based on a matrix linear recurrence over a finite binary field and is designed to pass various statistical tests for randomness.

These are some of the common transformations used in the generation of pseudo-random numbers in the field of AI, ML, and Data Science. It is important to understand these methods and their properties in order to effectively generate and use random numbers in these fields.