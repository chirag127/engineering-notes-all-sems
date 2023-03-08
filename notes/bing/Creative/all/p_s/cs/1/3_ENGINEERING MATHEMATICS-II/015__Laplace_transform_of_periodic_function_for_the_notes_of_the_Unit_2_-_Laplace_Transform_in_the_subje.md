### Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- If f(t) is a periodic function with period T, then f(t) = f(t+nT) for any integer n. Therefore, we can write f(t) as a sum of shifted functions:

  f(t) = f(t) + f(t-T) + f(t-2T) + ...

- Applying the Laplace transform to both sides, we get:

  F(s) = F(s) + e^(-sT)F(s) + e^(-2sT)F(s) + ...

- This is an infinite geometric series with common ratio e^(-sT). The sum of the series is:

  F(s) = F(s) / (1 - e^(-sT))

- Therefore, the Laplace transform of a periodic function with period T is given by:

  F(s) = (1 / (1 - e^(-sT))) * L{f(t)}

  where L{f(t)} is the Laplace transform of one cycle of the function.

- Example: Find the Laplace transform of the periodic function f(t) shown below, where T = 2.

  f(t) = |t| for 0 <= t < 2

  f(t) = f(t+2) for t >= 2

  ![periodic function](https://www.intmath.com/laplace-transformation/img/periodic-abs-t.gif)

- Solution: To find the Laplace transform of f(t), we need to find the Laplace transform of one cycle of the function, which is f(t) for 0 <= t < 2. This is a piecewise continuous function, so we can use the formula:

  L{f(t)} = integral from 0 to 2 of f(t) * e^(-st) dt

  L{f(t)} = integral from 0 to 1 of t * e^(-st) dt + integral from 1 to 2 of (2-t) * e^(-st) dt

  L{f(t)} = [(t/s) - (1/s^2)] * e^(-st) evaluated from 0 to 1 + [(-t/s) - (1/s^2)] * e^(-st) evaluated from 1 to 2

  L{f(t)} = [(1/s) - (1/s^2)] * e^(-s) - (1/s^2) + [(2/s) - (1/s^2)] * e^(-2s) - [(-1/s) - (1/s^2)] * e^(-s)

  L{f(t)} = (1/s^2) * (1 - e^(-s)) + (1/s) * (e^(-s) - e^(-2s))

- Now, using the formula for the Laplace transform of a periodic function, we get:

  F(s) = (1 / (1 - e^(-2s))) * L{f(t)}

  F(s) = (1 / (1 - e^(-2s))) * [(1/s^2) * (1 - e^(-s)) + (1/s) * (e^(-s) - e^(-2s))]

  F(s) = (1/s^2) * (1 - e^(-s)) / (1 - e^(-2s)) + (1/s) * (e^(-s) - e^(-2s)) / (1 - e^(-2s))

Some possible mnemonics and learning tricks for the topic are:

- To remember the formula for the Laplace transform of a periodic function, you can use the acronym PLOT:

  P = Periodic function

  L = Laplace transform

  O = One cycle

  T = Time-shifting

  F(s) = (1 / (1 - e^(-sT))) * L{f(t)}

- To remember the formula for the Laplace transform of a piecewise continuous function, you can use the acronym PIE:

  P = Piecewise continuous function

  I = Integral

  E = Exponential

  L{f(t)} = integral from a to b of f(t) * e^(-st) dt

- To remember the time-shifting property of the Laplace transform, you can use the acronym SET:

  S = Shift

  E = Exponential

  T = Time

  L{f(t-T)} = e^(-sT) * L{f(t)}