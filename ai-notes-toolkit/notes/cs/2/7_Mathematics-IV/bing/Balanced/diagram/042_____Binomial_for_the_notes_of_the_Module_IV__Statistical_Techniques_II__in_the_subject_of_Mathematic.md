### Binomial Distribution

- Binomial distribution is a type of probability distribution that describes the possible outcomes of a series of independent trials, where each trial has only two possible outcomes, such as success or failure, yes or no, heads or tails, etc.
- Binomial distribution is defined by two parameters: the number of trials (n) and the probability of success (p) in each trial. The probability of getting exactly x successes in n trials is given by the formula:

![Binomial formula](https://latex.codecogs.com/png.latex?P%28X%3Dx%29%3D%5Cbinom%7Bn%7D%7Bx%7Dp%5Ex%281-p%29%5E%7Bn-x%7D)

where ![Binomial coefficient](https://latex.codecogs.com/png.latex?%5Cbinom%7Bn%7D%7Bx%7D) is the binomial coefficient, which is equal to ![Binomial coefficient formula](https://latex.codecogs.com/png.latex?%5Cfrac%7Bn%21%7D%7Bx%21%28n-x%29%21%7D).

- Binomial distribution has some important properties, such as:

  - The mean of the binomial distribution is equal to ![Mean](https://latex.codecogs.com/png.latex?np).
  - The variance of the binomial distribution is equal to ![Variance](https://latex.codecogs.com/png.latex?np%281-p%29).
  - The standard deviation of the binomial distribution is equal to ![Standard deviation](https://latex.codecogs.com/png.latex?%5Csqrt%7Bnp%281-p%29%7D).
  - The mode of the binomial distribution is equal to ![Mode](https://latex.codecogs.com/png.latex?%5Cleft%5Clfloor%20%5Cfrac%7B%28n&plus;1%29p%7D%7B1%7D%20%5Cright%5Crfloor) or ![Mode](https://latex.codecogs.com/png.latex?%5Cleft%5Clceil%20%5Cfrac%7B%28n&plus;1%29p%7D%7B1%7D%20-%201%20%5Cright%5Crceil), depending on the value of p.
  - The binomial distribution is symmetric when p = 0.5, skewed to the right when p < 0.5, and skewed to the left when p > 0.5.

- Binomial distribution is used to model various real-life situations, such as:

  - The number of heads in a series of coin flips.
  - The number of yes votes in a survey.
  - The number of defective items in a batch of products.
  - The number of patients who recover from a disease after a treatment.
  - The number of goals scored by a team in a soccer match.

- Binomial distribution can be approximated by other distributions, such as:

  - The normal distribution, when n is large and p is not too close to 0 or 1.
  - The Poisson distribution, when n is large and p is small.
  - The geometric distribution, when n = 1 and p is any value.