### Expansion of functions by Taylor’s and Maclaurin’s theorems for functions of one and two variables

- Taylor's theorem states that any infinitely differentiable function f(x) can be approximated by a polynomial of degree n, called the Taylor polynomial, near a point a, as follows:

`f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2/2! + ... + f^n(a)(x-a)^n/n! + Rn(x)`

where Rn(x) is the remainder term that measures the error of the approximation.

- The Taylor polynomial of degree n can be written in a compact form using the sigma notation as follows:

`Pn(x) = sum_(k=0)^n f^k(a)(x-a)^k/k!`

where f^k(a) denotes the kth derivative of f at a.

- The Maclaurin series is a special case of the Taylor series when a = 0. It can be written as follows:

`f(x) = f(0) + f'(0)x + f''(0)x^2/2! + ... + f^n(0)x^n/n! + Rn(x)`

or

`Pn(x) = sum_(k=0)^n f^k(0)x^k/k!`

- Some common Maclaurin series are:

`e^x = sum_(k=0)^infty x^k/k!`

`sin x = sum_(k=0)^infty (-1)^k x^(2k+1)/(2k+1)!`

`cos x = sum_(k=0)^infty (-1)^k x^(2k)/(2k)!`

`ln(1+x) = sum_(k=1)^infty (-1)^(k+1) x^k/k`

`(1+x)^n = sum_(k=0)^infty (n,k) x^k`

where (n,k) is the binomial coefficient.

- For functions of two variables f(x,y), the Taylor polynomial of degree n near a point (a,b) can be written as follows:

`Pn(x,y) = sum_(k=0)^n 1/k! sum_(i+j<=k) f^i,j(a,b)(x-a)^i(y-b)^j`

where f^i,j(a,b) denotes the mixed partial derivative of f with respect to x i times and y j times at (a,b).

- The Maclaurin polynomial of degree n for functions of two variables is obtained by setting a = b = 0 in the above formula:

`Pn(x,y) = sum_(k=0)^n 1/k! sum_(i+j<=k) f^i,j(0,0)x^iy^j`

- Some examples of Maclaurin polynomials of degree 2 for functions of two variables are:

`f(x,y) = e^(x+y)`

`P2(x,y) = 1 + x + y + x^2/2 + xy + y^2/2`

`f(x,y) = sin(x+y)`

`P2(x,y) = x + y - x^2/2 - xy - y^2/2`

`f(x,y) = ln(1+x+y)`

`P2(x,y) = x + y - x^2/2 - xy - y^2/2`