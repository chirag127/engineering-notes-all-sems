### Acceptance-Rejection

The acceptance-rejection method is a technique used to generate random numbers from a distribution. It is a part of Unit 3 - Pseudo-Random Numbers in the subject of Mathematical Foundation AI, ML and Data Science. Here are some key points to remember about the acceptance-rejection method:

1. The acceptance-rejection method is used to generate random numbers from a target distribution, given a proposal distribution that is easy to sample from.
2. The proposal distribution must have a larger support than the target distribution, meaning that it must be possible to generate all values from the target distribution using the proposal distribution.
3. The acceptance-rejection method involves generating a random number from the proposal distribution and then accepting or rejecting it based on a comparison with the target distribution.
4. The acceptance probability is calculated as the ratio of the target distribution to the proposal distribution, evaluated at the generated random number.
5. If the generated random number is accepted, it is considered a sample from the target distribution. If it is rejected, the process is repeated until a random number is accepted.
6. The acceptance-rejection method can be computationally expensive if the acceptance probability is low, as many random numbers may need to be generated before one is accepted.
