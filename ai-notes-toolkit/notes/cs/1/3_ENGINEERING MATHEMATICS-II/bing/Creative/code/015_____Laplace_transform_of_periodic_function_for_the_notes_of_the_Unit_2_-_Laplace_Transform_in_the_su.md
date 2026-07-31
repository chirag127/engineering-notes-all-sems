# Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- Let f(t) be a periodic function with period T, such that f(t) = f(t+nT) for any integer n and for all t > 0. Then, the Laplace transform of f(t) is given by:

  L{f(t)} = F(s) = (1-e^(-sT))^-1 int_0^T f(t) e^(-st) dt

  where int_0^T f(t) e^(-st) dt is the Laplace transform of one cycle of the function.

- The formula can be derived as follows:

  L{f(t)} = int_0^infty f(t) e^(-st) dt

  = sum_{n=0}^infty int_nT^(n+1)T f(t) e^(-st) dt

  = sum_{n=0}^infty int_0^T f(t+nT) e^(-s(t+nT)) dt

  = sum_{n=0}^infty e^(-snT) int_0^T f(t) e^(-st) dt

  = int_0^T f(t) e^(-st) dt sum_{n=0}^infty (e^(-sT))^n

  = int_0^T f(t) e^(-st) dt (1-e^(-sT))^-1

  = F(s)

- Some examples of Laplace transform of periodic functions are:

  - L{sin(wt)} = w/(s^2+w^2) for w > 0, where sin(wt) is a periodic function with period 2pi/w.

  - L{u(t)-u(t-T)} = (1-e^(-sT))/s for T > 0, where u(t) is the unit step function and u(t)-u(t-T) is a periodic function with period T.

  - L{t mod T} = (T-sT^2/2)/(s^2(1-e^(-sT))) for T > 0, where t mod T is the remainder of t divided by T and is a periodic function with period T.