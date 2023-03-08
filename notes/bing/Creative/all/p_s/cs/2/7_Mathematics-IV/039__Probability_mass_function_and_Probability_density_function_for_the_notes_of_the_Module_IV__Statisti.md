### Probability mass function and Probability density function

- Probability mass function (PMF) and probability density function (PDF) are two ways of describing the probability distribution of a random variable.
- A random variable is a variable whose value is determined by the outcome of a random experiment.
- A probability distribution is a function that assigns probabilities to all possible values of a random variable.
- A discrete random variable is a random variable that can take only a finite or countable number of values, such as the number of heads in a coin toss, the roll of a die, or the number of students in a class.
- A continuous random variable is a random variable that can take any value in an interval or a collection of intervals, such as the height of a person, the weight of a fruit, or the time of arrival of a bus.
- A PMF is a function that gives the probability that a discrete random variable is exactly equal to some value. For example, the PMF of the number of heads in two coin tosses is:

| x | P(X = x) |
|---|----------|
| 0 | 0.25     |
| 1 | 0.5      |
| 2 | 0.25     |

- A PDF is a function that gives the relative likelihood that a continuous random variable is equal to some value. However, since the probability of a continuous random variable being exactly equal to any value is zero, the PDF is usually used to find the probability that a continuous random variable falls within some interval. For example, the PDF of the height of a person in centimeters is:

![PDF of height](https://www.embibe.com/exams/wp-content/uploads/sites/2/2021/01/Probability-Density-Function-1.png)

- The probability that the height of a person is between 160 and 170 cm is given by the area under the curve between 160 and 170, which is approximately 0.2.
- The properties of a PMF are:

  - It is non-negative, i.e., P(X = x) ≥ 0 for all x.
  - It sums to one, i.e., ∑ P(X = x) = 1, where the sum is over all possible values of x.
  - It gives the probability of each possible value of x, i.e., P(X = x) = P({ω ∈ Ω : X(ω) = x}), where Ω is the sample space of the random experiment and X(ω) is the value of X corresponding to the outcome ω.

- The properties of a PDF are:

  - It is non-negative, i.e., f(x) ≥ 0 for all x.
  - It integrates to one, i.e., ∫ f(x) dx = 1, where the integral is over the entire domain of x.
  - It gives the relative likelihood of each possible value of x, i.e., f(x) = P(X = x) / dx, where dx is an infinitesimal interval around x. However, this does not mean that f(x) is the probability of X = x, since P(X = x) = 0 for any x.

Some possible mnemonics and learning tricks for the topic are:

- To remember the difference between PMF and PDF, think of PMF as Probability of a Mass of values, and PDF as Probability of a Density of values. Mass is discrete and countable, while density is continuous and uncountable.
- To remember the properties of a PMF, think of PMS: Positive, adds to one, and gives the probability of each value.
- To remember the properties of a PDF, think of PID: Positive, integrates to one, and gives the relative likelihood of each value.