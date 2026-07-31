### Antithetic Variables/Control Variates

Antithetic variables and control variates are variance reduction techniques used in Monte Carlo methods. These methods are used when estimating some quantity of two distributions, and they reduce the variance of estimators by controlling the covariance between the random variables of the two distributions.

The antithetic variable procedure makes use of the antitheses of the random numbers, namely (1− u1), (1− u2),…, (1− un), to form x ′ given by x ′=g (1− u1, 1− u2,…, 1− un). Write X ′′ as the corresponding random variable.

Antithetic variates work best when f is a monotonically increasing function. Then Cov[f (X),f (−X)] <0 and the antithetic variates reduce simulation variance.

Control variates are another variance reduction technique used in Monte Carlo methods. The idea is to use additional information about the system being simulated to reduce the variance of the estimator. This is done by introducing a control variate, which is a random variable that is correlated with the quantity being estimated, and for which the expected value is known.
