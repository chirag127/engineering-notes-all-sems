# Fitting of Straight Lines

- Fitting of a straight line is the process of finding a line that best represents the relationship between two variables, X and Y, based on a set of data points.
- The equation of a straight line is Y = a + bX, where a and b are constants or unknowns that need to be determined from the data.
- One of the most common methods for fitting a straight line is the method of least squares, which minimizes the sum of the squares of the vertical distances from the data points to the line.
- The method of least squares leads to the following normal equations that can be solved for a and b:

  - n a + b ∑ X i = ∑ Y i
  - a ∑ X i + b ∑ X i 2 = ∑ X i Y i

  where n is the number of data points and ∑ denotes the summation over all data points.

- Another method for fitting a straight line is the orthogonal regression, which minimizes the sum of the squares of the perpendicular distances from the data points to the line.
- The orthogonal regression leads to the following equation that can be solved for b:

  - b 2 + b ( ∑ X i 2 − ∑ Y i 2 ) / n ∑ X i Y i − ∑ X i ∑ Y i = 0

  and then a can be obtained from:

  - a = ( ∑ Y i − b ∑ X i ) / n

- There are other methods for fitting a straight line, such as robust regression, Deming regression, and total least squares, that have different assumptions and properties.