## Unit 2 - Laplace Transform

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform can be used to solve linear differential equations, analyze systems and signals, and study stability and control problems.
- The Laplace transform is defined as follows:

  - Let f(t) be a function of a real variable t, defined for all t ≥ 0. Then the Laplace transform of f(t), denoted by F(s), is given by

    - F(s) = L{f(t)} = ∫∞0 f(t)e^(-st) dt

  - where s is a complex variable of the form s = σ + jω, and e^(-st) is the kernel of the transform.

- The Laplace transform has some important properties, such as:

  - Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)}, where a and b are constants.
  - Shift in time: L{f(t - a)} = e^(-as)F(s), where a is a constant.
  - Shift in frequency: L{e^(at)f(t)} = F(s - a), where a is a constant.
  - Scaling: L{f(at)} = (1/a)F(s/a), where a is a nonzero constant.
  - Differentiation in time: L{f'(t)} = sF(s) - f(0), L{f''(t)} = s^2F(s) - sf(0) - f'(0), etc.
  - Differentiation in frequency: L{(-t)f(t)} = F'(s), L{t^nf(t)} = (-1)^nF^(n)(s), where n is a positive integer.
  - Integration in time: L{∫t0 f(τ) dτ} = (1/s)F(s), L{∫∞0 f(τ) dτ} = F(0).
  - Convolution: L{f(t) * g(t)} = F(s)G(s), where f(t) * g(t) = ∫t0 f(τ)g(t - τ) dτ is the convolution of f(t) and g(t).
  - Initial value theorem: lim t→0 f(t) = lim s→∞ sF(s), if f(t) and f'(t) are piecewise continuous on [0, ∞) and F(s) is defined for all s.
  - Final value theorem: lim t→∞ f(t) = lim s→0 sF(s), if f(t) and f'(t) are piecewise continuous on [0, ∞), F(s) is defined for all s, and all poles of F(s) have negative real parts.

- The inverse Laplace transform is the operation that recovers the original function f(t) from its Laplace transform F(s). It is denoted by L^(-1){F(s)} or f(t).
- The inverse Laplace transform can be computed by using partial fraction decomposition, completing the square, inverse trigonometric identities, and other algebraic techniques.
- The inverse Laplace transform can also be obtained by using the Bromwich integral, which is given by

  - f(t) = L^(-1){F(s)} = (1/2πj) ∫γ-j∞γ+j∞ F(s)e^(st) ds

  - where γ is a real constant such that F(s) is analytic for all s with Re(s) > γ, and the integral is taken along a vertical line in the complex plane.

- The inverse Laplace transform has the same properties as the Laplace transform, except that the roles of f(t) and F(s) are interchanged. For example, L^(-1){aF(s) + bG(s)} = af(t) + bg(t), where a and b are constants.