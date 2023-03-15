### Half range Fourier sine and cosine series

The half range Fourier sine and cosine series are used to represent a function defined on a finite interval in terms of sine and cosine functions. These series are useful in solving problems in engineering and physics where the function is defined only on a finite interval.

- The half range Fourier sine series of a function `f(x)` defined on the interval `[0, L]` is given by:

```
f(x) = sum_(n=1)^infinity b_n sin((n pi x)/L)
```

where `b_n` is given by:

```
b_n = (2/L) int_0^L f(x) sin((n pi x)/L) dx
```

- The half range Fourier cosine series of a function `f(x)` defined on the interval `[0, L]` is given by:

```
f(x) = a_0/2 + sum_(n=1)^infinity a_n cos((n pi x)/L)
```

where `a_n` is given by:

```
a_n = (2/L) int_0^L f(x) cos((n pi x)/L) dx
```

- These series can be used to represent a function defined on a finite interval in terms of sine and cosine functions.
- The coefficients `a_n` and `b_n` can be determined by using the orthogonality properties of sine and cosine functions.
- The half range Fourier sine and cosine series are useful in solving problems in engineering and physics where the function is defined only on a finite interval.
