### Beta and Gamma Function and Their Properties

- The **gamma function** is a single variable function that generalizes the factorial function to positive real numbers and complex numbers. It is defined by the following integral:

$$\Gamma(z) = \int_0^\infty x^{z-1} e^{-x} dx$$

- The **beta function** is a dual variable function that is related to the gamma function by the following formula:

$$B(x,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$$

- The beta function can also be defined by the following integral:

$$B(x,y) = \int_0^1 t^{x-1} (1-t)^{y-1} dt$$

- Some properties of the gamma function are:

  - $\Gamma(n) = (n-1)!$ for any positive integer $n$.
  - $\Gamma(z+1) = z\Gamma(z)$ for any complex number $z$.
  - $\Gamma(1/2) = \sqrt{\pi}$.
  - $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$ for any complex number $z$.

- Some properties of the beta function are:

  - $B(x,y) = B(y,x)$ for any complex numbers $x$ and $y$.
  - $B(x,1) = B(1,x) = \frac{1}{x}$ for any complex number $x$.
  - $B(x,y) = \frac{x-1}{x+y-1} B(x-1,y) + \frac{y-1}{x+y-1} B(x,y-1)$ for any complex numbers $x$ and $y$.
  - $B(x,y) = \frac{\Gamma(x+y)}{\Gamma(x)\Gamma(y)} \int_0^\infty \frac{t^{x-1}}{(1+t)^{x+y}} dt$ for any complex numbers $x$ and $y$.

- The beta and gamma functions are useful for computing and representing various integrals, such as:

  - $\int_0^\infty x^{a-1} e^{-bx} dx = \frac{\Gamma(a)}{b^a}$ for any positive real numbers $a$ and $b$.
  - $\int_0^1 x^{a-1} (1-x)^{b-1} dx = B(a,b)$ for any positive real numbers $a$ and $b$.
  - $\int_0^\pi \sin^{2n-1}(\theta) \cos^{2m-1}(\theta) d\theta = \frac{1}{2} B(n,m)$ for any positive integers $n$ and $m$.

- The beta and gamma functions are also applied in various fields of mathematics and science, such as:

  - Calculus, where they are used to evaluate improper integrals and to express solutions of differential equations.
  - Probability and statistics, where they are used to define probability distributions, such as the gamma distribution, the beta distribution, and the Dirichlet distribution.
  - Number theory, where they are used to study the Riemann zeta function and the Dirichlet L-functions.
  - Physics, where they are used to model physical phenomena, such as quantum mechanics, thermodynamics, and scattering theory.