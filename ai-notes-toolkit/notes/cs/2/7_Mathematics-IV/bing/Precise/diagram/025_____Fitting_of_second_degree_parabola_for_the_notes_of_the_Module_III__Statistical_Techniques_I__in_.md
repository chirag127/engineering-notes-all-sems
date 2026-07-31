### Fitting of second degree parabola

A second degree parabola is a curve that can be represented by the equation `y = ax^2 + bx + c`, where `a`, `b`, and `c` are constants. Fitting a second degree parabola to a set of data points involves finding the values of `a`, `b`, and `c` that minimize the sum of the squared errors between the observed `y` values and the `y` values predicted by the parabola.

Here are the steps to fit a second degree parabola to a set of data points:

1. Calculate the sums `Sx`, `Sx^2`, `Sx^3`, `Sx^4`, `Sy`, `Sxy`, and `Sx^2y` for the data points, where `Sx` is the sum of the `x` values, `Sx^2` is the sum of the squares of the `x` values, `Sx^3` is the sum of the cubes of the `x` values, `Sx^4` is the sum of the fourth powers of the `x` values, `Sy` is the sum of the `y` values, `Sxy` is the sum of the products of the `x` and `y` values, and `Sx^2y` is the sum of the products of the squares of the `x` values and the `y` values.

2. Solve the system of equations given by `n * a + Sx * b + Sx^2 * c = Sy`, `Sx * a + Sx^2 * b + Sx^3 * c = Sxy`, and `Sx^2 * a + Sx^3 * b + Sx^4 * c = Sx^2y` for `a`, `b`, and `c`, where `n` is the number of data points.

3. The values of `a`, `b`, and `c` obtained in step 2 are the coefficients of the second degree parabola that best fits the data points.