### Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams can be used for various natural language processing tasks, such as text generation, language modeling, machine translation, speech recognition, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical properties of natural language and how well they generalize to unseen data.
- One common way to evaluate n-grams is to use perplexity, which is a measure of how uncertain the model is about the next word in a sequence.
- Perplexity is defined as the inverse of the average probability of the words in a test set, given by the model. The lower the perplexity, the better the model.
- Perplexity can be calculated as follows:

  - Let M be an n-gram model, W be a test set of words, and N be the number of words in W.
  - The perplexity of M on W is given by:

    `PP(M, W) = (P(w1, w2, ..., wN))^(-1/N)`

  - where P(w1, w2, ..., wN) is the probability of the sequence of words in W, given by the model M.
  - If we use the chain rule of probability, we can rewrite P(w1, w2, ..., wN) as:

    `P(w1, w2, ..., wN) = P(w1) * P(w2 | w1) * ... * P(wN | w1, ..., wN-1)`

  - If we use the Markov assumption, which states that the probability of a word only depends on the previous n-1 words, we can simplify P(wN | w1, ..., wN-1) as P(wN | wN-n+1, ..., wN-1).
  - Therefore, the perplexity of M on W can be approximated as:

    `PP(M, W) = (P(w1) * P(w2 | w1) * ... * P(wN | wN-n+1, ..., wN-1))^(-1/N)`

- Another way to evaluate n-grams is to use cross-entropy, which is a measure of how much information is needed to encode the test set using the model.
- Cross-entropy is defined as the negative logarithm of the average probability of the words in a test set, given by the model. The lower the cross-entropy, the better the model.
- Cross-entropy can be calculated as follows:

  - Let M be an n-gram model, W be a test set of words, and N be the number of words in W.
  - The cross-entropy of M on W is given by:

    `H(M, W) = - (1/N) * log(P(w1, w2, ..., wN))`

  - where P(w1, w2, ..., wN) is the probability of the sequence of words in W, given by the model M.
  - If we use the same simplifications as before, we can approximate the cross-entropy of M on W as:

    `H(M, W) = - (1/N) * (log(P(w1)) + log(P(w2 | w1)) + ... + log(P(wN | wN-n+1, ..., wN-1)))`

- Perplexity and cross-entropy are related by the following formula:

  `PP(M, W) = 2^(H(M, W))`

- Therefore, minimizing the cross-entropy is equivalent to minimizing the perplexity of the model.