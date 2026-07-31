### Permutations and Randomization Test

- Permutations and randomization tests are two types of nonparametric statistical tests that can be used to compare two or more samples without making any assumptions about the underlying population distribution.
- Permutations and randomization tests are based on the idea of shuffling or rearranging the data in some way to create different possible scenarios under the null hypothesis of no difference between the samples.
- Permutations and randomization tests differ in how they generate the scenarios and how they calculate the p-value for the test statistic.

#### Permutation Test

- A permutation test involves two or more samples. The null hypothesis is that all samples come from the same distribution.
- A permutation test is conducted by following these three steps:
  - Compute some test statistic using the set of original observations.
  - Re-arrange the observations in all possible orders, computing the test statistic each time. This creates the permutation distribution of the test statistic under the null hypothesis.
  - Calculate the permutation test p-value, which is the proportion of permutations that have a test statistic as or more extreme than the observed one.
- A permutation test is an exact test, meaning that it gives the exact p-value for any sample size and any test statistic. However, it can be computationally intensive, especially when the number of possible permutations is large.
- A permutation test assumes that the data is sampled randomly from an underlying population distribution (the population model). This means that the conclusions drawn from the permutation test are generally applicable to other data from the population.

#### Randomization Test

- A randomization test is also called a re-randomization test or a random assignment test. It is based on the idea of randomly assigning the observations to different groups or treatments, as in an experiment.
- The null hypothesis of a randomization test is that there is no treatment effect, meaning that the random assignment procedure produces a random shuffle of the responses.
- A randomization test is conducted by following these three steps:
  - Compute some test statistic using the set of original observations.
  - Re-assign the observations to different groups or treatments randomly, computing the test statistic each time. This creates the randomization distribution of the test statistic under the null hypothesis.
  - Calculate the randomization test p-value, which is the proportion of randomizations that have a test statistic as or more extreme than the observed one.
- A randomization test is an approximate test, meaning that it gives an approximate p-value that depends on the number of randomizations performed. Usually, a large number of randomizations (such as 10,000 or more) is used to get a reliable p-value. A randomization test can be less computationally intensive than a permutation test, especially when the number of possible permutations is large.
- A randomization test assumes that the data is obtained by random assignment to different groups or treatments (the randomization model). This means that the conclusions drawn from the randomization test are only applicable to the data at hand and not to other data from the population.

#### Summary

- Permutations and randomization tests are both nonparametric tests that can be used to compare two or more samples without making any assumptions about the underlying population distribution.
- Permutations and randomization tests differ in how they generate the scenarios and how they calculate the p-value for the test statistic.
- Permutation tests are exact tests that assume the population model, while randomization tests are approximate tests that assume the randomization model.