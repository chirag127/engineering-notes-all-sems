### Beta and Gamma Function and their Properties

The Beta and Gamma functions are special functions that have important applications in probability theory, statistics, and mathematical physics.

#### Gamma Function
- The Gamma function is defined as:
$$\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt$$
- The Gamma function is an extension of the factorial function to the complex plane, with the property that $\Gamma(n) = (n-1)!$ for all positive integers $n$.
- The Gamma function has the following properties:
  - $\Gamma(z+1) = z\Gamma(z)$
  - $\Gamma(1) = 1$
  - $\Gamma(1/2) = \sqrt{\pi}$
  - $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$

#### Beta Function
- The Beta function is defined as:
$$B(x,y) = \int_0^1 t^{x-1}(1-t)^{y-1}dt$$
- The Beta function is related to the Gamma function by the following identity:
$$B(x,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$$
- The Beta function has the following properties:
  - $B(x,y) = B(y,x)$
  - $B(x,1) = \frac{1}{x}$
  - $B(x,y) = \frac{(x-1)!(y-1)!}{(x+y-1)!}$ for positive integers $x$ and $y$.

These are some of the basic properties of the Beta and Gamma functions. They are used in the study of multiple integration in the subject of Engineering Mathematics-I. It is important to understand these functions and their properties in order to apply them effectively in solving problems.