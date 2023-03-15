# Fitting of second degree parabola

- A second degree parabola is a curve of the form `y = a + bx + cx^2`, where `a`, `b`, and `c` are constants.
- Fitting a second degree parabola to a given set of data points means finding the values of `a`, `b`, and `c` that minimize the sum of squared errors between the observed `y` values and the predicted `y` values from the parabola.
- One method to fit a second degree parabola is the **least squares method**, which involves solving a system of **normal equations** derived from the data points.
- The normal equations for fitting a second degree parabola are:

  - `∑y = an + b∑x + c∑x^2`
  - `∑xy = a∑x + b∑x^2 + c∑x^3`
  - `∑x^2y = a∑x^2 + b∑x^3 + c∑x^4`

  where `n` is the number of data points, and `∑` denotes the sum of the values.

- To solve the normal equations, one can use various methods, such as matrix inversion, Gaussian elimination, or Cramer's rule.
- Alternatively, one can use a **change of origin** technique, which involves shifting the origin to the middle value of `x` and making the substitution `u = x - h`, `v = y`, where `h` is the new origin. This simplifies the normal equations to:

  - `∑v = an + c∑u^2`
  - `∑uv = b∑u^2 + c∑u^3`
  - `∑u^2v = b∑u^3 + c∑u^4`

  where `n` is the number of data points, and `∑` denotes the sum of the values.

- After finding the values of `a`, `b`, and `c`, one can obtain the equation of the fitted parabola by substituting back `u = x - h`, `v = y`.
- The fitted parabola can be used to estimate the trend of the data, to interpolate or extrapolate the values of `y` for given values of `x`, or to analyze the relationship between the variables `x` and `y`.