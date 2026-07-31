### Permutations and Randomization Test

- Permutations and randomization tests are two types of nonparametric statistical tests that can be used to compare two or more samples without making any assumptions about the underlying population distribution.
- Permutations and randomization tests are based on the idea of shuffling or rearranging the data in some way to create different possible scenarios under the null hypothesis of no difference between the samples.
- Permutations and randomization tests differ in how they generate the scenarios and how they calculate the p-value for the test statistic.

#### Permutation Test

- A permutation test involves two or more samples. The null hypothesis is that all samples come from the same distribution.
- A permutation test is conducted by following these three steps:
  1. Compute some test statistic using the set of original observations.
  2. Re-arrange the observations in all possible orders, computing the test statistic each time. This creates the permutation distribution of the test statistic.
  3. Calculate the permutation test p-value, which is the proportion of permutations that have a test statistic as extreme or more extreme than the original one.
- A permutation test is an exact test, meaning that it gives the exact p-value for the test without any approximation or error.
- A permutation test assumes that the data is sampled randomly from an underlying population distribution (the population model). This means that the conclusions drawn from the permutation test are generally applicable to other data from the population.
- A permutation test can be applied to any test statistic and any type of data, as long as the permutation distribution is well-defined and the test statistic is appropriate for the research question.
- A permutation test can be computationally intensive, especially when the sample size is large or the number of samples is more than two. In such cases, a random sample of permutations can be used instead of all possible permutations.

#### Randomization Test

- A randomization test is based on random assignment and can be used to test the effect of a treatment or intervention on a response variable.
- A randomization test is conducted by following these three steps:
  1. Compute some test statistic using the set of original observations.
  2. Re-assign the observations to different groups randomly, keeping the group sizes fixed, and compute the test statistic each time. This creates the randomization distribution of the test statistic.
  3. Calculate the randomization test p-value, which is the proportion of randomizations that have a test statistic as extreme or more extreme than the original one.
- A randomization test is also an exact test, meaning that it gives the exact p-value for the test without any approximation or error.
- A randomization test does not assume any population model, but only relies on the random assignment procedure. This means that the conclusions drawn from the randomization test are only valid for the specific data and the specific random assignment used in the experiment.
- A randomization test can also be applied to any test statistic and any type of data, as long as the random assignment procedure is well-defined and the test statistic is appropriate for the research question.
- A randomization test can also be computationally intensive, especially when the number of possible randomizations is large. In such cases, a random sample of randomizations can be used instead of all possible randomizations.