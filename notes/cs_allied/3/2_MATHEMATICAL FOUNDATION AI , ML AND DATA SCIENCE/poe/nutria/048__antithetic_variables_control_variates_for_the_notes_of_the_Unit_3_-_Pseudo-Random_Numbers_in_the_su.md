
### Antithetic Variables/Control Variates

Antithetic variables and control variates are two techniques used to reduce the variance of a Monte Carlo simulation.

**Antithetic Variables**

Antithetic variables are a technique used to reduce the variance of the Monte Carlo simulation by generating two correlated random variables. The idea is that the two random variables will cancel out each other’s variance. This technique is especially useful when the underlying random variable is normally distributed.

To implement this technique, we generate two random variables, X and Y, that have the same distribution but are negatively correlated. X and Y will be generated in such a way that X+Y=C, where C is a constant. This ensures that the two variables are negatively correlated.

**Control Variates**

Control variates are a technique used to reduce the variance of the Monte Carlo simulation by using a deterministic function of the random variable. The idea is that the deterministic function will have a lower variance than the random variable, and the difference in variance can be used to reduce the variance of the Monte Carlo simulation.

To implement this technique, we generate a random variable X and a deterministic function f(X). The variance of f(X) is assumed to be lower than the variance of X. We then calculate the difference between the expected value of X and the expected value of f(X). This difference is then used to reduce the variance of the Monte Carlo simulation.