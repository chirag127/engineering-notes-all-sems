### Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A sine series is a Fourier series that contains only sine terms, and it is used to represent odd functions, which satisfy f(-x) = -f(x) for all x.
- A cosine series is a Fourier series that contains only cosine terms, and it is used to represent even functions, which satisfy f(-x) = f(x) for all x.
- To find a half range Fourier series, we need to extend the function to the full range by using either odd or even extension, and then apply the standard Fourier series formulae.
- The general formulae for the half range Fourier series are:

  - Half range cosine series:

    f(x) = a0/2 + sum_{n=1}^infty a_n cos(n pi x/L)

    where

    a0 = (2/L) int_0^L f(x) dx

    a_n = (2/L) int_0^L f(x) cos(n pi x/L) dx

  - Half range sine series:

    f(x) = sum_{n=1}^infty b_n sin(n pi x/L)

    where

    b_n = (2/L) int_0^L f(x) sin(n pi x/L) dx

- The half range Fourier series can be used to approximate functions over a finite interval, and to solve boundary value problems involving heat conduction, vibration, and wave motion.