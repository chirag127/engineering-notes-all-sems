### Fitting of Second Degree Parabola for the Notes of the Module III: Statistical Techniques I: in the Subject of Mathematics-IV KCS

In this module, we will discuss the fitting of a second degree parabola to a given set of data points. The second degree parabola is given by the equation:

```
y = a + bx + cx^2
```

where `a`, `b`, and `c` are constants.

#### Steps for Fitting a Second Degree Parabola

1. Find the mean values of the given data set. Let the mean of `x` values be denoted by `x̄` and the mean of `y` values be denoted by `ȳ`.

2. Calculate the values of `Σx`, `Σy`, `Σx^2`, `Σy^2`, and `Σxy`, where `Σ` denotes the sum of the respective terms over all the data points.

3. Use these values to solve for the constants `a`, `b`, and `c` using the following equations:

   ```
   a = (Σy * Σx^2 - Σx * Σxy) / (n * Σx^2 - (Σx)^2)
   ```
   
   ```
   b = (n * Σxy - Σx * Σy) / (n * Σx^2 - (Σx)^2)
   ```
   
   ```
   c = (n * Σy * Σx^2 - Σx * Σxy - Σy * (Σx)^2 + n * Σx * Σy) / (n * Σx^2 - (Σx)^2)
   ```
   
   where `n` is the number of data points.

4. Substitute the calculated values of `a`, `b`, and `c` into the equation of the second degree parabola to obtain the equation of the curve that best fits the given data set.

#### Interpretation of the Second Degree Parabola

The second degree parabola is a curve that is symmetric about its vertex. The vertex is given by the point:

```
(-b / 2c, a - b^2 / 4c)
```

The coefficient `c` determines the shape of the curve. If `c > 0`, the curve is a U-shaped parabola with a minimum value at the vertex. If `c < 0`, the curve is an inverted U-shaped parabola with a maximum value at the vertex.

The second degree parabola can be used to make predictions about data points that are not in the original data set. However, it is important to note that the accuracy of these predictions depends on the quality of the fit of the parabola to the original data set.

#### Conclusion

Fitting a second degree parabola to a given data set can be a useful tool in statistical analysis. By following the steps outlined above, we can obtain the equation of the curve that best fits the data and use it to make predictions about future data points.