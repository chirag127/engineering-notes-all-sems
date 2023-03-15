# Laplace Transform of Derivatives and Integrals

## Definition

The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency). It is useful for solving differential equations, integral equations, and other problems involving functions of time.

The Laplace transform of a function f(t) is defined as

L{f(t)} = F(s) = ∫<sub>0</sub><sup>∞</sup> f(t) e<sup>-st</sup> dt

where s is a complex variable and the integral is taken over the positive real axis.

## Properties

The Laplace transform has many properties that make it easier to manipulate and apply. Some of the most important ones are:

- Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)} for any constants a and b
- Shift in time: L{f(t-a)u(t-a)} = e<sup>-as</sup>F(s) where u(t) is the unit step function
- Shift in frequency: L{e<sup>at</sup>f(t)} = F(s-a)
- Scaling: L{f(at)} = (1/a)F(s/a) for any constant a ≠ 0
- Differentiation in time: L{f'(t)} = sF(s) - f(0) and L{f''(t)} = s<sup>2</sup>F(s) - sf(0) - f'(0)
- Differentiation in frequency: L{(-t)f(t)} = F'(s) and L{(-t<sup>n</sup>)f(t)} = F<sup>(n)</sup>(s)
- Integration in time: L{∫<sub>0</sub><sup>t</sup> f(τ) dτ} = (1/s)F(s)
- Integration in frequency: L{f(t)/t} = ∫<sub>s</sub><sup>∞</sup> F(σ) dσ
- Convolution: L{f(t) * g(t)} = F(s)G(s) where f(t) * g(t) = ∫<sub>0</sub><sup>t</sup> f(τ) g(t-τ) dτ
- Initial value theorem: lim<sub>t→0</sub> f(t) = lim<sub>s→∞</sub> sF(s) if f(t) and f'(t) are piecewise continuous and of exponential order
- Final value theorem: lim<sub>t→∞</sub> f(t) = lim<sub>s→0</sub> sF(s) if f(t) and f'(t) are piecewise continuous and of exponential order and lim<sub>t→∞</sub> f(t) exists

## Examples

Here are some examples of how to use the Laplace transform to solve differential equations and integral equations.

### Example 1: Solve y'' + 2y' + y = e<sup>-t</sup> with y(0) = 0 and y'(0) = 1

Taking the Laplace transform of both sides, we get

s<sup>2</sup>Y(s) - sy(0) - y'(0) + 2sY(s) - 2y(0) + Y(s) = 1/(s+1)

Substituting the initial conditions, we get

(s<sup>2</sup> + 2s + 1)Y(s) - 1 = 1/(s+1)

Solving for Y(s), we get

Y(s) = (1 + s)/(s+1)<sup>2</sup>

Using partial fraction decomposition, we get

Y(s) = 1/(s+1) - 1/(s+1)<sup>2</sup>

Taking the inverse Laplace transform, we get

y(t) = e<sup>-t</sup> - te<sup>-t</sup>

### Example 2: Solve y(t) = ∫<sub>0</sub><sup>t</sup> e<sup>-τ</sup> sin(t-τ) y(τ) dτ with y(0) = 1

Taking the Laplace transform of both sides, we get

Y(s) = L{∫<sub>0</sub