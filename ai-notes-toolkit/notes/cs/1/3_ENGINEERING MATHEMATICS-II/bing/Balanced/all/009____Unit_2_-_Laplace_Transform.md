## Unit 2 - Laplace Transform

- The Laplace transform is a mathematical technique that converts a function of time, f(t), into a function of a complex variable, F(s), where s is the Laplace variable.
- The Laplace transform is useful for solving linear differential equations with constant coefficients, as well as for analyzing the behavior of linear systems in the frequency domain.
- The Laplace transform of a function f(t) is defined as:

  `F(s) = L{f(t)} = ∫<sub>0</sub><sup>∞</sup> f(t) e<sup>-st</sup> dt`

  where s is a complex variable of the form s = σ + jω, and j is the imaginary unit.

- The inverse Laplace transform of a function F(s) is defined as:

  `f(t) = L<sup>-1</sup>{F(s)} = (1/2πj) ∫<sub>γ-j∞</sub><sup>γ+j∞</sup> F(s) e<sup>st</sup> ds`

  where γ is a real constant such that all the singularities of F(s) lie to the left of the line Re(s) = γ.

- The Laplace transform has some important properties, such as:

  - Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)}
  - Shifting in time: L{f(t-a)u(t-a)} = e<sup>-as</sup>F(s), where u(t) is the unit step function
  - Shifting in frequency: L{e<sup>at</sup>f(t)} = F(s-a)
  - Scaling: L{f(at)} = (1/a)F(s/a)
  - Differentiation: L{f'(t)} = sF(s) - f(0), L{f''(t)} = s<sup>2</sup>F(s) - sf(0) - f'(0), etc.
  - Integration: L{∫<sub>0</sub><sup>t</sup> f(τ) dτ} = (1/s)F(s)
  - Convolution: L{f(t) * g(t)} = F(s)G(s), where * denotes the convolution operation
  - Initial value theorem: lim<sub>t→0</sub> f(t) = lim<sub>s→∞</sub> sF(s), if f(t) and f'(t) are both Laplace transformable
  - Final value theorem: lim<sub>t→∞</sub> f(t) = lim<sub>s→0</sub> sF(s), if f(t) and sF(s) are both Laplace transformable and all the singularities of sF(s) are in the left half-plane

- Some common Laplace transforms are:

  - L{1} = 1/s
  - L{t<sup>n</sup>} = n!/s<sup>n+1</sup>, n = 0, 1, 2, ...
  - L{e<sup>at</sup>} = 1/(s-a)
  - L{sin(at)} = a/(s<sup>2</sup>+a<sup>2</sup>)
  - L{cos(at)} = s/(s<sup>2</sup>+a<sup>2</sup>)
  - L{sinh(at)} = a/(s<sup>2</sup>-a<sup>2</sup>)
  - L{cosh(at)} = s/(s<sup>2</sup>-a<sup>2</sup>)
  - L{δ(t)} = 1, where δ(t) is the Dirac delta function
  - L{u(t)} = 1/s, where u(t) is the unit step function
  - L{r(t)} = 1/s<sup>2</sup>, where r(t) is the unit ramp function
  - L{t<sup>n</sup>e<sup>at</sup>} = n!/((s-a)<sup>n+1</sup>), n = 0, 1, 2, ...
  - L{e<sup>at</sup>sin(bt)} = b/((s-a)<sup>2</sup>+b<sup>2</sup>)
  - L{e<sup>at</sup>cos(bt)} = (s-a)/((s-a)<sup>2</sup>+b<sup