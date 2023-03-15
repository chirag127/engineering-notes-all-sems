## Unit 2 - Laplace Transform

- The Laplace transform is a mathematical technique that converts a function of a real variable (usually time) into a function of a complex variable (usually frequency).
- The Laplace transform can be used to solve linear differential equations, analyze control systems, and study various physical phenomena such as electrical circuits, mechanical systems, and heat transfer.
- The Laplace transform of a function f(t) is defined as:

  L{f(t)} = F(s) = ∫∞0 f(t) e^(-st) dt

  where s is a complex variable of the form s = σ + jω, and the integral is taken over the positive real axis.

- The Laplace transform has some important properties, such as:

  - Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)} for any constants a and b
  - Shift in time: L{f(t-a)u(t-a)} = e^(-as)F(s) for any constant a, where u(t) is the unit step function
  - Shift in frequency: L{e^(at)f(t)} = F(s-a) for any constant a
  - Scaling: L{f(at)} = (1/a)F(s/a) for any constant a
  - Differentiation in time: L{f'(t)} = sF(s) - f(0)
  - Differentiation in frequency: L{(-t)f(t)} = F'(s)
  - Integration in time: L{∫t0 f(τ) dτ} = (1/s)F(s)
  - Convolution: L{f(t) * g(t)} = F(s)G(s), where f(t) * g(t) is the convolution of f(t) and g(t) defined as:

    f(t) * g(t) = ∫∞-∞ f(τ)g(t-τ) dτ

  - Initial value theorem: lim t→0 f(t) = lim s→∞ sF(s), if f(t) and f'(t) are both Laplace transformable
  - Final value theorem: lim t→∞ f(t) = lim s→0 sF(s), if f(t) and f'(t) are both Laplace transformable and lim t→∞ f(t) exists

- Some common Laplace transforms are:

  - L{1} = 1/s
  - L{e^(at)} = 1/(s-a)
  - L{sin(at)} = a/(s^2 + a^2)
  - L{cos(at)} = s/(s^2 + a^2)
  - L{t^n} = n!/(s^(n+1))
  - L{δ(t)} = 1, where δ(t) is the Dirac delta function
  - L{u(t)} = 1/s, where u(t) is the unit step function
  - L{r(t)} = 1/s^2, where r(t) is the unit ramp function