### Permutations and Randomization Test

- Permutations and randomization tests are non-parametric methods for testing hypotheses about the difference between two or more groups or treatments.
- Permutations and randomization tests do not rely on any assumptions about the distribution of the data or the test statistic, unlike parametric tests such as t-tests or ANOVA.
- Permutations and randomization tests use the data itself to generate the sampling distribution of the test statistic under the null hypothesis, by rearranging or shuffling the labels of the observations.
- Permutations and randomization tests are also called exact tests, because they do not approximate the p-value by using a normal or t-distribution, but calculate it exactly by counting the number of permutations or randomizations that are as extreme or more extreme than the observed test statistic.

#### Permutation Test

- A permutation test involves two or more samples that are assumed to be randomly sampled from an underlying population distribution.
- The null hypothesis is that all samples come from the same distribution, and the alternative hypothesis is that at least one sample comes from a different distribution.
- A permutation test works by computing a test statistic (such as the difference in means, medians, or proportions) using the original samples, and then permuting or shuffling the labels of the observations in all possible ways, computing the test statistic for each permutation.
- The p-value of the permutation test is the proportion of permutations that have a test statistic as extreme or more extreme than the observed one, in the direction of the alternative hypothesis.
- A permutation test is valid only if the samples are independent and identically distributed (i.i.d.) under the null hypothesis, and if the test statistic is a function of the ranks of the observations, not their values.
- A permutation test can be applied to any situation where a comparison between two or more groups is of interest, such as a two-sample t-test, a paired t-test, or an ANOVA.

#### Randomization Test

- A randomization test is similar to a permutation test, but it is based on the idea of random assignment of treatments or groups, rather than random sampling from a population.
- The null hypothesis is that the treatment or group has no effect on the outcome, and the alternative hypothesis is that the treatment or group has some effect on the outcome.
- A randomization test works by computing a test statistic (such as the difference in means, medians, or proportions) using the original data, and then randomly assigning or shuffling the labels of the observations to different treatments or groups, computing the test statistic for each randomization.
- The p-value of the randomization test is the proportion of randomizations that have a test statistic as extreme or more extreme than the observed one, in the direction of the alternative hypothesis.
- A randomization test is valid only if the random assignment procedure produces a random shuffle of the responses, and if the test statistic is a function of the ranks of the observations, not their values.
- A randomization test can be applied to any situation where a random experiment is conducted, such as a randomized controlled trial, a matched-pairs design, or a block design.