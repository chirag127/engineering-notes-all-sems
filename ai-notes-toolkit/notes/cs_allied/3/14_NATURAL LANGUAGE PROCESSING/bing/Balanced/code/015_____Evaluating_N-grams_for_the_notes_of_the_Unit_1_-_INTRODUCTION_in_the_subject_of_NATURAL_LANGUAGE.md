### Evaluating N-grams

- N-grams are sequences of words or characters that are used to model language and capture the probability of a word given its previous context.
- N-grams are evaluated based on how well they can predict unseen data, such as test sentences or documents, using the probabilities estimated from the training data.
- There are different methods to evaluate n-grams, such as:

  - **Perplexity**: a measure of how uncertain the model is about the next word, given the previous context. Perplexity is inversely proportional to the probability of the test data, and lower perplexity means better prediction. Perplexity can be calculated as:

    $$\text{Perplexity}(W) = P(w_1 w_2 \dots w_N)^{-\frac{1}{N}} = \sqrt[N]{\frac{1}{P(w_1 w_2 \dots w_N)}}$$

    where $W$ is the test data, $N$ is the number of words in the test data, and $P(w_1 w_2 \dots w_N)$ is the probability of the test data according to the n-gram model.

  - **Entropy**: a measure of how much information is needed to encode the test data, given the n-gram model. Entropy is proportional to the negative logarithm of the probability of the test data, and lower entropy means better compression. Entropy can be calculated as:

    $$\text{Entropy}(W) = -\frac{1}{N} \log_2 P(w_1 w_2 \dots w_N)$$

    where $W$ is the test data, $N$ is the number of words in the test data, and $P(w_1 w_2 \dots w_N)$ is the probability of the test data according to the n-gram model.

  - **Cross-entropy**: a measure of how much information is needed to encode the test data, given the n-gram model and a reference model. Cross-entropy is proportional to the negative logarithm of the probability of the test data, weighted by the reference model. Cross-entropy can be calculated as:

    $$\text{Cross-entropy}(W) = -\frac{1}{N} \sum_{i=1}^N q(w_i) \log_2 p(w_i)$$

    where $W$ is the test data, $N$ is the number of words in the test data, $q(w_i)$ is the probability of the $i$-th word according to the reference model, and $p(w_i)$ is the probability of the $i$-th word according to the n-gram model.

  - **Kullback-Leibler divergence**: a measure of how much the n-gram model differs from the reference model. Kullback-Leibler divergence is proportional to the difference between the cross-entropy and the entropy of the test data, and lower divergence means better similarity. Kullback-Leibler divergence can be calculated as:

    $$\text{Kullback-Leibler divergence}(W) = \text{Cross-entropy}(W) - \text{Entropy}(W)$$

    where $W$ is the test data, and $\text{Cross-entropy}(W)$ and $\text{Entropy}(W)$ are defined as above.

- N-gram evaluation methods have some limitations, such as:

  - They do not account for the semantic or syntactic quality of the generated text, only the statistical likelihood.
  - They are sensitive to the choice of the test data and the reference model, which may not reflect the true distribution of the language or the task.
  - They are affected by the smoothing techniques used to deal with zero or low probabilities of unseen n-grams. Different smoothing methods may result in different n-gram probabilities and evaluations.