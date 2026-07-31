# Unit 5 - Complex Variable –Integration

## Taylor’s and Laurent’s series

### Taylor’s Series

- Taylor's series is a representation of a function as an infinite sum of terms calculated from the values of its derivatives at a single point.
- For a function `f(z)` that is analytic at `z = z0`, the Taylor series expansion of `f(z)` around `z0` is given by:

```
f(z) = f(z0) + f'(z0)(z-z0) + f''(z0)(z-z0)^2/2! + ... + f^(n)(z0)(z-z0)^n/n! + ...
```

- The series converges to the value of the function for all `z` in a disk centered at `z0` with radius equal to the distance from `z0` to the nearest singularity of `f(z)`.

### Laurent’s Series

- Laurent's series is a representation of a function as an infinite sum of terms, similar to Taylor's series, but it includes terms with negative powers of `(z-z0)`.
- For a function `f(z)` that has an isolated singularity at `z = z0`, the Laurent series expansion of `f(z)` in an annulus around `z0` is given by:

```
f(z) = a_0 + a_1(z-z0) + a_2(z-z0)^2 + ... + a_n(z-z0)^n + ... + b_1/(z-z0) + b_2/(z-z0)^2 + ... + b_n/(z-z0)^n + ...
```

- The coefficients `a_n` and `b_n` are given by the Cauchy integral formula:

```
a_n = 1/(2πi) * ∫[f(z)/(z-z0)^(n+1)]dz
b_n = 1/(2πi) * ∫[f(z)(z-z0)^(n-1)]dz
```

- The series converges to the value of the function for all `z` in the annulus between the inner and outer radii, which are determined by the locations of the nearest singularities of `f(z)`.