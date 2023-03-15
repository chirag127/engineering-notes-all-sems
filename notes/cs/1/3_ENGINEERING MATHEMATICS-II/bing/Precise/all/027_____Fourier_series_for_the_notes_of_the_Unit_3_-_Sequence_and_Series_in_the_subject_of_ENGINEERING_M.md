# Unit 3 - Sequence and Series: Fourier Series

Fourier series is a way to represent a periodic function as an infinite sum of sine and cosine functions. It is named after the French mathematician Jean-Baptiste Joseph Fourier, who introduced the concept in his study of heat transfer.

The Fourier series of a periodic function f(x) with period 2π is given by:

f(x) = a0/2 + Σ (an * cos(nx) + bn * sin(nx))

where the coefficients an and bn are given by:

an = (1/π) * ∫ f(x) * cos(nx) dx, from -π to π

bn = (1/π) * ∫ f(x) * sin(nx) dx, from -π to π

The Fourier series can be used to approximate a periodic function with arbitrary accuracy. It is widely used in engineering, physics, and other fields to analyze periodic signals and systems.

Some important properties of Fourier series include:

- Linearity: The Fourier series of the sum of two functions is equal to the sum of their Fourier series.
- Symmetry: The Fourier series of an even function contains only cosine terms, while the Fourier series of an odd function contains only sine terms.
- Parseval's Theorem: The sum of the squares of the Fourier coefficients of a function is equal to the integral of the square of the function over one period.
