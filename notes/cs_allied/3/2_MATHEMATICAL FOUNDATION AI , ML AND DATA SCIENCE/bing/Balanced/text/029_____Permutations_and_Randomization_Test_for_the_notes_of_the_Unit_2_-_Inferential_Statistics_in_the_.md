### Permutations and Randomization Test

- Permutations and randomization tests are two types of nonparametric statistical tests that can be used to compare two or more samples without making any assumptions about the underlying population distribution.
- Permutations and randomization tests are based on the idea of shuffling or rearranging the data in some way to create different possible scenarios under the null hypothesis of no difference between the samples.
- Permutations and randomization tests differ in how they generate the scenarios and how they calculate the p-value for the test statistic.

#### Permutation Test

- A permutation test involves two or more samples. The null hypothesis is that all samples come from the same distribution.
- A permutation test is conducted by following these three steps:
  - Compute some test statistic using the set of original observations.
  - Re-arrange the observations in all possible orders, computing the test statistic each time. This creates the permutation distribution of the test statistic under the null hypothesis.
  - Calculate the permutation test p-value, which is the proportion of permutations that have a test statistic as extreme or more extreme than the observed one.
- A permutation test is an exact test, meaning that it gives the exact p-value without any approximation or error. However, a permutation test can be computationally intensive, especially when the sample size is large or the number of samples is more than two, as the number of possible permutations grows exponentially.
- A permutation test assumes that the data is sampled randomly from an underlying population distribution (the population model). This means that the conclusions drawn from the permutation test are generally applicable to other data from the population.

#### Randomization Test

- A randomization test is also called a re-randomization test or a random assignment test. It is based on the idea of randomly assigning the observations to different groups or treatments, as in a randomized experiment.
- A randomization test involves two or more groups or treatments. The null hypothesis is that there is no difference between the groups or treatments in terms of the outcome variable.
- A randomization test is conducted by following these three steps:
  - Compute some test statistic using the set of original observations.
  - Re-assign the observations to different groups or treatments in a random manner, computing the test statistic each time. This creates the randomization distribution of the test statistic under the null hypothesis.
  - Calculate the randomization test p-value, which is the proportion of randomizations that have a test statistic as extreme or more extreme than the observed one.
- A randomization test is an approximate test, meaning that it gives an approximate p-value that may have some error. However, a randomization test can be computationally efficient, as it does not require generating all possible permutations, but only a large enough number of randomizations to get a reliable estimate of the p-value.
- A randomization test does not assume any population model, but only relies on the random assignment procedure. This means that the conclusions drawn from the randomization test are only applicable to the specific data and the specific randomization method used.