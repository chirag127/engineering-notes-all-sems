 Here is the content in markdown format without any emojis or external links:

### Inverse-transform for the notes of the Unit 3 - Pseudo-Random Numbers

1. The inverse transform method is a technique for generating pseudo-random numbers with a desired probability distribution.
2. Given a continuous CDF (Cumulative Distribution Function) F(x), the inverse transform method works as follows:
 - Generate a uniform random number u from the range (0, 1)
 - Compute x = F−1(u) , where F−1 is the inverse of the CDF F
 - The random variable X with CDF F is simulated by generating x
3. The key advantage of this method is that it can be used to simulate random variables with any CDF for which the inverse can be computed.
4. However, the inverse transform method has some disadvantages:
 - It may be difficult or impossible to compute the inverse of the CDF for some distributions
 - Overflow and numerical precision issues can occur, especially for distributions with tails that decline slowly
 - It can be inefficient if many random variables need to be generated from the same distribution

The content is written in a formal tone with points and without any emojis or external links as required. Please let me know if you would like me to modify or expand the content in any way.