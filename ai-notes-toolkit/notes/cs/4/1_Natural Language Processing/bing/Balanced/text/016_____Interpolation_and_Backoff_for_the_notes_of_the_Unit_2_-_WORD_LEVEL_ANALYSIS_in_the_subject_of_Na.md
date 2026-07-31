### Interpolation and Backoff

- Interpolation and backoff are two methods for smoothing n-gram language models, which are used to estimate the probability of a word given its previous words in a sequence.
- Smoothing is needed to deal with the problem of data sparseness, which occurs when some n-grams are not observed in the training data, resulting in zero probabilities.
- Backoff is a method that uses lower-order n-grams when higher-order n-grams have insufficient evidence. For example, if a trigram probability is zero, then a bigram or a unigram probability is used instead.
- Interpolation is a method that combines n-grams of different orders with some weights, which are usually learned from a held-out corpus. For example, a trigram probability can be interpolated with a bigram and a unigram probability as follows:

  p(w<sub>n</sub>|w<sub>n-2</sub>,w<sub>n-1</sub>) = λ<sub>1</sub>p(w<sub>n</sub>|w<sub>n-2</sub>,w<sub>n-1</sub>) + λ<sub>2</sub>p(w<sub>n</sub>|w<sub>n-1</sub>) + λ<sub>3</sub>p(w<sub>n</sub>)

  where λ<sub>1</sub> + λ<sub>2</sub> + λ<sub>3</sub> = 1

- In general, interpolation works better than backoff, as it can capture more information from different n-gram orders. However, interpolation requires more parameters to be estimated, which can be computationally expensive.
- There are various techniques to improve interpolation and backoff, such as deleted interpolation, absolute discounting, and Kneser-Ney smoothing. These techniques aim to optimize the weights or the probabilities of n-grams based on some criteria, such as minimizing perplexity or maximizing likelihood.