# Measures of Skewness and Kurtosis

- Skewness and kurtosis are two measures of shape that describe the distribution of data values.
- Skewness measures the degree of symmetry or asymmetry of a distribution, while kurtosis measures the degree of heaviness or lightness of the tails of a distribution relative to a normal distribution.
- Skewness and kurtosis are important for descriptive statistics, as they can reveal information about the central tendency, variability, and outliers of a data set.
- Skewness and kurtosis can also be used for inferential statistics, as they can test the normality assumption of many statistical methods.

## Skewness

- Skewness is a measure of the lack of symmetry of a distribution. A distribution is symmetric if it looks the same to the left and right of the center point.
- Skewness can be positive, negative, or zero. Positive skewness means that the distribution has a longer right tail, and the mean is greater than the median. Negative skewness means that the distribution has a longer left tail, and the mean is less than the median. Zero skewness means that the distribution is symmetric, and the mean is equal to the median.
- Skewness can be calculated by various formulas, but one of the simplest is Pearson's median skewness, which is defined as:

$$
\text{Pearson's median skewness} = \frac{3(\text{mean} - \text{median})}{\text{standard deviation}}
$$

- Pearson's median skewness tells us how many standard deviations separate the mean and the median. The larger the absolute value of the skewness, the more skewed the distribution is.
- Skewness can also be estimated by looking at the shape of a histogram or a box plot. A histogram can show the symmetry or asymmetry of the data values, while a box plot can show the relative positions of the mean and the median.

## Kurtosis

- Kurtosis is a measure of the heaviness or lightness of the tails of a distribution relative to a normal distribution. A normal distribution has a kurtosis of 3, which is also called mesokurtic.
- Kurtosis can be greater than 3, less than 3, or equal to 3. Greater than 3 means that the distribution has heavier tails and a sharper peak than a normal distribution, and it is called leptokurtic. Less than 3 means that the distribution has lighter tails and a flatter peak than a normal distribution, and it is called platykurtic. Equal to 3 means that the distribution has the same tails and peak as a normal distribution, and it is called mesokurtic.
- Kurtosis can be calculated by various formulas, but one of the simplest is the excess kurtosis, which is defined as:

$$
\text{Excess kurtosis} = \frac{\text{sum of fourth powers of deviations from the mean}}{(\text{number of observations})(\text{fourth power of standard deviation})} - 3
$$

- Excess kurtosis tells us how much the kurtosis of the distribution differs from 3. The larger the absolute value of the excess kurtosis, the more different the distribution is from a normal distribution.
- Kurtosis can also be estimated by looking at the shape of a histogram or a box plot. A histogram can show the height and width of the peak and the tails of the distribution, while a box plot can show the relative lengths of the whiskers and the interquartile range.