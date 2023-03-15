## Unit 2 - Laplace Transform

The Laplace Transform is a mathematical technique used to solve differential equations and to represent signals in the frequency domain. It is named after Pierre-Simon Laplace, who introduced the transform in his work on probability theory.

The Laplace Transform of a function `f(t)` is defined as:

```
F(s) = L{f(t)} = ∫[0,∞] e^(-st) f(t) dt
```

where `s` is a complex number and `F(s)` is the Laplace Transform of `f(t)`.

Some properties of the Laplace Transform include:

1. Linearity: `L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)}`
2. Time shifting: `L{f(t-a)} = e^(-as)F(s)`
3. Frequency shifting: `L{e^(at)f(t)} = F(s-a)`
4. Scaling: `L{f(at)} = (1/a)F(s/a)`
5. Derivatives: `L{f'(t)} = sF(s) - f(0)`

The Laplace Transform is commonly used in engineering and physics to solve differential equations and to analyze systems in the frequency domain. It is also used in control theory, signal processing, and probability theory.

The inverse Laplace Transform is used to recover the original function `f(t)` from its Laplace Transform `F(s)`. It is defined as:

```
f(t) = L^(-1){F(s)} = (1/2πi) ∫[γ-i∞,γ+i∞] e^(st) F(s) ds
```

where `γ` is a real number such that all singularities of `F(s)` lie to the left of the line `Re(s) = γ`. The inverse Laplace Transform is commonly computed using partial fraction decomposition or by using tables of Laplace Transforms.