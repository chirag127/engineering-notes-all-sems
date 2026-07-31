# Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- If f(t) is a periodic function with period T, then f(t) = f(t+nT) for any integer n. Therefore, we can write f(t) as a sum of shifted copies of f(t) over one period, as follows:

  f(t) = f(t) + e^(-sT)f(t) + e^(-2sT)f(t) + ... + e^(-nsT)f(t) + ...

- Taking the Laplace transform of both sides, we get:

  F(s) = F(s) + e^(-sT)F(s) + e^(-2sT)F(s) + ... + e^(-nsT)F(s) + ...

- This is an infinite geometric series with common ratio e^(-sT). If |e^(-sT)| < 1, then the series converges and we can use the formula for the sum of an infinite geometric series:

  F(s) = F(s) / (1 - e^(-sT))

- This is the formula for the Laplace transform of a periodic function with period T. Note that F(s) is the Laplace transform of f(t) over one period, i.e., F(s) = L{f(t)} from 0 to T.

- Example: Find the Laplace transform of the periodic function f(t) shown below, where T = 2.

  ![periodic function](https://www.intmath.com/laplace-transformation/img/periodic-function.gif)

- Solution: The function f(t) is periodic with period T = 2. To find the Laplace transform of f(t), we need to find the Laplace transform of f(t) over one period, i.e., from 0 to 2. We can split f(t) into two parts: f(t) = f1(t) + f2(t), where f1(t) is the function from 0 to 1 and f2(t) is the function from 1 to 2. Then, we can use the linearity property of the Laplace transform to write:

  F(s) = L{f(t)} from 0 to 2 = L{f1(t)} from 0 to 1 + L{f2(t)} from 1 to 2

- The Laplace transform of f1(t) is:

  L{f1(t)} from 0 to 1 = L{1} from 0 to 1 = 1/s

- The Laplace transform of f2(t) is:

  L{f2(t)} from 1 to 2 = L{-1} from 1 to 2 = -e^(-s)/s

- Therefore, the Laplace transform of f(t) over one period is:

  F(s) = L{f(t)} from 0 to 2 = 1/s - e^(-s)/s = (1 - e^(-s))/s

- Using the formula for the Laplace transform of a periodic function with period T = 2, we get:

  F(s) = (1 - e^(-s))/s / (1 - e^(-2s)) = 1 / (s(1 + e^(-s)))

- This is the final answer.