### Moment Generating Function (MGF)

A moment generating function (MGF) is a mathematical tool used in probability theory and statistics to describe the distribution of a random variable. It is defined as the expected value of the exponential function of the random variable, that is, if X is a random variable, its MGF is given by:

`M_X(t) = E[e^(tX)]`

where `t` is a real number and `E` denotes the expected value.

The MGF is useful because it can be used to derive the moments of the distribution of the random variable. The `n`-th moment of the distribution is given by the `n`-th derivative of the MGF evaluated at `t = 0`. That is:

`E[X^n] = M_X^(n)(0)`

where `M_X^(n)(0)` denotes the `n`-th derivative of the MGF evaluated at `t = 0`.

The MGF is not always defined for all values of `t`. In particular, it may not exist for values of `t` that are too large. However, if the MGF exists in a neighborhood of `t = 0`, then it uniquely determines the distribution of the random variable.

In summary, the moment generating function is a useful tool for characterizing the distribution of a random variable and for deriving its moments. It is defined as the expected value of the exponential function of the random variable and can be used to derive the moments of the distribution if it exists in a neighborhood of `t = 0`.