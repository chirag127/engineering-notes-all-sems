### Moments

- Moments are measures of the shape and variability of a data set.
- Moments are used to describe the location and dispersion of the data.
- Moments are defined as the expected values of powers of the random variable under consideration.
- Moments can be used to find a probability distribution's mean, variance, and skewness.
- Moments can also be used to estimate the population parameters by the method of moments.

#### Types of Moments

- There are several types of moments that can be calculated, each providing different information about the data set.
- The most common types of moments are:

  - **Raw moments**: These are the moments of the random variable itself, without any transformation. They are denoted by $\mu_n=E(X^n)$, where $n$ is the order of the moment and $E$ is the expectation operator.
  - **Central moments**: These are the moments of the random variable after subtracting its mean. They are denoted by $\mu_n=E[(X-\mu)^n]$, where $\mu$ is the mean of the random variable. The central moments measure the deviation of the random variable from its mean.
  - **Standardized moments**: These are the moments of the random variable after dividing by its standard deviation. They are denoted by $\gamma_n=E[(X-\mu)^n]/\sigma^n$, where $\sigma$ is the standard deviation of the random variable. The standardized moments measure the shape of the distribution, independent of its scale.

#### Examples of Moments

- Some examples of moments and their interpretations are:

  - The zeroth raw moment is the total mass of the distribution, if the random variable represents mass density.
  - The first raw moment is the mean of the distribution, which measures the location of the data.
  - The second raw moment is the second moment of inertia of the distribution, which measures the spread of the data.
  - The second central moment is the variance of the distribution, which measures the variability of the data.
  - The third central moment is the skewness of the distribution, which measures the asymmetry of the data.
  - The fourth central moment is the kurtosis of the distribution, which measures the peakedness or flatness of the data.
  - The third standardized moment is the coefficient of skewness, which measures the degree of deviation from symmetry.
  - The fourth standardized moment is the coefficient of kurtosis, which measures the degree of deviation from normality.

#### Method of Moments

- The method of moments is a method of estimation of population parameters.
- The method of moments starts by expressing the population moments as functions of the parameters of interest.
- The method of moments then equates the population moments with the sample moments, which are calculated from the observed data.
- The method of moments then solves for the parameters by algebraic or numerical methods.
- The method of moments is simple and intuitive, but it may not be efficient or consistent in some cases.

#### References

: https://vitalflux.com/types-uses-of-moments-in-statistics/
: https://www.analyticsvidhya.com/blog/2022/01/moments-a-must-known-statistical-concept-for-data-science/
: https://www.thoughtco.com/what-are-moments-in-statistics-3126234
: https://en.wikipedia.org/wiki/Moment_(mathematics)
: https://en.wikipedia.org/wiki/Method_of_moments_(statistics)