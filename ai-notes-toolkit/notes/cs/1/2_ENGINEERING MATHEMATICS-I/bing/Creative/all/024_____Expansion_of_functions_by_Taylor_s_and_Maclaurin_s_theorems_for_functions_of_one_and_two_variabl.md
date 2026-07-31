# Expansion of functions by Taylor’s and Maclaurin’s theorems for functions of one and two variables

- Taylor's theorem states that any infinitely differentiable function f(x) can be approximated by a polynomial of degree n, called the Taylor polynomial, near a point a, such that the error term (or remainder) goes to zero as n goes to infinity.
- The Taylor polynomial of degree n for f(x) at a is given by:

$$
P_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n
$$

- The Taylor series of f(x) at a is the infinite sum of the Taylor polynomials:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n
$$

- The Taylor series may or may not converge to the original function f(x), depending on the function and the point a. A proof is required to show that they are equal (or not equal) for a function under consideration.
- The Maclaurin series is a special case of the Taylor series, where the point a is zero. The Maclaurin series of f(x) at zero is given by:

$$
f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n
$$

- The Maclaurin series is useful for expanding functions that are symmetric or periodic around the origin, such as trigonometric, exponential, and logarithmic functions.
- Taylor's theorem can be generalized to functions of two or more variables, such as f(x,y). The Taylor polynomial of degree n for f(x,y) at (a,b) is given by:

$$
P_n(x,y) = \sum_{i=0}^{n} \sum_{j=0}^{n-i} \frac{1}{i!j!} \frac{\partial^{i+j} f}{\partial x^i \partial y^j}(a,b)(x-a)^i(y-b)^j
$$

- The Taylor series of f(x,y) at (a,b) is the infinite sum of the Taylor polynomials:

$$
f(x,y) = \sum_{n=0}^{\infty} \sum_{i=0}^{n} \sum_{j=0}^{n-i} \frac{1}{i!j!} \frac{\partial^{i+j} f}{\partial x^i \partial y^j}(a,b)(x-a)^i(y-b)^j
$$

- The Taylor series may or may not converge to the original function f(x,y), depending on the function and the point (a,b). A proof is required to show that they are equal (or not equal) for a function under consideration.
- The Maclaurin series for f(x,y) at (0,0) is a special case of the Taylor series, where the point (a,b) is zero. The Maclaurin series of f(x,y) at zero is given by:

$$
f(x,y) = \sum_{n=0}^{\infty} \sum_{i=0}^{n} \sum_{j=0}^{n-i} \frac{1}{i!j!} \frac{\partial^{i+j} f}{\partial x^i \partial y^j}(0,0)x^iy^j
$$

- The Maclaurin series is useful for expanding functions that are symmetric or periodic around the origin, such as trigonometric, exponential, and logarithmic functions of two variables.