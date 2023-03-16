### Monte Carlo Integration

- Monte Carlo integration is a technique for numerical integration using random numbers .
- It is a particular Monte Carlo method that numerically computes a definite integral.
- While other algorithms usually evaluate the integrand at a regular grid, Monte Carlo randomly chooses points at which the integrand is evaluated .
- The basic concept of the Monte Carlo estimator is to approximate the value of the integral by the average value of the integrand at the random points.
- The Monte Carlo estimator converges to the true value of the integral as the number of random points increases, according to the law of large numbers.
- The advantage of Monte Carlo integration is that it can handle complex domains and high-dimensional integrals, where other methods may fail or be inefficient .
- The disadvantage of Monte Carlo integration is that it is a non-deterministic approach, meaning that each realization provides a different outcome with respective error bars.
- The error of Monte Carlo integration depends on the variance of the integrand and the number of random points, and it decreases as the inverse square root of the number of points  .
- There are various ways to improve the accuracy and efficiency of Monte Carlo integration, such as importance sampling, stratified sampling, quasi-Monte Carlo methods, and variance reduction techniques   .