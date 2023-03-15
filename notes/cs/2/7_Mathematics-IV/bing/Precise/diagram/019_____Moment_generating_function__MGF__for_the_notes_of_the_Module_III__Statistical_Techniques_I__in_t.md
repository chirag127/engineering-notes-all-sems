### Moment Generating Function (MGF)

The moment generating function (MGF) is a useful tool in probability theory and statistics. It is defined as the expected value of the exponential function of a random variable. Specifically, for a random variable X, the MGF is defined as:

$$ M_X(t) = E[e^{tX}] $$

where t is a real number and E[.] denotes the expected value.

The MGF is useful because it can be used to derive the moments of a distribution. The nth moment of a distribution is given by the nth derivative of the MGF evaluated at t=0. That is:

$$ E[X^n] = M_X^{(n)}(0) $$

where $M_X^{(n)}(0)$ denotes the nth derivative of the MGF evaluated at t=0.

The MGF is not always defined for all values of t. When it is defined, it uniquely determines the distribution of the random variable X.

Some common MGFs include:

- The MGF of a Bernoulli distribution with parameter p is given by $M_X(t) = 1-p+pe^t$.
- The MGF of a Poisson distribution with parameter λ is given by $M_X(t) = e^{\lambda(e^t-1)}$.
- The MGF of a normal distribution with mean μ and variance σ^2 is given by $M_X(t) = e^{\mu t + \frac{1}{2}\sigma^2t^2}$.
