### Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- The Laplace transform of a periodic function f(t) with period T is given by:

  L{f(t)} = (1/(1-e^(-sT))) * integral from 0 to T of f(t) e^(-st) dt

- The above formula can be derived by using the fact that f(t) can be expressed as an infinite sum of shifted copies of itself, i.e.:

  f(t) = f(t) + f(t+T) + f(t+2T) + ...

- Applying the Laplace transform to both sides of the above equation and using the linearity and time-shifting properties, we get:

  L{f(t)} = L{f(t)} + e^(-sT)L{f(t)} + e^(-2sT)L{f(t)} + ...

- Factoring out L{f(t)} and simplifying, we get:

  L{f(t)} = (1/(1-e^(-sT))) * L{f(t)}

- To find L{f(t)}, we can use the definition of the Laplace transform and integrate over one period of f(t), i.e.:

  L{f(t)} = integral from 0 to T of f(t) e^(-st) dt

- Substituting this into the previous equation, we get the final formula for the Laplace transform of a periodic function.

- Example: Find the Laplace transform of the periodic function f(t) shown below, where T = 2.

  ![periodic function](https://www.intmath.com/laplace-transformation/img/periodic-function-1.gif)

- Solution: Using the formula for the Laplace transform of a periodic function, we have:

  L{f(t)} = (1/(1-e^(-2s))) * integral from 0 to 2 of f(t) e^(-st) dt

- The integral can be split into two parts, corresponding to the two intervals where f(t) has different values, i.e.:

  L{f(t)} = (1/(1-e^(-2s))) * (integral from 0 to 1 of e^(-st) dt + integral from 1 to 2 of 2e^(-st) dt)

- Evaluating the integrals and simplifying, we get:

  L{f(t)} = (1/(1-e^(-2s))) * ((1/s) - (e^(-s)/s) + (2e^(-s)/s) - (2e^(-2s)/s))

- Further simplifying, we get:

  L{f(t)} = (1/(s(1-e^(-2s)))) * (1 - e^(-s) + 2e^(-s) - 2e^(-2s))

- This is the Laplace transform of the periodic function f(t).