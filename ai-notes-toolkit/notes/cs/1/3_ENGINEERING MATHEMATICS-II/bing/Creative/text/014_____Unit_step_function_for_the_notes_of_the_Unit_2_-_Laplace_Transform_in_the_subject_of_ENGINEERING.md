### Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function, also known as the Heaviside function, is a discontinuous function that is zero for negative arguments and one for positive arguments. It is denoted by u(t) and defined as:

u(t) = {1 for t ≥ 0 0 for t < 0

- The unit step function can be used to model the switching behavior of circuits, systems, and signals. It can also be used to construct piecewise continuous functions by multiplying them with different unit step functions.

- The Laplace transform of the unit step function is given by :

L[u(t)] = ∫∞ 0u(t)e − stdt = ∫∞ 0e − stdt = [e − st − s]∞ 0 = 1 s

- The Laplace transform of a unit step function shifted by a constant a is given by:

L[u(t − a)] = e − as s

- This result can be derived using the time displacement theorem, which states that if F(s) is the Laplace transform of f(t), then e − as F(s) is the Laplace transform of u(t − a)f(t − a).

- The Laplace transform of a piecewise continuous function can be obtained by using the linearity property and the Laplace transform of the unit step function. For example, if f(t) is defined as:

f(t) = {t for 0 ≤ t < 2 2 for 2 ≤ t < 4 4 − t for 4 ≤ t < 6 0 for t ≥ 6

- Then f(t) can be written as:

f(t) = t[u(t) − u(t − 2)] + 2[u(t − 2) − u(t − 4)] + (4 − t)[u(t − 4) − u(t − 6)]

- And the Laplace transform of f(t) is:

L[f(t)] = L[t[u(t) − u(t − 2)]] + L[2[u(t − 2) − u(t − 4)]] + L[(4 − t)[u(t − 4) − u(t − 6)]]

- Using the linearity property and the time displacement theorem, we get:

L[f(t)] = L[t] − e − 2s L[t] + 2e − 2s s − 2e − 4s s + e − 4s L[4 − t] − e − 6s L[4 − t]

- Simplifying, we get:

L[f(t)] = 1 s2 − e − 2s s2 + 2 s (e − 2s − e − 4s) + 4 s (e − 4s − e − 6s) − 1 s2 (e − 4s − e − 6s)

- This is the Laplace transform of the piecewise continuous function f(t).

- References:

: https://www.intmath.com/laplace-transformation/4-transform-unit-step-function.php

: https://www.tutorialspoint.com/laplace-transform-of-unit-impulse-function-and-unit-step-function

: http://www.personal.psu.edu/sxt104/class/Math251/Notes-LT2.pdf

: https://www.khanacademy.org/math/differential-equations/laplace-transform/properties-of-laplace-transform/v/laplace-transform-of-the-unit-step-function

: https://math.libretexts.org/Courses/Monroe_Community_College/MTH_225_Differential_Equations/8%3A_Laplace_Transforms/8.4%3A_The_Unit_Step_Function