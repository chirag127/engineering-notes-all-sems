### Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function is a function that is zero for negative values of the argument and one for positive values. It is denoted by u(t) and defined as:

```
u(t) = { 1, t >= 0
         0, t < 0
```

- The unit step function can be used to model a switch that turns on or off at a certain time, or a signal that starts or stops abruptly.

- The Laplace transform of the unit step function is given by :

```
L[u(t)] = int_0^infty u(t) e^(-st) dt = [e^(-st)/(-s)]_0^infty = 1/s, s > 0
```

- The Laplace transform of a function multiplied by a unit step function is given by the time displacement theorem :

```
L[u(t-a) f(t-a)] = e^(-as) L[f(t)], s > 0
```

- This theorem allows us to find the Laplace transform of a piecewise continuous function by breaking it into segments and multiplying each segment by a unit step function that indicates when it starts.

- For example, if f(t) is defined as:

```
f(t) = { 0, 0 <= t < 1
         t, 1 <= t < 2
         2, t >= 2
```

- Then we can write f(t) as:

```
f(t) = u(t-1) t + u(t-2) (2-t)
```

- And the Laplace transform of f(t) is:

```
L[f(t)] = L[u(t-1) t] + L[u(t-2) (2-t)]
        = e^(-s) L[t] + e^(-2s) L[2-t]
        = e^(-s) 1/s^2 + e^(-2s) (2/s - 1/s^2)
        = (e^(-s) - 2e^(-2s))/s^2 + 2e^(-2s)/s
```