### Inverse Laplace Transform

- The inverse Laplace transform is a process of finding the original function from its Laplace transform .
- The inverse Laplace transform is denoted by L<sup>-1</sup> and has the following formula :

  L<sup>-1</sup>{F(s)} = f(t) = &int;<sub>&Gamma;</sub> F(s) e<sup>st</sup> ds

  where &Gamma; is a contour in the complex plane that separates the poles of F(s) from the singularities of e<sup>st</sup>.

- The inverse Laplace transform is a linear operation, which means that for any constants a and b, and any functions F(s) and G(s), the following property holds:

  L<sup>-1</sup>{aF(s) + bG(s)} = af(t) + bg(t)

- A necessary condition for the existence of the inverse Laplace transform is that the function F(s) must be absolutely integrable, which means the integral of the absolute value of F(s) over the whole real axis must converge.
- A sufficient condition for the existence of the inverse Laplace transform is that the function F(s) must be of exponential order, which means there exist constants M, c, and s<sub>0</sub> such that |F(s)| &le; Me<sup>cs</sup> for all s &ge; s<sub>0</sub> .
- The inverse Laplace transform can be used to solve differential equations by transforming them from the time domain to the frequency domain, where they become easier to manipulate, and then transforming them back to the time domain using the inverse Laplace transform .
- The inverse Laplace transform of a rational function F(s) = P(s)/Q(s), where P and Q are polynomials in s with no common factors, can be found by using partial fraction decomposition and then applying the inverse Laplace transform to each term.
- The inverse Laplace transform of some common functions are given in the following table  :

| F(s) | f(t) |
| --- | --- |
| 1/s | 1 |
| 1/s<sup>2</sup> | t |
| e<sup>-as</sup>/s | u<sub>a</sub>(t) |
| s<sup>-n</sup> | t<sup>n-1</sup>/(n-1)! |
| 1/(s-a) | e<sup>at</sup> |
| 1/(s<sup>2</sup> + a<sup>2</sup>) | sin(at)/a |
| s/(s<sup>2</sup> + a<sup>2</sup>) | cos(at) |
| 1/(s<sup>2</sup> - a<sup>2</sup>) | sinh(at)/a |
| s/(s<sup>2</sup> - a<sup>2</sup>) | cosh(at) |

where u<sub>a</sub>(t) is the unit step function defined as:

u<sub>a</sub>(t) = { 0, if t < a
                   { 1, if t &ge; a