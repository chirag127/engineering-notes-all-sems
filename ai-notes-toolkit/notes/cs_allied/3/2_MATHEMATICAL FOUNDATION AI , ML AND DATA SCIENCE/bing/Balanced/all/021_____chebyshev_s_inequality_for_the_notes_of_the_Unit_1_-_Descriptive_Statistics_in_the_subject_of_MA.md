# Chebyshev's Inequality

- Chebyshev's inequality is a theorem in probability theory that guarantees that, for a wide class of probability distributions, no more than a certain fraction of values can be more than a certain distance from the mean  .
- The inequality is named after the Russian mathematician Pafnuty Chebyshev, who proved it in the 19th century. It is also known as the Bienaymé-Chebyshev inequality, after the French mathematician Irénée-Jules Bienaymé, who independently discovered it.
- The inequality can be stated as follows: Let X be a random variable with finite mean μ and finite non-zero variance σ^2^. Then, for any positive number k, the probability that X deviates from μ by more than k standard deviations is bounded by 1/k^2^, that is,

P(|X - μ| ≥ kσ) ≤ 1/k^2^

- The inequality can be interpreted as a measure of how spread out the values of a random variable are from its mean. The larger the value of k, the smaller the fraction of values that can be farther than k standard deviations from the mean .
- For example, Chebyshev's inequality states that at most 25% of the values can be more than 2 standard deviations from the mean, and at most 11.11% of the values can be more than 3 standard deviations from the mean . These bounds are valid for any probability distribution, not only the normal distribution.
- Chebyshev's inequality is useful for analyzing data sets that do not follow a specific distribution, or for which the distribution is unknown. It can also be used to derive other inequalities, such as Markov's inequality and Chernoff's bound .