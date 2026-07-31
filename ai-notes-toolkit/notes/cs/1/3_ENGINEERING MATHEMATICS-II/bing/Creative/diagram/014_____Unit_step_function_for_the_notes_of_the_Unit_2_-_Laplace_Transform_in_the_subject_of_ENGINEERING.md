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

- Then, f(t) can be written as a linear combination of unit step functions as:

f(t) = tu(2 − t) + 2u(t − 2) − 2u(t − 4) + (4 − t)u(t − 4) − (4 − t)u(t − 6)

- And the Laplace transform of f(t) can be found by applying the linearity property and the time displacement theorem as:

L[f(t)] = L[tu(2 − t)] + 2L[u(t − 2)] − 2L[u(t − 4)] + L[(4 − t)u(t − 4)] − L[(4 − t)u(t − 6)]

= e − 2s L[t] + 2e − 2s L[1] − 2e − 4s L[1] + e − 4s L[4 − t] − e − 6s L[4 − t]

= e − 2s 1 s2 + 2e − 2s 1 s − 2e − 4s 1 s + e − 4s (4 s − 1 s2 ) − e − 6s (4 s − 1 s2 )

= 1 s2 − e − 2s (1 s2 − 2 s ) − e − 4s (1 s2 − 8 s + 16) + e − 6s (1 s2 − 8 s + 16)