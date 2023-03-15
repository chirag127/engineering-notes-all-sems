### Expansion of functions by Taylor’s and Maclaurin’s theorems for functions of one and two variables

- Taylor's theorem states that any infinitely differentiable function f(x) can be approximated by a polynomial of degree n, called the Taylor polynomial, in a neighborhood of a point a, where the coefficients of the polynomial are determined by the derivatives of f at a .
- The general form of the Taylor polynomial of degree n for f(x) at a is:

`Pn(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2/2! + ... + f^n(a)(x-a)^n/n!`

- The Taylor polynomial is the sum of the first n terms of the Taylor series, which is an infinite series that represents f(x) as a power series in (x-a). The Taylor series is:

`f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2/2! + ... + f^n(a)(x-a)^n/n! + ...`

- The difference between f(x) and Pn(x) is called the remainder term, which can be estimated by various formulas, such as the Lagrange form:

`Rn(x) = f^(n+1)(c)(x-a)^(n+1)/(n+1)!`

where c is some number between a and x.

- If the remainder term approaches zero as n increases, then the Taylor series converges to f(x) for all x in the interval of convergence .

- A special case of Taylor's theorem is Maclaurin's theorem, which applies when a = 0. The Maclaurin polynomial and series are:

`Pn(x) = f(0) + f'(0)x + f''(0)x^2/2! + ... + f^n(0)x^n/n!`

`f(x) = f(0) + f'(0)x + f''(0)x^2/2! + ... + f^n(0)x^n/n! + ...`

- Some common functions have well-known Maclaurin series, such as:

`e^x = 1 + x + x^2/2! + x^3/3! + ...`

`sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...`

`cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...`

`ln(1+x) = x - x^2/2 + x^3/3 - x^4/4 + ...`

- Taylor's and Maclaurin's theorems can be extended to functions of two variables f(x,y) by using partial derivatives and the binomial theorem. The Taylor polynomial of degree n for f(x,y) at (a,b) is:

`Pn(x,y) = f(a,b) + fx(a,b)(x-a) + fy(a,b)(y-b) + 1/2! [fxx(a,b)(x-a)^2 + 2fxy(a,b)(x-a)(y-b) + fyy(a,b)(y-b)^2] + ...`

- The Maclaurin polynomial of degree n for f(x,y) at (0,0) is:

`Pn(x,y) = f(0,0) + fx(0,0)x + fy(0,0)y + 1/2! [fxx(0,0)x^2 + 2fxy(0,0)xy + fyy(0,0)y^2] + ...`

- The remainder term for functions of two variables can also be estimated by various formulas, such as the Peano form:

`Rn(x,y) = o[(x-a)^n + (y-b)^n]`

where o means "order of magnitude" and implies that the remainder term is much smaller than the polynomial term as x and y approach a and b .