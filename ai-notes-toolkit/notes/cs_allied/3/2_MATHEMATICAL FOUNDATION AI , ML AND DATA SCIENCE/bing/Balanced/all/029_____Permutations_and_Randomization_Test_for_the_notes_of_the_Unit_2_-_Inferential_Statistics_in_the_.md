Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 2 - Inferential Statistics in the subject of Mathematical Foundation AI, ML and Data Science. Here are some notes on the topic of Permutations and Randomization Test:

# Permutations and Randomization Test

- Permutations and randomization tests are non-parametric methods for testing hypotheses about the distribution of a variable or the relationship between two variables.
- Permutations and randomization tests do not rely on any assumptions about the shape or parameters of the population distribution, such as normality or homogeneity of variance.
- Permutations and randomization tests use the observed data to generate a reference distribution of possible outcomes under the null hypothesis, and compare the observed outcome to this distribution to calculate a p-value.
- Permutations and randomization tests are also called resampling methods, because they involve repeatedly resampling the data or rearranging the labels of the data to create new samples.
- Permutations and randomization tests can be applied to different types of data and hypotheses, such as one-sample, two-sample, paired, or correlation tests.

## One-sample permutation test

- A one-sample permutation test is used to test whether the mean or median of a variable is equal to a specified value.
- The null hypothesis is that the mean or median of the variable is equal to the specified value, and the alternative hypothesis is that it is not equal (or greater or less than) the specified value.
- The test statistic is the difference between the observed mean or median and the specified value.
- The permutation procedure is to randomly shuffle the values of the variable and calculate the test statistic for each shuffled sample. This creates a reference distribution of possible test statistics under the null hypothesis.
- The p-value is the proportion of shuffled samples that have a test statistic as extreme or more extreme than the observed test statistic.

## Two-sample permutation test

- A two-sample permutation test is used to test whether the means or medians of two independent groups are equal.
- The null hypothesis is that the means or medians of the two groups are equal, and the alternative hypothesis is that they are not equal (or that one is greater or less than the other).
- The test statistic is the difference between the means or medians of the two groups.
- The permutation procedure is to randomly swap the group labels of the observations and calculate the test statistic for each swapped sample. This creates a reference distribution of possible test statistics under the null hypothesis.
- The p-value is the proportion of swapped samples that have a test statistic as extreme or more extreme than the observed test statistic.

## Paired permutation test

- A paired permutation test is used to test whether the mean or median of the differences between two paired or matched groups is equal to zero.
- The null hypothesis is that the mean or median of the differences is zero, and the alternative hypothesis is that it is not zero (or positive or negative).
- The test statistic is the mean or median of the differences between the paired observations.
- The permutation procedure is to randomly change the sign of the differences and calculate the test statistic for each sign-changed sample. This creates a reference distribution of possible test statistics under the null hypothesis.
- The p-value is the proportion of sign-changed samples that have a test statistic as extreme or more extreme than the observed test statistic.

## Randomization test for correlation

- A randomization test for correlation is used to test whether the correlation coefficient between two variables is equal to zero.
- The null hypothesis is that the correlation coefficient is zero, and the alternative hypothesis is that it is not zero (or positive or negative).
- The test statistic is the observed correlation coefficient.
- The randomization procedure is to randomly shuffle the values of one of the variables and calculate the correlation coefficient for each shuffled sample. This creates a reference distribution of possible correlation coefficients under the null hypothesis.
- The p-value is the proportion of shuffled samples that have a correlation coefficient as extreme or more extreme than the observed correlation coefficient.