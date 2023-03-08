### Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A half range Fourier series can be useful for representing functions that are discontinuous, odd, or even over a certain interval.

#### Half range cosine series

- A half range cosine series is a Fourier series that consists of cosine terms only.
- A half range cosine series can be obtained by extending the function f(x) as an even function over the interval [-L, L], where L is half the period of the original function.
- A half range cosine series has the form:

  f(x) = a0/2 + sum_{n=1}^infty a_n cos(n pi x/L)

  where the coefficients a_n are given by:

  a_n = (2/L) int_0^L f(x) cos(n pi x/L) dx

- A half range cosine series can be used to represent functions that are even or discontinuous over the interval [0, L].

#### Half range sine series

- A half range sine series is a Fourier series that consists of sine terms only.
- A half range sine series can be obtained by extending the function f(x) as an odd function over the interval [-L, L], where L is half the period of the original function.
- A half range sine series has the form:

  f(x) = sum_{n=1}^infty b_n sin(n pi x/L)

  where the coefficients b_n are given by:

  b_n = (2/L) int_0^L f(x) sin(n pi x/L) dx

- A half range sine series can be used to represent functions that are odd or discontinuous over the interval [0, L].

Some possible mnemonics and learning tricks for the topic are:

- To remember the formula for the half range cosine series, you can use the acronym ACE: A for a0/2, C for cosine, and E for even function.
- To remember the formula for the half range sine series, you can use the acronym BOS: B for b_n, O for odd function, and S for sine.
- To remember the integrals for the coefficients, you can use the rhyme: "From zero to L, multiply and integrate, with cosine or sine, depending on the case."
- To remember whether to use a sine or cosine series, you can use the rule: "If the function is odd, use sine; if the function is even, use cosine; if the function is neither, use both."