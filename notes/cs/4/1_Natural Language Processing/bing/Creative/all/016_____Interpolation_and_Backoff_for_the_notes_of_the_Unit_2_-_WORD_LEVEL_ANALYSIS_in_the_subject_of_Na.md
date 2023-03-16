# Interpolation and Backoff

Interpolation and backoff are two techniques for smoothing n-gram models in natural language processing (NLP). Smoothing is the process of assigning non-zero probabilities to unseen n-grams, and adjusting the probabilities of seen n-grams, to avoid overfitting and improve generalization.

## Interpolation

Interpolation is a method of smoothing that combines multiple n-gram models into a single model. For example, a trigram model can be interpolated with a bigram model and a unigram model, using some weights that sum to one. The weights can be learned from a held-out corpus or tuned using some optimization method. The general formula for interpolation is:

$$p_{interp}(w_i|w_{i-1}w_{i-2}) = \lambda_1 p(w_i|w_{i-1}w_{i-2}) + \lambda_2 p(w_i|w_{i-1}) + \lambda_3 p(w_i)$$

where $\lambda_1 + \lambda_2 + \lambda_3 = 1$ and $p(w_i|w_{i-1}w_{i-2})$, $p(w_i|w_{i-1})$, and $p(w_i)$ are the trigram, bigram, and unigram probabilities, respectively  .

Interpolation can also be applied recursively, such that the lower-order models are themselves interpolated. For example, the bigram model can be interpolated with the unigram model, and the unigram model can be interpolated with a uniform distribution. This is called Jelinek-Mercer smoothing, and the formula is:

$$p_{interp}(w_i|w_{i-1}w_{i-2}) = \lambda_1 p(w_i|w_{i-1}w_{i-2}) + (1 - \lambda_1)p_{interp}(w_i|w_{i-1})$$

$$p_{interp}(w_i|w_{i-1}) = \lambda_2 p(w_i|w_{i-1}) + (1 - \lambda_2)p_{interp}(w_i)$$

$$p_{interp}(w_i) = \lambda_3 p(w_i) + (1 - \lambda_3)p_{u}(w_i)$$

where $p_{u}(w_i)$ is the uniform distribution.

Interpolation has the advantage of using all the available information from different n-gram models, and can produce smooth and consistent probability estimates. However, it also has the disadvantage of requiring more parameters to be estimated, and can be computationally expensive.

## Backoff

Backoff is another method of smoothing that uses a lower-order n-gram model when the higher-order model is zero or unreliable. For example, a trigram model can back off to a bigram model when the trigram is unseen, and a bigram model can back off to a unigram model when the bigram is unseen. The general formula for backoff is:

$$p_{backoff}(w_i|w_{i-1}w_{i-2}) = \begin{cases} p(w_i|w_{i-1}w_{i-2}) & \text{if } c(w_{i-2}w_{i-1}w_i) > 0 \\ \alpha(w_{i-1}w_{i-2})p_{backoff}(w_i|w_{i-1}) & \text{otherwise} \end{cases}$$

where $c(w_{i-2}w_{i-1}w_i)$ is the count of the trigram, and $\alpha(w_{i-1}w_{i-2})$ is a scaling factor that ensures the probabilities sum to one  .

Backoff can also be modified to use a discounting factor that reduces the probability of seen n-grams, and allocates some probability mass to unseen n-grams. This is called Katz smoothing, and the formula is:

$$p_{backoff}(w_i|w_{i-1}w_{i-2}) = \begin{cases} d(c(w_{i-2}w_{i-1}w_i))p(w_i|w_{i-1}w_{i-2}) & \text{if } c(w_{i-2}w_{i-1}w