### Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions .
- Fourier series can be used to represent periodic functions as a linear combination of sine and cosine functions .
- Fourier series is a very powerful tool in connection with various problems involving partial differential equations.
- The computation and study of Fourier series is known as harmonic analysis.

#### Formula of Fourier Series

- The general form of a Fourier series is:

  f(x) = a0/2 + sum(n=1 to infinity) [an cos(nx) + bn sin(nx)]

  where a0, an, and bn are called the Fourier coefficients  .

- The Fourier coefficients can be calculated using the following formulas:

  a0 = (1/pi) integral(-pi to pi) f(x) dx

  an = (1/pi) integral(-pi to pi) f(x) cos(nx) dx

  bn = (1/pi) integral(-pi to pi) f(x) sin(nx) dx

  for n = 1, 2, 3, ...  .

#### Examples of Fourier Series

- Example 1: Find the Fourier series of the function f(x) = x, defined on the interval [-pi, pi] and extended periodically.

  Solution:

  The Fourier coefficients are:

  a0 = (1/pi) integral(-pi to pi) x dx = 0

  an = (1/pi) integral(-pi to pi) x cos(nx) dx = 0

  bn = (1/pi) integral(-pi to pi) x sin(nx) dx = (-1/n) [cos(nx)](-pi to pi) = 2/n (1 - (-1)^n)

  Therefore, the Fourier series is:

  f(x) = sum(n=1 to infinity) [2/n (1 - (-1)^n) sin(nx)]

- Example 2: Find the Fourier series of the function f(x) = |x|, defined on the interval [-pi, pi] and extended periodically.

  Solution:

  The Fourier coefficients are:

  a0 = (1/pi) integral(-pi to pi) |x| dx = (2/pi) integral(0 to pi) x dx = 2

  an = (1/pi) integral(-pi to pi) |x| cos(nx) dx = (2/pi) integral(0 to pi) x cos(nx) dx = (2/pi) [x sin(nx)/n + cos(nx)/n^2](0 to pi) = 4/n^2 (1 - (-1)^n)

  bn = (1/pi) integral(-pi to pi) |x| sin(nx) dx = 0

  Therefore, the Fourier series is:

  f(x) = 1 + sum(n=1 to infinity) [4/n^2 (1 - (-1)^n) cos(nx)]

#### Applications of Fourier Series

- Fourier series have many applications in various fields of science and engineering, such as:

  - Signal processing: Fourier series can be used to analyze and synthesize periodic signals, such as sound waves, radio waves, and electrical currents .
  - Heat transfer: Fourier series can be used to solve the heat equation, which models the flow of heat in a solid body .
  - Quantum mechanics: Fourier series can be used to express the wave function of a particle in a periodic potential, such as an electron in a crystal lattice .
  - Image processing: Fourier series can be used to compress and decompress images, such as JPEG files .
  - Music: Fourier series can be used to decompose a musical sound into its harmonic components, such as pitch, timbre, and volume .