# Inverse Laplace Transform

- The inverse Laplace transform is a process of finding a function of time from its Laplace transform.
- The inverse Laplace transform of a function F(s) is denoted by L<sup>-1</sup>{F(s)} or f(t), where t is the time variable.
- The inverse Laplace transform can be obtained by using the following formula:

  L<sup>-1</sup>{F(s)} = f(t) = (1/2πi) ∫<sub>γ-i∞</sub><sup>γ+i∞</sup> F(s) e<sup>st</sup> ds

  where γ is a real constant such that all the singularities of F(s) lie to the left of the line Re(s) = γ, and the integral is taken along this line.

- The inverse Laplace transform can also be found by using the following properties:

  - Linearity: L<sup>-1</sup>{aF(s) + bG(s)} = af(t) + bg(t), where a and b are constants.
  - First shifting theorem: L<sup>-1</sup>{e<sup>-as</sup>F(s)} = f(t-a)u(t-a), where a is a constant and u(t) is the unit step function.
  - Second shifting theorem: L<sup>-1</sup>{F(s-a)} = e<sup>at</sup>f(t), where a is a constant.
  - Scaling theorem: L<sup>-1</sup>{F(as)} = (1/a)f(t/a), where a is a positive constant.
  - Convolution theorem: L<sup>-1</sup>{F(s)G(s)} = f(t) * g(t), where * denotes the convolution operation.

- The inverse Laplace transform of some common functions are:

  - L<sup>-1</sup>{1/s} = 1
  - L<sup>-1</sup>{1/s<sup>2</sup>} = t
  - L<sup>-1</sup>{1/s<sup>n</sup>} = t<sup>n-1</sup>/(n-1)!, where n is a positive integer.
  - L<sup>-1</sup>{e<sup>-as</sup>/s} = u(t-a)
  - L<sup>-1</sup>{s<sup>-1</sup> - e<sup>-as</sup>s<sup>-1</sup>} = 1 - u(t-a)
  - L<sup>-1</sup>{e<sup>-as</sup>/s<sup>2</sup>} = (t-a)u(t-a)
  - L<sup>-1</sup>{sin(at)/s<sup>2</sup> + a<sup>2</sup>} = sin(at)
  - L<sup>-1</sup>{cos(at)/s<sup>2</sup> + a<sup>2</sup>} = cos(at)
  - L<sup>-1</sup>{s/(s<sup>2</sup> + a<sup>2</sup>)} = cos(at)
  - L<sup>-1</sup>{a/(s<sup>2</sup> + a<sup>2</sup>)} = sin(at)