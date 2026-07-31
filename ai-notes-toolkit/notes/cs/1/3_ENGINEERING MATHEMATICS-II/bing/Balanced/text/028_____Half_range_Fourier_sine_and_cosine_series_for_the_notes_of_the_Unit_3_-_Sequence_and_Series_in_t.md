### Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A sine series is a Fourier series that contains only sine terms, and it is used to represent odd functions, which satisfy f(-x) = -f(x) for all x.
- A cosine series is a Fourier series that contains only cosine terms, and it is used to represent even functions, which satisfy f(-x) = f(x) for all x.
- To obtain a half range Fourier series, the original function is extended periodically to the full range, either by taking the odd or even extension of the function, and then applying the standard Fourier series formulae.
- The general formulae for the half range Fourier series are:

  - For the sine series:

    f(x) = sum_{n=1}^{infty} b_n sin(n pi x / L)

    where b_n = (2/L) int_{0}^{L} f(x) sin(n pi x / L) dx

  - For the cosine series:

    f(x) = a_0 / 2 + sum_{n=1}^{infty} a_n cos(n pi x / L)

    where a_0 = (2/L) int_{0}^{L} f(x) dx

    and a_n = (2/L) int_{0}^{L} f(x) cos(n pi x / L) dx

- The half range Fourier series can be used to approximate any function over a finite interval, as long as the function is integrable and satisfies the Dirichlet conditions.