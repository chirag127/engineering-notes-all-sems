### Random Variable

A random variable is a variable whose value is subject to uncertainty or randomness. It is a function that maps the outcomes of a random event to numerical values. In other words, it is a numerical quantity that represents the outcome of a random event.

Random variables can be classified into two broad categories:

1. Discrete Random Variables
2. Continuous Random Variables

#### Discrete Random Variables

A discrete random variable can take on only a finite or countably infinite number of distinct values. Examples of discrete random variables include the number of heads obtained in a series of coin flips, the number of cars passing through a tollbooth in an hour, or the number of people in a room.

The probability distribution of a discrete random variable is described by a probability mass function (PMF) which assigns probabilities to each possible value that the random variable can take.

#### Continuous Random Variables

A continuous random variable can take on any value within a specified range. Examples of continuous random variables include the height of a person or the time it takes to complete a task.

The probability distribution of a continuous random variable is described by a probability density function (PDF) which assigns probabilities to intervals of values that the random variable can take.

#### Notation

Random variables are typically denoted by capital letters, such as X, Y or Z. The values that a random variable can take are denoted by lowercase letters, such as x, y or z.

The probability that a random variable takes on a particular value is denoted by P(X=x), where X is the random variable and x is a particular value.

#### Expected Value

The expected value of a random variable is the average value that the random variable takes over the long run. It is denoted by E(X) and is calculated as the sum of the product of each possible value of X and its corresponding probability. For discrete random variables, it is calculated as:

```
E(X) = ∑x P(X=x) x
```

For continuous random variables, it is calculated as:

```
E(X) = ∫ f(x) x dx
```

where f(x) is the probability density function of X.

#### Variance and Standard Deviation

The variance of a random variable measures how much the random variable deviates from its expected value. It is denoted by Var(X) and is calculated as the expected value of the squared difference between the random variable and its expected value. For discrete random variables, it is calculated as:

```
Var(X) = E[(X - E(X))^2] = ∑x P(X=x) (x - E(X))^2
```

For continuous random variables, it is calculated as:

```
Var(X) = E[(X - E(X))^2] = ∫ f(x) (x - E(X))^2 dx
```

The standard deviation of a random variable is the square root of its variance. It is denoted by σ(X) and is a measure of the spread of the random variable.

#### Conclusion

Random variables are a fundamental concept in statistics and probability theory. They provide a way to quantify and analyze the uncertainty inherent in many real-world phenomena. Understanding the properties and characteristics of random variables is essential for developing statistical models, making predictions, and drawing conclusions from data.