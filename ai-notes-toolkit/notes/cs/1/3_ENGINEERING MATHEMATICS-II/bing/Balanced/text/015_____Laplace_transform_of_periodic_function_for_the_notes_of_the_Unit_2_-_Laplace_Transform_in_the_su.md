### Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- If f(t) is a periodic function with period T, then f(t) = f(t+nT) for any integer n. Therefore, we can write f(t) as a sum of shifted functions:

  f(t) = f(t) + f(t-T) + f(t-2T) + ...

- Applying the Laplace transform to both sides, we get:

  F(s) = F(s) + e^(-sT)F(s) + e^(-2sT)F(s) + ...

- Factoring out F(s), we get:

  F(s) = F(s) [1 + e^(-sT) + e^(-2sT) + ...]

- The infinite series in the brackets is a geometric series with common ratio e^(-sT), which converges to 1/(1-e^(-sT)) if |e^(-sT)| < 1, or equivalently, if Re(s) > 0. Therefore, we have:

  F(s) = F(s) / (1-e^(-sT))

- This formula gives the Laplace transform of a periodic function in terms of the Laplace transform of one cycle of the function. For example, if f(t) is a periodic function with period 2 and f(t) = t for 0 < t < 1 and f(t) = 2-t for 1 < t < 2, then the Laplace transform of f(t) is:

  F(s) = (1/s^2 - e^(-s)/s^2) / (1-e^(-2s))