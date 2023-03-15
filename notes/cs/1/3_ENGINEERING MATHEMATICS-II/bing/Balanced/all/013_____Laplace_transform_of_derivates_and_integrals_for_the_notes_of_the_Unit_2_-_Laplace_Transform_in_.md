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
- Derivative in time: L{f'(t)} = sF(s) - f(0)
- Derivative in frequency: L{(-t)f(t)} = F'(s)
- Integral in time: L{∫<sub>0</sub><sup>t</sup> f(τ) dτ} = (1/s)F(s)
- Integral in frequency: L{f(t)/t} = ∫<sub>s</sub><sup>∞</sup> F(σ) dσ
- Convolution: L{f(t) * g(t)} = F(s)G(s) where * denotes the convolution operation
- Initial value theorem: lim<sub>t→0</sub> f(t) = lim<sub>s→∞</sub> sF(s) if f(t) and f'(t) are of exponential order
- Final value theorem: lim<sub>t→∞</sub> f(t) = lim<sub>s→0</sub> sF(s) if f(t) and f'(t) are of exponential order and all the poles of F(s) are in the left half-plane

## Examples

Here are some examples of how to use the Laplace transform to find the solutions of differential equations and integral equations.

### Example 1: Differential equation

Solve the differential equation y'' + 2y' + y = e<sup>-t</sup> with y(0) = 0 and y'(0) = 1.

Solution:

Taking the Laplace transform of both sides, we get

L{y'' + 2y' + y} = L{e<sup>-t</sup>}

Using the properties of linearity and derivative in time, we get

s<sup>2</sup>Y(s) - sy(0) - y'(0) + 2sY(s) - 2y(0) + Y(s) = (1/s+1)

Substituting the initial conditions y(0) = 0 and y'(0) = 1, we get

(s<sup>2</sup> + 2s + 1)Y(s) - 1 = (1/s+1)

Solving for Y(s), we get

Y(s) = (1 + s)/((s+1)(s<sup>2</sup> + 2s + 1))

Using partial fraction decomposition, we get

Y(s) = (1/2)(1/s+1) + (1/2)(1/s+1)<sup>2</sup> - (1/s<sup>2</sup> + 2s + 1)

Taking the inverse Laplace transform of both sides, we get

y(t) = (1/2)e<sup>-t</sup> + (1/2)t e<sup>-t</sup> - e<sup>-t</sup> cos t

This is the solution of the differential equation.

### Example 2: Integral equation

Solve the integral equation y(t) = 2 + ∫<sub>0</sub><sup>t</sup> (t -