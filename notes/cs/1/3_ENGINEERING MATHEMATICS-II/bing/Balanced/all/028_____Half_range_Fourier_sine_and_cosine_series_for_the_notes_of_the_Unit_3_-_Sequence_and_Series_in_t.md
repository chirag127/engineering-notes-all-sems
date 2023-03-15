# Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A sine series is a Fourier series that contains only sine terms, and it is used to represent odd functions, which are functions that satisfy f(-x) = -f(x) for all x.
- A cosine series is a Fourier series that contains only cosine terms, and it is used to represent even functions, which are functions that satisfy f(-x) = f(x) for all x.
- To find the half range Fourier series of a function f(x) defined over the interval [0, L], we need to extend the function to the interval [-L, L] in a way that preserves its symmetry. For example, if f(x) is odd, we can extend it as f(x) = -f(-x) for x < 0, and if f(x) is even, we can extend it as f(x) = f(-x) for x < 0.
- The coefficients of the half range Fourier series are given by the following formulas, where n is a positive integer:

  - For the sine series:

    - a0 = 0
    - an = 0
    - bn = (2/L) * integral from 0 to L of f(x) * sin(n * pi * x / L) dx

  - For the cosine series:

    - a0 = (1/L) * integral from 0 to L of f(x) dx
    - an = (2/L) * integral from 0 to L of f(x) * cos(n * pi * x / L) dx
    - bn = 0

- The half range Fourier series of f(x) is then given by the following sums, depending on the type of series:

  - For the sine series:

    - f(x) = sum from n = 1 to infinity of bn * sin(n * pi * x / L)

  - For the cosine series:

    - f(x) = a0 / 2 + sum from n = 1 to infinity of an * cos(n * pi * x / L)

- The half range Fourier series can be used to approximate the function f(x) over the interval [0, L], and to analyze its properties such as periodicity, symmetry, and convergence.