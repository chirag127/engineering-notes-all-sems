### Fitting of second degree parabola

A second degree parabola is a curve that can be represented by the equation `y = ax^2 + bx + c`, where `a`, `b`, and `c` are constants. Fitting a second degree parabola to a set of data points involves finding the values of `a`, `b`, and `c` that minimize the sum of the squared differences between the observed `y` values and the `y` values predicted by the parabola.

Here are the steps to fit a second degree parabola to a set of data points:

1. Calculate the sums `Sx`, `Sx^2`, `Sx^3`, `Sx^4`, `Sy`, `Sxy`, and `Sx^2y` for the given data points `(x1, y1), (x2, y2), ..., (xn, yn)`.
2. Set up the normal equations:
```
Sx^2 * a + Sx * b + n * c = Sxy
Sx^3 * a + Sx^2 * b + Sx * c = Sx^2y
Sx^4 * a + Sx^3 * b + Sx^2 * c = Sx^3y
```
3. Solve the normal equations for `a`, `b`, and `c` using any method for solving systems of linear equations.
4. The fitted second degree parabola is given by the equation `y = ax^2 + bx + c`, where `a`, `b`, and `c` are the values obtained in the previous step.

This method can be used to fit a second degree parabola to any set of data points. It is a useful technique in statistical analysis and can be used to model and analyze various types of data.