### Binomial Distribution

- A binomial distribution is a type of probability distribution that models the number of successes and failures in a fixed number of independent and identical trials, each with the same probability of success .
- A binomial distribution can be represented by the following formula:

![Binomial formula](https://latex.codecogs.com/png.latex?P%28X%3Dx%29%3D%5Cbinom%7Bn%7D%7Bx%7Dp%5Ex%281-p%29%5E%7Bn-x%7D)

where:

  - X is the random variable that counts the number of successes in n trials
  - x is a specific value of X, ranging from 0 to n
  - n is the number of trials
  - p is the probability of success in each trial
  - 1-p is the probability of failure in each trial
  - P(X=x) is the probability of getting exactly x successes in n trials
  - ![Binomial coefficient](https://latex.codecogs.com/png.latex?%5Cbinom%7Bn%7D%7Bx%7D) is the binomial coefficient, which is the number of ways to choose x objects from n objects, given by:

![Binomial coefficient formula](https://latex.codecogs.com/png.latex?%5Cbinom%7Bn%7D%7Bx%7D%3D%5Cfrac%7Bn%21%7D%7Bx%21%28n-x%29%21%7D)

- A binomial distribution has two parameters: n and p. The mean and variance of a binomial distribution are given by:

![Binomial mean and variance](https://latex.codecogs.com/png.latex?%5Cmu%3DE%28X%29%3Dnp%5Cquad%5Csigma%5E2%3DVar%28X%29%3Dnp%281-p%29)

- A binomial distribution can be approximated by a normal distribution when n is large and p is not too close to 0 or 1. The normal approximation is given by:

![Normal approximation](https://latex.codecogs.com/png.latex?X%5Csim%20N%28np%2Cnp%281-p%29%29)

- A binomial distribution can be used to model various real-world scenarios, such as:

  - The number of heads in a series of coin tosses
  - The number of defective items in a batch of products
  - The number of patients who recover from a disease after a treatment
  - The number of voters who prefer a certain candidate in an election