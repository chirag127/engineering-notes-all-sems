### Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines .
- Fourier series can be used to represent periodic functions as a linear combination of sine and cosine functions .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions.
- Fourier series are analogous to Taylor series, which represent functions as possibly infinite sums of monomial terms.
- Fourier series are very powerful tools in connection with various problems involving partial differential equations.

#### Formula of Fourier Series

- The general form of a Fourier series is:

  f(x) = a0/2 + sum(n=1 to infinity) [an cos(nx) + bn sin(nx)]

  where a0, an, and bn are the Fourier coefficients .

- The Fourier coefficients can be calculated using the following formulas:

  a0 = (1/pi) int(-pi to pi) f(x) dx

  an = (1/pi) int(-pi to pi) f(x) cos(nx) dx

  bn = (1/pi) int(-pi to pi) f(x) sin(nx) dx

  where n is a positive integer .

#### Examples of Fourier Series

- The Fourier series of the function f(x) = x, defined on the interval [-pi, pi], is:

  f(x) = 0 + sum(n=1 to infinity) [(-1)^n+1 (2/n) sin(nx)]

  This can be verified by calculating the Fourier coefficients using the formulas above.

- The Fourier series of the function f(x) = |x|, defined on the interval [-pi, pi], is:

  f(x) = pi/2 + sum(n=1 to infinity) [(-1)^n (4/n^2) cos(nx)]

  This can be verified by calculating the Fourier coefficients using the formulas above.

- The Fourier series of the function f(x) = x^2, defined on the interval [-pi, pi], is:

  f(x) = pi^2/3 + sum(n=1 to infinity) [(-1)^n (4/n^2) cos(nx)]

  This can be verified by calculating the Fourier coefficients using the formulas above.

#### Applications of Fourier Series

- Fourier series can be used to model periodic phenomena such as sound waves, heat conduction, electric currents, and light intensity .
- Fourier series can be used to approximate non-periodic functions by extending their domain to a larger interval and applying the Fourier series formula.
- Fourier series can be used to solve partial differential equations such as the heat equation, the wave equation, and the Laplace equation by separating the variables and applying the Fourier series formula.