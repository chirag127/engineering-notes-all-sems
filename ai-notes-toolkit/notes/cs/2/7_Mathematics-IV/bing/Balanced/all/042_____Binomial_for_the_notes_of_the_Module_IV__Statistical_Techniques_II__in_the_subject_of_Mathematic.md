# Binomial Distribution

- Binomial distribution is a type of probability distribution that describes the possible outcomes of a series of independent trials, where each trial has only two possible outcomes, such as success or failure, yes or no, or on or off.
- Binomial distribution is defined by two parameters: n and p, where n is the number of trials and p is the probability of success in each trial. The probability of getting exactly x successes in n trials is given by the formula:

![binomial formula](https://latex.codecogs.com/png.latex?P%28X%3Dx%29%3D%5Cbinom%7Bn%7D%7Bx%7Dp%5Ex%281-p%29%5E%7Bn-x%7D)

- where ![binomial coefficient](https://latex.codecogs.com/png.latex?%5Cbinom%7Bn%7D%7Bx%7D) is the binomial coefficient, which is equal to ![factorial formula](https://latex.codecogs.com/png.latex?%5Cfrac%7Bn%21%7D%7Bx%21%28n-x%29%21%7D).

- Binomial distribution has some important properties, such as:

  - The mean of the binomial distribution is equal to ![mean formula](https://latex.codecogs.com/png.latex?np).
  - The variance of the binomial distribution is equal to ![variance formula](https://latex.codecogs.com/png.latex?np%281-p%29).
  - The standard deviation of the binomial distribution is equal to ![standard deviation formula](https://latex.codecogs.com/png.latex?%5Csqrt%7Bnp%281-p%29%7D).
  - The binomial distribution is symmetric when p = 0.5, and skewed to the right when p < 0.5, and skewed to the left when p > 0.5.
  - The binomial distribution can be approximated by the normal distribution when n is large and p is not too close to 0 or 1.

- Binomial distribution is used to model various real-life situations, such as:

  - The number of heads in a series of coin flips.
  - The number of yes votes in a survey.
  - The number of defective items in a batch of products.
  - The number of free throws made by a basketball player.

- Binomial distribution can be calculated using the binomial probability formula, or using the binompdf and binomcdf functions in a calculator or a software. For example, if a coin is flipped 10 times, and the probability of getting a head is 0.5, then the probability of getting exactly 6 heads is:

![example calculation](https://latex.codecogs.com/png.latex?P%28X%3D6%29%3D%5Cbinom%7B10%7D%7B6%7D0.5%5E6%280.5%29%5E4%3D0.205)

- Binomial distribution can be graphed using a histogram or a probability mass function, where the x-axis shows the possible values of x, and the y-axis shows the corresponding probabilities. For example, the graph of the binomial distribution with n = 10 and p = 0.5 is:

![example graph](https://www.mathsisfun.com/data/images/binomial-distribution-10-05.gif)