### Random Number Generation

Random number generation is a process of generating a sequence of numbers that cannot be predicted better than by random chance. In the context of Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI, ML, AND DATA SCIENCE, we will be discussing Pseudo-Random Number Generators (PRNGs).

- PRNGs refer to an algorithm that uses mathematical formulas to produce sequences of random numbers .
- PRNGs generate a sequence of numbers approximating the properties of random numbers .
- A PRNG starts from an arbitrary starting state using a seed state .
- One of the most commonly used PRNGs is the Linear Congruential Generator (LCG)   .
- The LCG is defined by the recurrence relation: Xn+1 = (aXn + c) mod m where X is the sequence of pseudo-random values, m is the modulus, a is the multiplier, c is the increment, and x0 is the seed or start value .
- Compared to True Random Number Generators, PRNGs can be generated with very fast calculations, are easier to debug and test due to their cyclic nature, require low memory, and do not require external hardware. This makes PRNGs cost-efficient and scalable .
