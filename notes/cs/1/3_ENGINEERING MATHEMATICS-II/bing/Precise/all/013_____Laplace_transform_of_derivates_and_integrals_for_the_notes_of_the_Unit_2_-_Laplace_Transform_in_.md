# Laplace Transform of Derivatives and Integrals

## Laplace Transform of Derivatives

The Laplace transform of the first derivative of a function `f(t)` is given by:

`L{f'(t)} = sF(s) - f(0)`

where `F(s)` is the Laplace transform of `f(t)` and `f(0)` is the initial value of the function.

Similarly, the Laplace transform of the second derivative of a function `f(t)` is given by:

`L{f''(t)} = s^2F(s) - sf(0) - f'(0)`

where `f'(0)` is the initial value of the first derivative of the function.

In general, the Laplace transform of the `n`-th derivative of a function `f(t)` is given by:

`L{f^(n)(t)} = s^nF(s) - s^(n-1)f(0) - s^(n-2)f'(0) - ... - f^(n-1)(0)`

## Laplace Transform of Integrals

The Laplace transform of the integral of a function `f(t)` is given by:

`L{∫f(t)dt} = F(s)/s + C/s`

where `C` is the constant of integration.

Similarly, the Laplace transform of the definite integral of a function `f(t)` from `0` to `t` is given by:

`L{∫[0,t]f(τ)dτ} = F(s)/s`

In general, the Laplace transform of the `n`-th integral of a function `f(t)` is given by:

`L{∫[0,t]...∫[0,t]f(τ)dτ...dτ} = F(s)/s^n + C/s^n`

where `C` is the constant of integration.

These are the basic formulas for the Laplace transform of derivatives and integrals, which are important concepts in the study of Laplace Transform in the subject of Engineering Mathematics-II. It is important to understand and memorize these formulas for solving problems and for exams.