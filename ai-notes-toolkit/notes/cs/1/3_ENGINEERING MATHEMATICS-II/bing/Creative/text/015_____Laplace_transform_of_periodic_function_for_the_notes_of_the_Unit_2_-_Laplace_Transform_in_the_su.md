### Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period. For example, a sine wave, a square wave, and a sawtooth wave are periodic functions.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- Let f(t) be a periodic function with period T, such that f(t) = f(t+nT) for any integer n and for all t > 0. Then, the Laplace transform of f(t) is given by:

  L{f(t)} = F(s) = (1-e^(-sT))^-1 ∫_0^T f(t) e^(-st) dt

  where F_1(s) = ∫_0^T f(t) e^(-st) dt is the Laplace transform of one cycle of the function.

- The formula can be derived as follows:

  L{f(t)} = ∫_0^∞ f(t) e^(-st) dt

  = ∫_0^T f(t) e^(-st) dt + ∫_T^2T f(t) e^(-st) dt + ∫_2T^3T f(t) e^(-st) dt + ...

  = ∫_0^T f(t) e^(-st) dt + e^(-sT) ∫_0^T f(t+T) e^(-st) dt + e^(-2sT) ∫_0^T f(t+2T) e^(-st) dt + ...

  = ∫_0^T f(t) e^(-st) dt + e^(-sT) ∫_0^T f(t) e^(-st) dt + e^(-2sT) ∫_0^T f(t) e^(-st) dt + ...

  = (1 + e^(-sT) + e^(-2sT) + ...) ∫_0^T f(t) e^(-st) dt

  = (1-e^(-sT))^-1 ∫_0^T f(t) e^(-st) dt

  = F(s)

- The Laplace transform of a periodic function can be used to solve differential equations with periodic forcing functions, such as harmonic oscillators, RLC circuits, and heat conduction problems.