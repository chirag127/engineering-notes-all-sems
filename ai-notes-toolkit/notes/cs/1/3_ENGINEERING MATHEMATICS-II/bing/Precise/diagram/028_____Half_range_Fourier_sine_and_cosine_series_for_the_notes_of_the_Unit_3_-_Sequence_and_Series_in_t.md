### Half range Fourier sine and cosine series

In the subject of ENGINEERING MATHEMATICS-II, Unit 3 - Sequence and Series, one of the important topics is the Half range Fourier sine and cosine series.

A half-range Fourier series is a representation of a function using either only sine terms or only cosine terms, rather than a combination of both. This is useful when the function being represented is either odd or even, as the resulting series will be simpler and easier to work with.

The half-range Fourier sine series of an odd function f(x) defined on the interval [0, L] is given by:

f(x) = sum from n=1 to infinity of ((2/L) * integral from 0 to L of f(x) * sin((n * pi * x)/L) dx) * sin((n * pi * x)/L)

The half-range Fourier cosine series of an even function f(x) defined on the interval [0, L] is given by:

f(x) = a0/2 + sum from n=1 to infinity of (a_n * cos((n * pi * x)/L))

where a_n = (2/L) * integral from 0 to L of f(x) * cos((n * pi * x)/L) dx

These series can be used to represent a function on a given interval, and can be useful in solving problems in engineering and physics. It is important to note that the function being represented must be either odd or even for the half-range series to be valid.