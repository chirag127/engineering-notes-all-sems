# Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function is a function that is zero for negative values of the argument and one for positive values. It is denoted by u(t) and defined as:

u(t) = {1 for t ≥ 0 0 for t < 0

- The unit step function can be used to model a switch that turns on or off at a certain time. For example, u(t - a) is a function that is zero for t < a and one for t > a, meaning that the switch turns on at time a.

- The Laplace transform of the unit step function is given by :

L[u(t)] = ∫∞ 0u(t)e − stdt = ∫∞ 0e − stdt = [e − st − s]∞ 0 = 1 s

- The Laplace transform of a shifted unit step function is given by :

L[u(t - a)] = ∫∞ 0u(t - a)e − stdt = ∫a ∞e − stdt = [e − st − s]∞ a = e − as s

- This result can be generalized to the time displacement theorem, which states that if F(s) is the Laplace transform of f(t), then:

L[u(t - a)f(t - a)] = e − as F(s)

- The time displacement theorem can be used to find the Laplace transform of piecewise continuous functions, which are functions that are continuous on each interval of a finite partition of the real line, and have finite jumps at the endpoints of the intervals. For example, if f(t) is defined as:

f(t) = {t for 0 ≤ t < 1 2 for 1 ≤ t < 2 3 − t for 2 ≤ t < 3 0 for t ≥ 3

- Then f(t) can be written as a linear combination of shifted unit step functions and their products:

f(t) = tu(1 - t) + 2u(t - 1) - tu(t - 1) + (3 - t)u(t - 2) - (3 - t)u(t - 3)

- Applying the time displacement theorem to each term, we get the Laplace transform of f(t):

L[f(t)] = L[tu(1 - t)] + L[2u(t - 1)] - L[tu(t - 1)] + L[(3 - t)u(t - 2)] - L[(3 - t)u(t - 3)]

= e − s s2 + 2e − s s - e − s s2 + e − 2s s2 - 3e − 2s s + e − 2s s2 - e − 3s s2 + 3e − 3s s

= 1 s2 - 2e − s s2 + 2e − 2s s2 - e − 3s s2

- The Laplace transform of piecewise continuous functions can be used to solve differential equations with discontinuous forcing functions, such as the following example:

y′′ + 2y′ + 2y = f(t), y(0) = 0, y′(0) = 0

where f(t) is the same function as above. Taking the Laplace transform of both sides, we get:

s2Y(s) + 2sY(s) + 2Y(s) = 1 s2 - 2e − s s2 + 2e − 2s s2 - e − 3s s2

Solving for Y(s), we get:

Y(s) = 1 s2 + 2s + 2 - 2e − s s2 + 2s + 2 + 2e − 2s s2 + 2s + 2 - e − 3s s2 + 2s + 2

Using partial fraction decomposition and inverse Laplace transform, we get the solution for y(t):

y(t) = 1 2 (1 − e − t cos t) − 1 2 e − t sin t + u(t − 1)(e − (t −