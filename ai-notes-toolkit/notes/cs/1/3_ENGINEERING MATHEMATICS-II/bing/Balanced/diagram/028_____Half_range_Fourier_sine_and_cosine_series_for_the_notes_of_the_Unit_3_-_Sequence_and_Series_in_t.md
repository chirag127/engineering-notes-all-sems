### Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that represents a function defined over half the range of its period, say from 0 to L, instead of the full range from -L to L .
- A half range Fourier series can be either a cosine series or a sine series, depending on the type of extension of the function over the full range .
- A cosine series is obtained by extending the function as an even function, that is, f(-x) = f(x) for all x in [-L, L]  .
- A sine series is obtained by extending the function as an odd function, that is, f(-x) = -f(x) for all x in [-L, L]  .
- The general form of a half range cosine series is :

f(x) = a_0/2 + sum_{n=1}^infty a_n cos(n pi x/L)

where

a_0 = (2/L) int_0^L f(x) dx

a_n = (2/L) int_0^L f(x) cos(n pi x/L) dx

- The general form of a half range sine series is :

f(x) = sum_{n=1}^infty b_n sin(n pi x/L)

where

b_n = (2/L) int_0^L f(x) sin(n pi x/L) dx

- The half range Fourier series can be used to approximate periodic functions that are not defined over the full range, or to simplify the calculations of the Fourier coefficients by exploiting the symmetry properties of even and odd functions   .