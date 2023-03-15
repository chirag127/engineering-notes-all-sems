### Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- If f(t) is a periodic function with period T, then f(t) = f(t+nT) for any integer n. Therefore, we can write f(t) as a sum of shifted functions:

  f(t) = f(t) + f(t-T) + f(t-2T) + ...

- Applying the Laplace transform to both sides, we get:

  F(s) = F(s) + e^(-sT)F(s) + e^(-2sT)F(s) + ...

- Rearranging the terms, we get:

  F(s) - e^(-sT)F(s) - e^(-2sT)F(s) - ... = F(s)

- Factoring out F(s), we get:

  F(s)(1 - e^(-sT) - e^(-2sT) - ...) = F(s)

- Dividing by F(s), we get:

  1 - e^(-sT) - e^(-2sT) - ... = 1

- This is a geometric series with common ratio e^(-sT), which converges to 1/(1-e^(-sT)) if |e^(-sT)| < 1, or equivalently, if Re(s) > 0. Therefore, we can write:

  F(s) = F(s)/(1-e^(-sT))

- This is the formula for the Laplace transform of a periodic function with period T. Note that F(s) is the Laplace transform of one cycle of the function, which can be obtained by integrating f(t) from 0 to T.

- Example: Find the Laplace transform of the periodic function f(t) shown below, where T = 2.

  ![periodic function](https://www.intmath.com/laplace-transformation/img/periodic-unit-ramp.gif)

- Solution: To find the Laplace transform of f(t), we need to find the Laplace transform of one cycle of the function, which is f_1(t) = t for 0 < t < 2. Using the formula for the Laplace transform of a linear function, we get:

  F_1(s) = L{f_1(t)} = L{t} = 1/s^2

- Using the formula for the Laplace transform of a periodic function, we get:

  F(s) = F_1(s)/(1-e^(-2s)) = 1/(s^2(1-e^(-2s)))