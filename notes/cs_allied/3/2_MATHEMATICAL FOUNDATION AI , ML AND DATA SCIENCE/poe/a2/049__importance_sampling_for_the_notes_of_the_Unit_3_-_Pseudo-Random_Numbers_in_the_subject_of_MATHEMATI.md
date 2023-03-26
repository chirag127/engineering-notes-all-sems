 Here is the content in markdown format without any emojis or external links:

### Importance Sampling

- Importance sampling is a technique to generate samples from a distribution of interest, instead of directly sampling from it.
- It works by sampling from another distribution (called the proposal distribution) and weighting the samples to get samples from the distribution of interest.
- The key is to choose a proposal distribution that is easier to sample from but still mimics the original distribution.
- The weights are proportional to the likelihood of the sample under the original distribution, divided by the likelihood under the proposal distribution.
- This technique is useful when direct sampling is difficult, e.g. due to an intractable normalization constant.
- The performance of importance sampling depends on how well the proposal distribution matches the original distribution. A poor choice can lead to high variance.
- Some applications of importance sampling are:
    - Estimating probabilities or expectations w.r.t a complex distribution.
    - Bayesian inference where the posterior is intractable to sample from directly.
    - Sequential Monte Carlo methods.

The content is written in a formal tone with points and no emojis or external links as requested. Let me know if you would like me to modify or add anything.