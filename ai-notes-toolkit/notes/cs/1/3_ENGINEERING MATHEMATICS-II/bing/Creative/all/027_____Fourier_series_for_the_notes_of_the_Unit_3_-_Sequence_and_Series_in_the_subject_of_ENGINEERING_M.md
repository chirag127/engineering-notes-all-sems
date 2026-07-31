# Fourier Series

## Definition

A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines. Fourier series make use of the orthogonality relationships of the sine and cosine functions. A Fourier series can be used to represent periodic functions of any period by scaling the argument of the function .

## Formula

The general form of a Fourier series is:

f(x) = a0/2 + sum(n=1 to infinity) [an cos(nx) + bn sin(nx)]

where a0, an, and bn are the Fourier coefficients, and n is the frequency or harmonic of the sine and cosine terms. The Fourier coefficients can be calculated by using the following formulas:

a0 = (1/pi) integral(x=0 to pi) f(x) dx

an = (1/pi) integral(x=0 to pi) f(x) cos(nx) dx

bn = (1/pi) integral(x=0 to pi) f(x) sin(nx) dx

## Applications

Fourier series have many applications in various fields of mathematics, physics, engineering, and signal processing. Some of the applications are:

- Solving partial differential equations, such as the heat equation, the wave equation, and the Laplace equation .
- Analyzing periodic signals, such as sound waves, light waves, and electrical signals .
- Decomposing complex functions into simpler components, such as harmonics, modes, and spectra .
- Approximating discontinuous functions, such as square waves, sawtooth waves, and triangle waves .

## Examples

Here are some examples of Fourier series of common functions:

- The Fourier series of the function f(x) = x, with period 2pi, is:

f(x) = pi - 4/pi sum(n=1 to infinity) [(-1)^n / (2n - 1)^2] cos((2n - 1)x)

- The Fourier series of the function f(x) = |x|, with period 2pi, is:

f(x) = pi/2 - 4/pi sum(n=1 to infinity) [1 / (2n - 1)] sin((2n - 1)x)

- The Fourier series of the function f(x) = 1, with period 2pi, is:

f(x) = 1

- The Fourier series of the function f(x) = sin(x), with period 2pi, is:

f(x) = sin(x)