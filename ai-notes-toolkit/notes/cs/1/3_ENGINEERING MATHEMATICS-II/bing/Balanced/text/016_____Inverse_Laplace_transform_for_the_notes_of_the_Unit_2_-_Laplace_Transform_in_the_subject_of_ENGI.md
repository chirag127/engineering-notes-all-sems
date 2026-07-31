### Inverse Laplace Transform

- The inverse Laplace transform is a process of finding a function of time from its Laplace transform.
- The inverse Laplace transform of a function F(s) is denoted by L<sup>-1</sup>{F(s)} or f(t), where t is the time variable.
- The inverse Laplace transform can be obtained by using the following formula:

  L<sup>-1</sup>{F(s)} = f(t) = (1/2πi) ∫<sub>γ-i∞</sub><sup>γ+i∞</sup> F(s) e<sup>st</sup> ds

  where γ is a real constant such that all the singularities of F(s) lie to the left of the line Re(s) = γ, and the integral is taken along this line.

- The inverse Laplace transform has the following properties:

  - Linearity: L<sup>-1</sup>{aF(s) + bG(s)} = af(t) + bg(t) for any constants a and b.
  - Initial value theorem: If f(t) is continuous and of exponential order, then

    lim<sub>s→∞</sub> sF(s) = f(0)

  - Final value theorem: If f(t) is continuous and of exponential order, and lim<sub>t→∞</sub> f(t) exists, then

    lim<sub>s→0</sub> sF(s) = lim<sub>t→∞</sub> f(t)

  - Convolution theorem: If F(s) and G(s) are the Laplace transforms of f(t) and g(t) respectively, then

    L<sup>-1</sup>{F(s)G(s)} = ∫<sub>0</sub><sup>t</sup> f(τ)g(t-τ) dτ

    which is called the convolution of f(t) and g(t).

- The inverse Laplace transform of some common functions are:

  - L<sup>-1</sup>{1/s} = 1 (unit step function)
  - L<sup>-1</sup>{1/s<sup>2</sup>} = t (ramp function)
  - L<sup>-1</sup>{e<sup>-as</sup>/s} = u<sub>a</sub>(t) (delayed unit step function)
  - L<sup>-1</sup>{s<sup>-n</sup>} = t<sup>n-1</sup>/(n-1)! for n = 1, 2, 3, ...
  - L<sup>-1</sup>{e<sup>-as</sup>s<sup>-n</sup>} = u<sub>a</sub>(t) t<sup>n-1</sup>/(n-1)! for n = 1, 2, 3, ...
  - L<sup>-1</sup>{1/(s-a)} = e<sup>at</sup>
  - L<sup>-1</sup>{1/(s<sup>2</sup>+a<sup>2</sup>)} = (1/a) sin(at)
  - L<sup>-1</sup>{s/(s<sup>2</sup>+a<sup>2</sup>)} = cos(at)
  - L<sup>-1</sup>{a/(s<sup>2</sup>+a<sup>2</sup>)} = sin(at)
  - L<sup>-1</sup>{(s-a)/(s<sup>2</sup>+a<sup>2</sup>)} = e<sup>at</sup> cos(at)
  - L<sup>-1</sup>{(s<sup>2</sup>-a<sup>2</sup>)/(s<sup>2</sup>+a<sup>2</sup>)<sup>2</sup>} = (1/2a) (t sin(at) + cos(at))

- The inverse Laplace transform of a rational function F(s) = P(s)/Q(s), where P and Q are polynomials in s with no common factors, can be found by using the following steps:

  - Find the partial fraction decomposition of F(s), i.e., write F(s) as a sum of simpler fractions of the form A/(s-a), B/(s-a)<sup>2</sup>, C/(s<sup