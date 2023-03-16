Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the measures of skewness and kurtosis for the Unit 1 - Descriptive Statistics in the subject of Mathematical Foundation AI, ML and Data Science.

### Measures of Skewness and Kurtosis

- Skewness is a measure of symmetry, or more precisely, the lack of symmetry. A distribution, or data set, is symmetric if it looks the same to the left and right of the center point .
- Kurtosis is a measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution. That is, it measures how peaked or flat the data are .
- Skewness and kurtosis are important for describing the shape of the data and detecting outliers or deviations from the normality assumption.
- There are different ways to calculate skewness and kurtosis, but one of the most common is the **moment-based** method, which uses the following formulas:

    - Skewness = (mean - median) / standard deviation
    - Kurtosis = (mean - mode) / standard deviation

- Alternatively, one can use the **Pearson's median skewness** formula, which is simpler and more robust to outliers:

    - Skewness = 3 * (mean - median) / standard deviation

- The sign and magnitude of skewness and kurtosis indicate the direction and degree of deviation from the normal distribution. For example:

    - A skewness of zero means the data are perfectly symmetric.
    - A positive skewness means the data are skewed to the right, with a longer right tail and a higher mean than median.
    - A negative skewness means the data are skewed to the left, with a longer left tail and a lower mean than median.
    - A kurtosis of zero means the data have the same kurtosis as the normal distribution, which is also called **mesokurtic**.
    - A positive kurtosis means the data have a higher kurtosis than the normal distribution, which is also called **leptokurtic**. This implies a more peaked and heavy-tailed distribution.
    - A negative kurtosis means the data have a lower kurtosis than the normal distribution, which is also called **platykurtic**. This implies a more flat and light-tailed distribution.

- Here are some examples of different distributions with different skewness and kurtosis values:

![skewness and kurtosis examples](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35b_files/image001.gif)

- Skewness and kurtosis can be calculated using various software tools, such as Excel, R, Python, etc. They can also be visualized using histograms, boxplots, or density plots.
- Skewness and kurtosis are useful for exploring the data, testing hypotheses, and building models. For example, some statistical tests and methods assume that the data are normally distributed, so checking the skewness and kurtosis can help to assess the validity of this assumption. Alternatively, some methods can handle non-normal data, such as robust or nonparametric methods, so knowing the skewness and kurtosis can help to choose the appropriate method.