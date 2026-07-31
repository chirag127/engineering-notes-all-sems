# Measures of Skewness and Kurtosis

- Skewness and kurtosis are two measures of shape that describe the distribution of data values.
- Skewness measures the degree of symmetry or asymmetry of a distribution, while kurtosis measures the degree of heaviness or lightness of the tails of a distribution.
- Skewness and kurtosis are important for understanding the characteristics of a data set, such as its central tendency, variability, and outliers.

## Skewness

- Skewness is a measure of the lack of symmetry of a distribution. A distribution is symmetric if it looks the same to the left and right of the center point.
- A distribution is positively skewed if it has a long right tail, meaning that most of the data values are concentrated on the left side of the distribution and some extreme values are on the right side. A positively skewed distribution has a mean that is greater than the median.
- A distribution is negatively skewed if it has a long left tail, meaning that most of the data values are concentrated on the right side of the distribution and some extreme values are on the left side. A negatively skewed distribution has a mean that is less than the median.
- A distribution is symmetric if it has no skewness, meaning that the mean and the median are equal and the distribution is balanced on both sides of the center point.
- Skewness can be calculated using different formulas, such as Pearson's median skewness, which is defined as:

$$
\text{Pearson's median skewness} = \frac{3(\text{mean} - \text{median})}{\text{standard deviation}}
$$

- Pearson's median skewness tells you how many standard deviations separate the mean and median of a distribution. A positive value indicates a positive skew, a negative value indicates a negative skew, and a zero value indicates a symmetric distribution.
- Skewness can also be calculated using the third moment of a distribution, which is defined as:

$$
\text{Skewness} = \frac{\sum_{i=1}^n (x_i - \bar{x})^3}{n\sigma^3}
$$

- The third moment of a distribution measures how much the distribution deviates from a normal distribution, which has a skewness of zero. A positive value indicates a positive skew, a negative value indicates a negative skew, and a zero value indicates a normal distribution.

## Kurtosis

- Kurtosis is a measure of the heaviness or lightness of the tails of a distribution. A distribution has heavy tails if it has more extreme values than a normal distribution, and it has light tails if it has fewer extreme values than a normal distribution.
- A distribution has high kurtosis if it has heavy tails and a sharp peak, meaning that most of the data values are close to the mean and some extreme values are far from the mean. A high kurtosis distribution is also called leptokurtic.
- A distribution has low kurtosis if it has light tails and a flat peak, meaning that the data values are spread out more evenly and there are fewer extreme values. A low kurtosis distribution is also called platykurtic.
- A distribution has normal kurtosis if it has the same kurtosis as a normal distribution, which is 3. A normal kurtosis distribution is also called mesokurtic.
- Kurtosis can be calculated using the fourth moment of a distribution, which is defined as:

$$
\text{Kurtosis} = \frac{\sum_{i=1}^n (x_i - \bar{x})^4}{n\sigma^4}
$$

- The fourth moment of a distribution measures how much the distribution deviates from a normal distribution, which has a kurtosis of 3. A value greater than 3 indicates a high kurtosis, a value less than 3 indicates a low kurtosis, and a value equal to 3 indicates a normal kurtosis.
- Kurtosis can also be calculated using the excess kurtosis, which is defined as:

$$
\text{Excess kurtosis} = \text{Kurtosis} - 3
$$

- The excess kurtosis measures how much the kurtosis of a distribution differs from the kurtosis of a normal distribution, which is zero. A positive value indicates a high kurtosis, a negative value indicates a low kurtosis, and a zero value indicates a normal kurtosis.