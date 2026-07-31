### Beta and Gamma Function and Their Properties

- Beta and gamma functions are special functions in mathematics that are useful for integration and factorial generalization.
- Gamma function is a single variable function defined as:

$$\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt$$

- Beta function is a dual variable function defined as:

$$B(x,y) = \int_0^1 t^{x-1} (1-t)^{y-1} dt$$

- Some properties of beta and gamma functions are:

  - Symmetry: $B(x,y) = B(y,x)$ and $\Gamma(x) = \Gamma(x+1)/x$
  - Relationship: $B(x,y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$
  - Binomial coefficients: $B(n+1,m+1) = \frac{n!m!}{(n+m+1)!}$ for non-negative integers $n$ and $m$
  - Recurrence: $\Gamma(x+1) = x\Gamma(x)$ and $B(x+1,y) = \frac{x}{x+y}B(x,y)$
  - Special values: $\Gamma(1) = 1$, $\Gamma(1/2) = \sqrt{\pi}$, $B(1,y) = \frac{1}{y}$, and $B(1/2,1/2) = \pi$