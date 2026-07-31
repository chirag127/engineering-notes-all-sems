# Transformations for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI, ML AND DATA SCIENCE

1. **Linear Congruential Generator (LCG)**: This is a method of generating a sequence of pseudo-random numbers. It is defined by the recurrence relation Xn+1 = (aXn + c) mod m, where X is the sequence of pseudo-random numbers, and a, c, and m are integer constants.

2. **Inverse Transform Method**: This method generates random numbers from a given distribution by using its inverse cumulative distribution function (CDF). The basic idea is to generate a random number from a uniform distribution and then transform it using the inverse CDF of the desired distribution.

3. **Acceptance-Rejection Method**: This method generates random numbers from a given distribution by generating random numbers from another distribution and then accepting or rejecting them based on a certain criterion. The basic idea is to generate random numbers from a proposal distribution and then accept them with a probability equal to the ratio of the desired distribution to the proposal distribution.

4. **Box-Muller Transform**: This method generates pairs of independent standard normally distributed random numbers. The basic idea is to generate two independent random numbers from a uniform distribution and then transform them into two independent standard normally distributed random numbers using a mathematical formula.

5. **Marsaglia Polar Method**: This method is similar to the Box-Muller transform, but it uses a different mathematical formula to generate pairs of independent standard normally distributed random numbers. It is also known as the polar method.

6. **Ziggurat Algorithm**: This method generates random numbers from a given distribution by dividing the area under the probability density function (PDF) into several horizontal layers and then generating random numbers within each layer. The basic idea is to generate a random number from a uniform distribution and then use it to select a layer and generate a random number within that layer.
