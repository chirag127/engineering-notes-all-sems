### Transformations for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI, ML AND DATA SCIENCE

1. **Linear Congruential Generator (LCG)**: This is a method of generating a sequence of pseudo-random numbers. It is defined by the recurrence relation: Xn+1 = (aXn + c) mod m, where X is the sequence of pseudo-random numbers, and a, c, and m are integer constants.

2. **Inverse Transform Method**: This method generates random numbers from a given distribution by using its inverse cumulative distribution function (CDF). The basic idea is to generate a random number from a uniform distribution and then use the inverse CDF to transform it into a random number from the desired distribution.

3. **Acceptance-Rejection Method**: This method generates random numbers from a given distribution by generating random numbers from another distribution and then accepting or rejecting them based on a certain criterion. The basic idea is to find a distribution that is easy to sample from and that "covers" the desired distribution, and then use it to generate random numbers.

4. **Box-Muller Transform**: This method generates pairs of independent standard normally distributed random numbers by using two independent uniformly distributed random numbers. The basic idea is to use the polar coordinates representation of a two-dimensional normal distribution to generate the random numbers.

5. **Marsaglia's Polar Method**: This is a variation of the Box-Muller transform that generates pairs of independent standard normally distributed random numbers by using two independent uniformly distributed random numbers. The basic idea is similar to the Box-Muller transform, but it uses a different approach to generate the random numbers.

6. **Ziggurat Algorithm**: This is an efficient method for generating random numbers from a given distribution by using a table of precomputed values. The basic idea is to divide the distribution into several layers, each of which can be sampled efficiently, and then use a combination of these layers to generate the random numbers.

These are some of the common transformations used in the generation of pseudo-random numbers in the field of AI, ML, and Data Science. It is important to understand these methods and their underlying principles to effectively generate and use pseudo-random numbers in various applications.