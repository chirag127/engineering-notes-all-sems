### Beta and Gamma Function and Their Properties

The beta and gamma functions are special functions that are widely used in mathematics, especially in calculus, differential equations, complex analysis, and probability theory. They are defined by integrals that involve powers and exponentials of the variables.

The gamma function is a single variable function that generalizes the factorial function to all positive real numbers and complex numbers (except the negative integers). It is denoted by $\Gamma(z)$ and defined by the integral

$$\Gamma(z) = \int_0^\infty t^{z-1} e^{-t} dt, \quad \text{for } \operatorname{Re}(z) > 0$$

The beta function is a dual variable function that is related to the gamma function by a simple formula. It is denoted by $B(x,y)$ and defined by the integral

$$B(x,y) = \int_0^1 t^{x-1} (1-t)^{y-1} dt, \quad \text{for } x,y > 0$$

Some of the properties of the beta and gamma functions are:

- The gamma function is symmetric, meaning that $\Gamma(z) = \Gamma(1-z)$ for all $z$.
- The gamma function satisfies the recurrence relation $\Gamma(z+1) = z \Gamma(z)$ for all $z$, which implies that $\Gamma(n) = (n-1)!$ for all positive integers $n$.
- The gamma function has poles at the negative integers, meaning that $\Gamma(z)$ becomes infinite when $z$ is a negative integer. The residue at each pole is given by $\operatorname{Res}(\Gamma,z) = \frac{(-1)^n}{n!}$ for $z = -n$, where $n$ is a positive integer.
- The gamma function is analytic on the complex plane except at the negative integers, meaning that it has a well-defined derivative at every point except the poles. The derivative is given by $\Gamma'(z) = \Gamma(z) \psi(z)$, where $\psi(z)$ is the digamma function, defined by $\psi(z) = \frac{\Gamma'(z)}{\Gamma(z)}$.
- The beta function is symmetric, meaning that $B(x,y) = B(y,x)$ for all $x,y$.
- The beta function is related to the gamma function by the formula $B(x,y) = \frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}$ for all $x,y$.
- The beta function is also related to the binomial coefficients by the formula $B(x,y) = \frac{(x-1)! (y-1)!}{(x+y-1)!}$ for all positive integers $x,y$.
- The beta function is analytic on the positive quadrant of the complex plane, meaning that it has a well-defined derivative at every point where $x,y > 0$. The derivative is given by $B'(x,y) = B(x,y) (\psi(x) + \psi(y) - \psi(x+y))$, where $\psi(z)$ is the digamma function.