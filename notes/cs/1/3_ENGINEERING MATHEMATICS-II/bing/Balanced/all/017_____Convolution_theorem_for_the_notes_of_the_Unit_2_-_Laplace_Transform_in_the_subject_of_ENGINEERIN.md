# Convolution Theorem

- The convolution theorem states that the Laplace transform of a convolution of two functions is the product of the Laplace transforms of the individual functions .
- The convolution of two functions f and g is defined as

  ```math
  f * g = \int_0^t f(\tau) g(t - \tau) d\tau
  ```

- The convolution theorem can be written as

  ```math
  \mathcal{L}[f * g] = F(s) G(s)
  ```

  where F(s) and G(s) are the Laplace transforms of f and g respectively .

- The convolution theorem can be used to simplify the inverse Laplace transform of a product of two functions.
- The convolution theorem can also be used to solve linear differential equations with constant coefficients and non-homogeneous boundary conditions .