### Interpolation and Backoff

- Interpolation and backoff are two techniques for smoothing n-gram models in natural language processing (NLP).
- Smoothing is the process of assigning non-zero probabilities to unseen n-grams, and adjusting the probabilities of seen n-grams, to avoid data sparseness and overfitting problems.
- Interpolation is a technique that combines the probabilities of different order n-grams, using some weights that sum to one. For example, a trigram probability can be interpolated as a linear combination of a trigram, a bigram, and a unigram probability  :
  - p<sub>interp</sub>(w<sub>i</sub>|w<sub>i-1</sub>w<sub>i-2</sub>) = λ<sub>1</sub>p<sub>ML</sub>(w<sub>i</sub>|w<sub>i-1</sub>w<sub>i-2</sub>) + λ<sub>2</sub>p<sub>ML</sub>(w<sub>i</sub>|w<sub>i-1</sub>) + λ<sub>3</sub>p<sub>ML</sub>(w<sub>i</sub>)
  - where p<sub>ML</sub> is the maximum likelihood estimate, and λ<sub>1</sub> + λ<sub>2</sub> + λ<sub>3</sub> = 1
- Backoff is a technique that uses a lower order n-gram probability when the higher order n-gram probability is zero or unreliable. For example, a trigram probability can be backed off to a bigram or a unigram probability, depending on the availability of the data  :
  - p<sub>backoff</sub>(w<sub>i</sub>|w<sub>i-1</sub>w<sub>i-2</sub>) = 
    - p<sub>ML</sub>(w<sub>i</sub>|w<sub>i-1</sub>w<sub>i-2</sub>) if count(w<sub>i-2</sub>w<sub>i-1</sub>w<sub>i</sub>) > 0
    - α<sub>1</sub>p<sub>ML</sub>(w<sub>i</sub>|w<sub>i-1</sub>) if count(w<sub>i-2</sub>w<sub>i-1</sub>w<sub>i</sub>) = 0 and count(w<sub>i-1</sub>w<sub>i</sub>) > 0
    - α<sub>2</sub>p<sub>ML</sub>(w<sub>i</sub>) if count(w<sub>i-2</sub>w<sub>i-1</sub>w<sub>i</sub>) = 0 and count(w<sub>i-1</sub>w<sub>i</sub>) = 0
  - where α<sub>1</sub> and α<sub>2</sub> are normalization factors to ensure that the probabilities sum to one
- Both interpolation and backoff can improve the performance of n-gram models, but they have different advantages and disadvantages. Interpolation can smooth the probabilities more smoothly, but it requires more parameters to estimate. Backoff can reduce the number of parameters, but it can introduce sudden changes in the probabilities when switching to a lower order model.