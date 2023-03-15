### Inverse Laplace Transform

- The inverse Laplace transform is a process of finding a function of time, f(t), from its Laplace transform, F(s).
- The inverse Laplace transform is denoted by L<sup>-1</sup>{F(s)} or f(t) = L<sup>-1</sup>{F(s)}.
- The inverse Laplace transform can be obtained by using the following methods:
  - Partial fraction decomposition
  - Completing the square
  - Convolution theorem
  - Residue theorem
  - Inverse Laplace transform tables
- The inverse Laplace transform has the following properties:
  - Linearity: L<sup>-1</sup>{aF(s) + bG(s)} = aL<sup>-1</sup>{F(s)} + bL<sup>-1</sup>{G(s)}
  - First shifting theorem: L<sup>-1</sup>{e<sup>-as</sup>F(s)} = f(t-a)u(t-a), where u(t) is the unit step function
  - Second shifting theorem: L<sup>-1</sup>{F(s-a)} = e<sup>at</sup>f(t)
  - Scaling theorem: L<sup>-1</sup>{F(cs)} = (1/c)f(t/c)
  - Differentiation theorem: L<sup>-1</sup>{sF(s) - f(0)} = f'(t)
  - Integration theorem: L<sup>-1</sup>{F(s)/s} = ∫<sub>0</sub><sup>t</sup> f(τ) dτ
  - Initial value theorem: lim<sub>s→∞</sub> sF(s) = f(0)
  - Final value theorem: lim<sub>s→0</sub> sF(s) = lim<sub>t→∞</sub> f(t)