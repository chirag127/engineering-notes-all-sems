# Permutations and Randomization Test

## Introduction

- Permutations and randomization tests are **nonparametric** methods for testing hypotheses about the distribution of data.
- They are based on the idea of **shuffling** or **rearranging** the data in some way to create different possible scenarios under the null hypothesis.
- They are useful when the **assumptions** of parametric tests (such as normality, independence, etc.) are not met or when the **sample size** is too small to rely on asymptotic results.
- They are also called **exact** tests because they do not rely on any approximation or distributional assumption, and they can provide the exact p-value for any test statistic.

## Permutation Test

- A permutation test (also called re-randomization test) is an exact statistical hypothesis test making use of the proof by contradiction.
- A permutation test involves two or more samples. The null hypothesis is that all samples come from the same distribution.
- The steps of a permutation test are:

  1. Compute some test statistic using the original data (e.g., difference in means, correlation coefficient, etc.).
  2. Shuffle or permute the data in all possible ways, or take a large random sample of permutations, and compute the test statistic for each permutation.
  3. Compare the original test statistic with the distribution of the permuted test statistics, and calculate the p-value as the proportion of permuted test statistics that are as extreme or more extreme than the original one.
  4. Reject the null hypothesis if the p-value is less than the significance level.

- Permutation tests assume that the data is sampled randomly from an underlying population distribution (the population model). This means that the conclusions drawn from the permutation test are generally applicable to other data from the population.

## Randomization Test

- A randomization test (also called random assignment test) is an exact statistical hypothesis test based on the idea of random assignment of treatments to experimental units.
- A randomization test involves two or more groups of experimental units that receive different treatments. The null hypothesis is that there is no treatment effect, i.e., the response variable is independent of the treatment variable.
- The steps of a randomization test are:

  1. Compute some test statistic using the original data (e.g., difference in means, ANOVA F-statistic, etc.).
  2. Shuffle or randomize the treatment labels among the experimental units, keeping the group sizes fixed, and compute the test statistic for each randomization.
  3. Compare the original test statistic with the distribution of the randomized test statistics, and calculate the p-value as the proportion of randomized test statistics that are as extreme or more extreme than the original one.
  4. Reject the null hypothesis if the p-value is less than the significance level.

- Randomization tests are based on the fact that under the null hypothesis of no treatment effect, the random assignment procedure produces a random shuffle of the responses. This means that the conclusions drawn from the randomization test are specific to the data and the randomization procedure used, and may not generalize to other data or randomization schemes.

## Main Difference

- The main difference between permutation tests and randomization tests is that permutation tests are based on random sampling and randomization tests are based on random assignment.
- Permutation tests can be applied to any situation where the data can be permuted, such as comparing two or more samples, testing for correlation, testing for independence, etc.
- Randomization tests can only be applied to a comparison situation where the treatments are randomly assigned to the experimental units, such as testing for the effect of a drug, a diet, a teaching method, etc.
- Permutation tests are more general and flexible than randomization tests, but they may require more computational power and time to perform, especially when the number of possible permutations is large.