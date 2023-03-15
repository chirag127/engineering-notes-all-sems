### Fitting of second degree parabola

- A second degree parabola is a curve of the form `y = a + bx + cx^2`, where `a`, `b`, and `c` are constants.
- Fitting a second degree parabola to a given set of data points means finding the values of `a`, `b`, and `c` that minimize the sum of squared errors between the observed `y` values and the predicted `y` values from the parabola.
- One method to fit a second degree parabola is the **least squares method**, which involves solving a system of **normal equations** derived from the error function.
- The normal equations for fitting a second degree parabola are:

  - `∑y = an + b∑x + c∑x^2`
  - `∑xy = a∑x + b∑x^2 + c∑x^3`
  - `∑x^2y = a∑x^2 + b∑x^3 + c∑x^4`

  where `n` is the number of data points, and `∑` denotes the summation over all data points.

- To solve the normal equations, one can use various methods such as matrix inversion, Gaussian elimination, or Cramer's rule.
- Alternatively, one can use a **change of origin** technique to simplify the normal equations by shifting the `x` values to a new origin, such as the mean or the median of the `x` values, and making the substitution `u = x - h`, where `h` is the new origin. Then, the curve of fit becomes `v = a + bu + cu^2`, where `v = y`, and the normal equations become:

  - `∑v = an + b∑u + c∑u^2`
  - `∑uv = a∑u + b∑u^2 + c∑u^3`
  - `∑u^2v = a∑u^2 + b∑u^3 + c∑u^4`

  where `∑` denotes the summation over all data points.

- The advantage of this technique is that the summation of `u` values is zero, which simplifies the normal equations and reduces the computational errors.
- Once the values of `a`, `b`, and `c` are obtained, the original values of `a`, `b`, and `c` for the parabola `y = a + bx + cx^2` can be found by using the relations:

  - `a = a - bh + ch^2`
  - `b = b - 2ch`
  - `c = c`

- The fitted parabola can then be used to estimate the trend values, forecast future values, or analyze the relationship between the variables.