# Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function is a function that is zero for negative values of the argument and one for positive values. It is denoted by u(t) and defined as:

u(t) = {1 for t ≥ 0 0 for t < 0

- The unit step function can be used to model a switch that turns on or off at a certain time, or a signal that starts or stops at a certain time.

- The Laplace transform of the unit step function is given by :

L[u(t)] = ∫∞ 0u(t)e − stdt = [e − st − s]∞ 0 = 1 s

- The Laplace transform of a function f(t) multiplied by a unit step function u(t-c) that shifts the function to the right by c units is given by the time displacement theorem :

L[u(t-c)f(t-c)] = e − csL[f(t)]

- This theorem allows us to find the Laplace transform of piecewise continuous functions that are defined by different formulas for different intervals of t, by using the unit step function to indicate when each formula applies. For example, if f(t) is defined as:

f(t) = {t for 0 ≤ t < 2 2 for t ≥ 2

then we can write f(t) as:

f(t) = tu(t) + (2-t)u(t-2)

and find its Laplace transform as:

L[f(t)] = L[tu(t)] + L[(2-t)u(t-2)] = L[t]L[u(t)] + L[2-t]L[u(t-2)] = 1 s2 1 s + ( 2 s − 1 s2 ) e − 2s = 1 s2 + 2 s e − 2s − e − 2s s2

- The inverse Laplace transform of a function F(s) that contains terms of the form e − csG(s) can be found by using the inverse of the time displacement theorem, which states that :

L−1[e − csF(s)] = u(t-c)L−1[F(s-c)]

- This means that we can shift the function back to the left by c units by multiplying it by the unit step function u(t-c) and replacing s by s-c in the inverse Laplace transform. For example, if F(s) is given by:

F(s) = 1 s2 + 2 s e − 2s − e − 2s s2

then we can write F(s) as:

F(s) = 1 s2 + e − 2s ( 2 s − 1 s2 )

and find its inverse Laplace transform as:

L−1[F(s)] = L−1[1 s2 ] + L−1[e − 2s ( 2 s − 1 s2 )] = t + u(t-2)L−1[2 s − 1 s2 − 2] = t + u(t-2)(2L−1[1 s ] − L−1[1 s2 ] − 2L−1[1]) = t + u(t-2)(2 − t − 2) = t + u(t-2)(−t)

which is the same as f(t) defined above.