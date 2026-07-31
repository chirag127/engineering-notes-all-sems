## Unit 2 - Laplace Transform

The Laplace Transform is a powerful mathematical tool used to solve differential equations and evaluate integrals. It is named after the French mathematician Pierre-Simon Laplace.

1. Definition: The Laplace Transform of a function f(t) is defined as:

    L{f(t)} = F(s) = ∫[0,∞] e^(-st)f(t)dt

    where s is a complex number.

2. Properties: The Laplace Transform has several useful properties, including linearity, time-shifting, and frequency-shifting.

3. Inverse Laplace Transform: The Inverse Laplace Transform is used to recover the original function f(t) from its Laplace Transform F(s). It is defined as:

    f(t) = L^(-1){F(s)} = (1/2πi) ∫[γ-i∞,γ+i∞] e^(st)F(s)ds

    where γ is a real number chosen such that all singularities of F(s) lie to the left of the line Re(s) = γ.

4. Applications: The Laplace Transform is widely used in engineering, physics, and other fields to solve differential equations, evaluate integrals, and model systems.

5. Example: Consider the differential equation y'' + y = sin(t) with initial conditions y(0) = 0 and y'(0) = 0. Taking the Laplace Transform of both sides, we get:

    s^2Y(s) - sy(0) - y'(0) + Y(s) = L{sin(t)}

    Substituting the initial conditions and solving for Y(s), we get:

    Y(s) = L{sin(t)}/(s^2 + 1)

    Taking the Inverse Laplace Transform, we find the solution to the differential equation:

    y(t) = L^(-1){L{sin(t)}/(s^2 + 1)} = sin(t)