Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your notes.

### Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A sine series is a Fourier series that contains only sine terms, and it is used for odd functions, which satisfy `f(-x) = -f(x)`.
- A cosine series is a Fourier series that contains only cosine terms, and it is used for even functions, which satisfy `f(-x) = f(x)`.
- To find a half range Fourier series, we need to extend the function to the full range by using its symmetry property, and then apply the standard Fourier series formulae.
- The general form of a half range Fourier series is:

  - For a sine series:

    `f(x) = sum_(n=1)^infty b_n sin(n pi x/L)`

    where `b_n = (2/L) int_0^L f(x) sin(n pi x/L) dx`

  - For a cosine series:

    `f(x) = a_0/2 + sum_(n=1)^infty a_n cos(n pi x/L)`

    where `a_0 = (2/L) int_0^L f(x) dx` and `a_n = (2/L) int_0^L f(x) cos(n pi x/L) dx`

- The half range Fourier series can be used to approximate the function over the half range, and to analyze its frequency components.