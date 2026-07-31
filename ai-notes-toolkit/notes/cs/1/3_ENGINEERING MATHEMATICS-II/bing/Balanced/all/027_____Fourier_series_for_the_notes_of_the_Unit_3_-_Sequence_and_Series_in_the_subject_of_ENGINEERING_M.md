# Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines  .
- Fourier series can be used to represent periodic functions as a linear combination of sine and cosine functions .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions .
- Fourier series are analogous to Taylor series, which represent functions as possibly infinite sums of monomial terms.
- Fourier series are very powerful tools in connection with various problems involving partial differential equations .

## Definition and Formula

- A periodic function f(x) with period T can be expressed as a Fourier series of the form  :

f(x) = a0/2 + sum(n=1 to infinity) [an cos(n pi x/T) + bn sin(n pi x/T)]

- where the coefficients a0, an, and bn are given by the following formulas  :

a0 = (2/T) integral(x=0 to T) f(x) dx

an = (2/T) integral(x=0 to T) f(x) cos(n pi x/T) dx

bn = (2/T) integral(x=0 to T) f(x) sin(n pi x/T) dx

- The term a0/2 is called the constant term or the average value of the function  .
- The terms an cos(n pi x/T) and bn sin(n pi x/T) are called the harmonic terms or the Fourier terms  .
- The number n pi/T is called the frequency or the angular frequency of the harmonic term  .

## Examples

- Example 1: Find the Fourier series of the function f(x) = x defined on the interval [-pi, pi] and extended periodically .

Solution:

- The period of the function is T = 2 pi, so the Fourier series is of the form:

f(x) = a0/2 + sum(n=1 to infinity) [an cos(n x) + bn sin(n x)]

- To find the coefficients, we use the formulas:

a0 = (2/T) integral(x=0 to T) f(x) dx

an = (2/T) integral(x=0 to T) f(x) cos(n pi x/T) dx

bn = (2/T) integral(x=0 to T) f(x) sin(n pi x/T) dx

- Substituting T = 2 pi and f(x) = x, we get:

a0 = (1/pi) integral(x=0 to 2 pi) x dx = (1/pi) [x^2/2] from 0 to 2 pi = 0

an = (1/pi) integral(x=0 to 2 pi) x cos(n x) dx = (1/pi) [x sin(n x)/n - cos(n x)/n^2] from 0 to 2 pi = 0

bn = (1/pi) integral(x=0 to 2 pi) x sin(n x) dx = (1/pi) [-x cos(n x)/n - sin(n x)/n^2] from 0 to 2 pi = -2/n (for n not equal to 0)

- Therefore, the Fourier series is:

f(x) = sum(n=1 to infinity) [-2/n sin(n x)]

- Example 2: Find the Fourier series of the function f(x) = |x| defined on the interval [-pi, pi] and extended periodically .

Solution:

- The period of the function is T = 2 pi, so the Fourier series is of the form:

f(x) = a0/2 + sum(n=1 to infinity) [an cos(n x) + bn sin(n x)]

- To find the coefficients, we use the formulas:

a0 = (2/T) integral(x=0 to T) f(x) dx

an = (2/T) integral(x=0 to T) f(x) cos(n pi x/T) dx

bn = (2/T)