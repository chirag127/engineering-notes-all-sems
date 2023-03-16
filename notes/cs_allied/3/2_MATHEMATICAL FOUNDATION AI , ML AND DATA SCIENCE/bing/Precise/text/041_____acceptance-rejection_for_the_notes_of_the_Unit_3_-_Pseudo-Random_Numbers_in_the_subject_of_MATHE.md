### Acceptance-Rejection

1. Acceptance-Rejection is a method for generating random numbers from a distribution.
2. It is also known as the Rejection Sampling method.
3. The method involves generating random numbers from a proposal distribution and then accepting or rejecting them based on a probability criterion.
4. The proposal distribution must be easy to sample from and its density function must be greater than or equal to the density function of the target distribution.
5. The acceptance probability is calculated as the ratio of the target density function to the proposal density function.
6. If the generated random number is accepted, it is considered a sample from the target distribution.
7. If it is rejected, the process is repeated until a sample is accepted.
8. This method can be used to generate random numbers from any distribution, provided that an appropriate proposal distribution can be found.
9. It is particularly useful for generating random numbers from complex or multi-modal distributions.
10. The efficiency of the method depends on the choice of the proposal distribution and the ratio of the target and proposal density functions. A good proposal distribution will result in a high acceptance rate and a low number of rejections.