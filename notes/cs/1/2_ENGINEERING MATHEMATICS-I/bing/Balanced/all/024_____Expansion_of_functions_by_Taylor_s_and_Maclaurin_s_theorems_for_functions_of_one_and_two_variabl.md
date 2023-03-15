# Expansion of functions by Taylor’s and Maclaurin’s theorems for functions of one and two variables

- Taylor's theorem states that any infinitely differentiable function f(x) can be approximated by a polynomial of degree n, called the Taylor polynomial, near a point a, such that the error term goes to zero as n goes to infinity    .
- The Taylor polynomial of degree n for f(x) at a is given by:

$$
P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n
$$

- The Taylor series for f(x) at a is the infinite sum of the Taylor polynomials:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n
$$

- The remainder term, or the error of the approximation, is given by:

$$
R_n(x) = f(x) - P_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}
$$

where c is some number between a and x .

- A special case of Taylor's theorem is Maclaurin's theorem, which applies when a = 0. The Maclaurin polynomial and series are given by:

$$
P_n(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n
$$

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n
$$

- Taylor's and Maclaurin's theorems can be extended to functions of two variables f(x,y) by using partial derivatives and binomial expansions. The Taylor polynomial of degree n for f(x,y) at (a,b) is given by:

$$
P_n(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b) + \frac{1}{2!}(f_{xx}(a,b)(x-a)^2 + 2f_{xy}(a,b)(x-a)(y-b) + f_{yy}(a,b)(y-b)^2) + \cdots
$$

- The Taylor series for f(x,y) at (a,b) is the infinite sum of the Taylor polynomials:

$$
f(x,y) = \sum_{n=0}^{\infty} \sum_{k=0}^n \frac{f_{x^ky^{n-k}}(a,b)}{k!(n-k)!}(x-a)^k(y-b)^{n-k}
$$

- The remainder term, or the error of the approximation, is given by:

$$
R_n(x,y) = f(x,y) - P_n(x,y) = \frac{1}{(n+1)!} \sum_{k=0}^{n+1} \binom{n+1}{k} f_{x^ky^{n+1-k}}(c,d)(x-a)^k(y-b)^{n+1-k}
$$

where (c,d) is some point in the region bounded by (a,b) and (x,y) .

- A special case of Taylor's theorem for two variables is Maclaurin's theorem, which applies when (a,b) = (0,0). The Maclaurin polynomial and series are given by:

$$
P_n(x,y) = f(0,0) + f_x(0,0)x + f_y(0,0)y + \frac{1}{2!}(f_{xx}(0,0)x^2 + 2f_{xy}(0,0)xy + f_{yy}(0,0)y^2) + \cdots
$$

$$
f(x,y) = \sum_{n=0}^{\infty} \sum_{