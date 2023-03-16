# Monte Carlo Integration

Monte Carlo integration is a technique for numerical integration using random numbers. It is a particular Monte Carlo method that numerically computes a definite integral. 

## Basic concept

- The basic idea of Monte Carlo integration is to approximate the value of an integral by the average value of the integrand over a set of randomly chosen points. 
- Suppose we want to integrate a function f over a domain D. We can write the integral as

$$
F = \int_D f(x) dx = \frac{1}{|D|} \int_D f(x) |D| dx
$$

where |D| is the area (or volume, or higher-dimensional content) of D.

- We can estimate the value of F by sampling n points x1, x2, ..., xn uniformly at random from D and computing the average value of f over these points:

$$
\hat{F}_n = \frac{1}{n} \sum_{i=1}^n f(x_i)
$$

- By the law of large numbers, the estimator $\hat{F}_n$ converges to F as n increases. The variance of the estimator is given by

$$
\mathrm{Var}(\hat{F}_n) = \frac{1}{n^2} \sum_{i=1}^n \mathrm{Var}(f(x_i)) = \frac{\sigma^2}{n}
$$

where $\sigma^2$ is the variance of f over D.

- The standard error of the estimator is the square root of the variance, which decreases as $1/\sqrt{n}$. This means that to reduce the error by a factor of 10, we need to increase the number of samples by a factor of 100. 

## Advantages and disadvantages

- Monte Carlo integration has some advantages over other numerical integration methods, such as:

  - It is easy to implement and can handle any dimensionality and shape of the domain. 
  - It can handle integrands that are discontinuous, singular, or have unknown analytical properties. 
  - It can be parallelized and distributed easily, since each sample is independent of the others. 
  - It can be combined with other techniques, such as importance sampling, variance reduction, or quasi-Monte Carlo methods, to improve the accuracy and efficiency of the estimation. 

- Monte Carlo integration also has some disadvantages, such as:

  - It is not deterministic, meaning that each run of the algorithm will produce a different outcome. The final result is an approximation with an associated error bar, and the true value is likely to be within those error bars. 
  - It converges slowly, meaning that it requires a large number of samples to achieve a desired accuracy. The error decreases as $1/\sqrt{n}$, which is slower than some other methods that converge as $1/n$ or faster. 
  - It can be inefficient or inaccurate if the integrand is highly variable or has regions of high or low values that are not well sampled by the random points. 

## References

: Monte Carlo integration - Wikipedia. https://en.wikipedia.org/wiki/Monte_Carlo_integration

: The basics of Monte Carlo integration - Towards Data Science. https://towardsdatascience.com/the-basics-of-monte-carlo-integration-5fe16b40482d