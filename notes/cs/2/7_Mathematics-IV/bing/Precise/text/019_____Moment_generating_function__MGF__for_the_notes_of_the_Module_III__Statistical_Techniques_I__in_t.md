### Moment Generating Function (MGF)

A moment generating function (MGF) is a mathematical tool used in probability theory and statistics to describe the distribution of a random variable. It is defined as the expected value of the exponential function of the random variable, that is, if X is a random variable, its MGF is given by:

M_X(t) = E[e^(tX)]

where t is a real number and E[.] denotes the expected value.

The MGF is useful because it can be used to derive the moments of the distribution of X. The n-th moment of X is given by the n-th derivative of the MGF evaluated at t=0, that is:

E[X^n] = M_X^(n)(0)

where M_X^(n)(0) denotes the n-th derivative of the MGF evaluated at t=0.

The MGF is not always defined for all values of t. When it is defined, it uniquely determines the distribution of the random variable X. This means that if two random variables have the same MGF, they have the same distribution.

Some common MGFs include:

- The MGF of a Bernoulli random variable with parameter p is given by M_X(t) = 1-p+pe^t.
- The MGF of a Poisson random variable with parameter λ is given by M_X(t) = e^(λ(e^t-1)).
- The MGF of a normal random variable with mean μ and variance σ^2 is given by M_X(t) = e^(μt+σ^2t^2/2).

The MGF is an important tool in the study of probability distributions and is covered in the Module III: Statistical Techniques I of the Mathematics-IV KCS course. It is important to understand the properties and applications of the MGF in order to effectively use it in statistical analysis.