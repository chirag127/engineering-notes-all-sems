# Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines  .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions  .
- Fourier series can be used to represent periodic functions as a linear combination of sine and cosine functions  .
- Fourier series are very useful in connection with various problems involving partial differential equations, signal processing, image processing, etc  .

## Fourier Series Formula

- The general form of a Fourier series is:

  f(x) = a0/2 + sum(n=1 to infinity) [an cos(nx) + bn sin(nx)]

  where a0, an, and bn are the Fourier coefficients   .

- The Fourier coefficients can be calculated using the following formulas:

  a0 = (1/pi) integral(-pi to pi) f(x) dx

  an = (1/pi) integral(-pi to pi) f(x) cos(nx) dx

  bn = (1/pi) integral(-pi to pi) f(x) sin(nx) dx

  for n = 1, 2, 3, ...   .

- The Fourier series is valid for any periodic function f(x) with period 2pi. If the function has a different period, say 2L, then the formulas can be modified by replacing x with x/L and n with nL   .

## Fourier Series Examples

- Example 1: Find the Fourier series of the function f(x) = x, for -pi < x < pi.

  Solution: The function is odd, so a0 = 0 and an = 0 for all n. The bn coefficients are:

  bn = (1/pi) integral(-pi to pi) x sin(nx) dx

     = (2/pi) integral(0 to pi) x sin(nx) dx

     = (2/pi) [(-x cos(nx))/n + (sin(nx))/n^2] (0 to pi)

     = (2/pi) [(-pi cos(npi))/n + (sin(npi))/n^2 - (sin(0))/n^2]

     = (2/pi) [(-1)^n pi/n]

  Therefore, the Fourier series is:

  f(x) = sum(n=1 to infinity) [(-1)^n 2pi/n sin(nx)]

- Example 2: Find the Fourier series of the function f(x) = |x|, for -pi < x < pi.

  Solution: The function is even, so bn = 0 for all n. The a0 and an coefficients are:

  a0 = (1/pi) integral(-pi to pi) |x| dx

     = (2/pi) integral(0 to pi) x dx

     = (2/pi) [x^2/2] (0 to pi)

     = (2/pi) [pi^2/2]

     = pi

  an = (1/pi) integral(-pi to pi) |x| cos(nx) dx

     = (2/pi) integral(0 to pi) x cos(nx) dx

     = (2/pi) [(x sin(nx))/n + (cos(nx))/n^2] (0 to pi)

     = (2/pi) [(pi sin(npi))/n + (cos(npi))/n^2 - (cos(0))/n^2]

     = (2/pi) [(-1)^n/n^2]

  Therefore, the Fourier series is:

  f(x) = pi/2 + sum(n=1 to infinity) [(-1)^n 4/pi n^2 cos(nx)]