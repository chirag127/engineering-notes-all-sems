### Half range Fourier sine and cosine series

In the subject of ENGINEERING MATHEMATICS-II, Unit 3 - Sequence and Series, one of the important topics is the Half range Fourier sine and cosine series.

- A half-range Fourier sine series is a representation of a function in terms of sine functions only.
- A half-range Fourier cosine series is a representation of a function in terms of cosine functions only.
- These series are used to represent functions defined on a finite interval, typically [0, L].
- The coefficients of the series are determined by the orthogonality properties of the sine and cosine functions.
- The half-range Fourier sine series of a function f(x) defined on the interval [0, L] is given by:

f(x) = sum from n=1 to infinity of (b_n * sin(n * pi * x / L))

where b_n = (2/L) * integral from 0 to L of (f(x) * sin(n * pi * x / L) dx)

- The half-range Fourier cosine series of a function f(x) defined on the interval [0, L] is given by:

f(x) = a_0/2 + sum from n=1 to infinity of (a_n * cos(n * pi * x / L))

where a_0 = (2/L) * integral from 0 to L of (f(x) dx) and a_n = (2/L) * integral from 0 to L of (f(x) * cos(n * pi * x / L) dx)

- These series are useful in solving boundary value problems in engineering and physics.