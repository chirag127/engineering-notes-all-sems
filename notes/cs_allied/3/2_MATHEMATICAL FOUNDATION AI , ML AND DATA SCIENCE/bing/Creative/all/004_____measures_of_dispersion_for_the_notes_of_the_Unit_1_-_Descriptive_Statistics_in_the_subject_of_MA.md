Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content on the topic of measures of dispersion for the notes of the Unit 1 - Descriptive Statistics in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE.

# Measures of Dispersion

- Measures of dispersion are numerical values that indicate the variability or spread of a data set.
- They complement the measures of central tendency, such as mean, median and mode, which describe the average or typical value of a data set.
- Measures of dispersion are useful for comparing the distributions of different data sets, or for assessing the reliability or accuracy of statistical summaries.

## Common Measures of Dispersion

- Some of the common measures of dispersion are:

  - **Range:** The difference between the maximum and minimum values in a data set. It is the simplest measure of dispersion, but it is sensitive to outliers and does not use all the data values.

  - **Interquartile Range (IQR):** The difference between the third quartile (Q3) and the first quartile (Q1) in a data set. It is the range of the middle 50% of the data values. It is less sensitive to outliers than the range and gives a better indication of the variability within a data set.

  - **Variance:** The average of the squared deviations of each data value from the mean of the data set. It measures how far the data values are spread around the mean. It is always non-negative, and a larger variance indicates a higher dispersion.

  - **Standard Deviation:** The positive square root of the variance. It measures how far the data values are spread around the mean in the same units as the data. It is the most widely used measure of dispersion, as it is easy to interpret and compare.

  - **Coefficient of Variation (CV):** The ratio of the standard deviation to the mean, expressed as a percentage. It measures the relative variability of a data set, regardless of the units or scale of the data. It is useful for comparing the dispersion of data sets with different means or units.

## How to Calculate Measures of Dispersion

- The formulas for calculating the measures of dispersion are:

  - **Range = Max - Min**

  - **IQR = Q3 - Q1**

  - **Variance = (Sum of (x - mean)^2) / n**

  - **Standard Deviation = Square root of Variance**

  - **CV = (Standard Deviation / Mean) x 100%**

- Here, x is a data value, mean is the arithmetic mean of the data set, n is the number of data values, and Q1 and Q3 are the first and third quartiles, respectively.

- To calculate the quartiles, we can use the following steps:

  - Arrange the data values in ascending order.
  - Find the median of the data set, which divides the data into two halves.
  - Find the median of the lower half of the data, which is Q1.
  - Find the median of the upper half of the data, which is Q3.

## Examples of Measures of Dispersion

- Suppose we have two data sets, A and B, as follows:

  - A = {2, 4, 6, 8, 10}
  - B = {1, 3, 5, 7, 9}

- We can calculate the measures of dispersion for each data set as follows:

  - **Range:**

    - Range of A = 10 - 2 = 8
    - Range of B = 9 - 1 = 8

  - **IQR:**

    - Q1 of A = Median of {2, 4} = 3
    - Q3 of A = Median of {8, 10} = 9
    - IQR of A = 9 - 3 = 6
    - Q1 of B = Median of {1, 3} = 2
    - Q3 of B = Median of {7, 9} = 8
    - IQR of B = 8 - 2 = 6

  - **Variance:**

    - Mean of A = (2 + 4 + 6 + 8 + 10) / 5 = 6
    - Variance of A = ((2 - 6)^2 + (4 - 6)^2 + (6 - 6)^2 + (8 - 6)^2 + (10 - 6)^2) / 5 = 8
    - Mean of B = (1 + 3