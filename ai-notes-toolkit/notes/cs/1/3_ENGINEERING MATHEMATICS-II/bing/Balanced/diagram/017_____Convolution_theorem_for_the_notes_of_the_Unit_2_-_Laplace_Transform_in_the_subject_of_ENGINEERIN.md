### Convolution theorem

- The convolution theorem states that the Laplace transform of a convolution of two functions is the product of the Laplace transforms of the individual functions .
- The convolution of two functions f and g is defined as

  ```math
  f * g (t) = \int_{0}^{t} f(\tau) g(t - \tau) d\tau
  ```

- The Laplace transform of a function f is defined as

  ```math
  F(s) = \mathcal{L}[f] = \int_{0}^{\infty} f(t) e^{-st} dt
  ```

- The convolution theorem can be proved by interchanging the order of integration and using the properties of the Laplace transform.
- The convolution theorem can be used to solve differential equations by breaking up a given Laplace transform into simpler factors and then finding the inverse Laplace transform of each factor.
- The convolution theorem can also be used to model physical phenomena such as heat transfer, electrical circuits, and signal processing.