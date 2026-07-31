### Fitting of straight lines

- Fitting of a straight line is the process of finding the best linear relationship between two variables, such as X and Y, based on a set of data points.
- The equation of a straight line is usually written as Y = a + bX, where a and b are constants or unknowns that need to be determined from the data.
- One of the most common methods for fitting a straight line is the method of least squares, which minimizes the sum of the squares of the vertical distances between the data points and the line.
- The method of least squares leads to the following normal equations that can be solved for a and b:

  - n a + b ∑ X i = ∑ Y i
  - a ∑ X i + b ∑ X i 2 = ∑ X i Y i

  where n is the number of data points and ∑ denotes the summation.

- Another method for fitting a straight line is the method of orthogonal regression, which minimizes the sum of the squares of the perpendicular distances between the data points and the line.
- The method of orthogonal regression leads to the following equation that can be solved for b:

  - b 2 ∑ X i 2 − 2 b ∑ X i Y i + ∑ Y i 2 = n ∑ X i 2 ∑ Y i 2 − ( ∑ X i Y i ) 2

  where n is the number of data points and ∑ denotes the summation. The value of a can be obtained from the relation:

  - a = ∑ Y i − b ∑ X i n

- There are other methods for fitting a straight line, such as robust simple linear regression and Deming regression, that are more resistant to outliers or measurement errors in the data. These methods use different criteria or weights to measure the distance between the data points and the line.