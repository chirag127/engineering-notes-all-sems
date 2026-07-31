### Monte Carlo Integration

Monte Carlo integration is a technique for numerical integration using random numbers. It is a particular Monte Carlo method that numerically computes a definite integral. 

- The basic concept of Monte Carlo integration is to use randomness to approximate the value of an integral by sampling points from a domain and evaluating the integrand at those points. 
- The Monte Carlo estimator of an integral is given by the average of the function values at the sampled points, multiplied by the area (or volume, or higher-dimensional content) of the domain. 
- The accuracy of the Monte Carlo estimator depends on the number of samples and the variance of the integrand. The more samples are used, the more likely the estimator is to converge to the true value of the integral. The lower the variance of the integrand, the smaller the error of the estimator. 
- Monte Carlo integration has some advantages over other numerical integration methods, such as:
  - It can handle integrands that are complex, high-dimensional, discontinuous, or have singularities. 
  - It does not require a regular grid or a specific quadrature rule to evaluate the integrand. 
  - It can be easily parallelized and distributed. 
- Monte Carlo integration also has some disadvantages, such as:
  - It is a non-deterministic method, meaning that each realization provides a different outcome with respective error bars. 
  - It can be slow to converge, especially for integrands with high variance or low smoothness. 
  - It can suffer from the curse of dimensionality, meaning that the number of samples required to achieve a given accuracy grows exponentially with the dimension of the domain. 

: Monte Carlo integration - Wikipedia
: The basics of Monte Carlo integration - Towards Data Science