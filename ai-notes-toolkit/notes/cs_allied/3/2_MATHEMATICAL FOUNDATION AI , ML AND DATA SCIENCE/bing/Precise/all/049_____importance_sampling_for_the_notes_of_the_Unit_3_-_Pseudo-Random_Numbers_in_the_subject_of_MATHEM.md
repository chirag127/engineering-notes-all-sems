# Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI, ML AND DATA SCIENCE

### Importance Sampling

- Importance sampling is a technique used to estimate properties of a particular distribution while only having samples generated from a different distribution than the distribution of interest.
- It is a variance reduction technique that can be used in Monte Carlo methods.
- The idea behind importance sampling is to choose a sampling distribution that is more likely to generate samples in the regions of the distribution of interest that have the most impact on the property being estimated.
- This can result in a lower variance estimate than if samples were generated from the distribution of interest directly.
- Importance sampling can be particularly useful when the distribution of interest has a heavy tail, as it can be difficult to generate samples from the tail of the distribution directly.
- To implement importance sampling, one must choose a proposal distribution from which to generate samples, and then weight the samples according to the ratio of the probability density functions of the distribution of interest and the proposal distribution.
- The choice of proposal distribution is critical to the success of importance sampling, as a poor choice can result in a higher variance estimate than if samples were generated from the distribution of interest directly.
- Importance sampling has applications in many areas, including computational finance, computer graphics, and machine learning.