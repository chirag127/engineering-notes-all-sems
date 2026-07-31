### Fourier Series

Fourier series is a mathematical tool used to represent periodic functions as an infinite sum of sines and cosines. It is named after the French mathematician Jean-Baptiste Joseph Fourier, who introduced the concept in his study of heat transfer.

The Fourier series of a periodic function `f(x)` with period `2π` is given by:

`f(x) = a0/2 + Σ(an * cos(nx) + bn * sin(nx))`

where `n` ranges from `1` to `∞`, and the coefficients `an` and `bn` are given by:

`an = (1/π) * Σ(f(x) * cos(nx))`

`bn = (1/π) * Σ(f(x) * sin(nx))`

The coefficients `an` and `bn` can be calculated using the following integrals:

`an = (1/π) * ∫[f(x) * cos(nx)] dx`

`bn = (1/π) * ∫[f(x) * sin(nx)] dx`

where the integral is taken over one period of the function.

Fourier series can be used to approximate any periodic function, and the accuracy of the approximation increases as more terms are included in the series. It is widely used in engineering, physics, and other fields to analyze periodic signals and systems.

Some important properties of Fourier series include:

- Linearity: The Fourier series of the sum of two functions is equal to the sum of their Fourier series.
- Symmetry: The Fourier series of an even function contains only cosine terms, while the Fourier series of an odd function contains only sine terms.
- Parseval's Theorem: The sum of the squares of the Fourier coefficients is equal to the average value of the square of the function over one period.
