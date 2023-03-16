# Evaluating N-grams

- N-grams are sequences of n words that are used to model the probability of a word given its previous words in a text.
- N-grams can be used for various natural language processing tasks, such as language modeling, text generation, machine translation, speech recognition, spelling correction, etc.
- To evaluate the quality of n-grams, we need to measure how well they capture the statistical properties of natural language and how well they generalize to unseen data.
- There are different methods to evaluate n-grams, such as:

  - **Perplexity**: Perplexity is a measure of how uncertain a model is about the next word in a sequence. It is defined as the inverse of the average probability assigned by the model to each word in a test set. A lower perplexity means a higher probability and a better model.
  - **Entropy**: Entropy is a measure of how much information is contained in a text. It is defined as the average number of bits needed to encode each word in a text using the model. A higher entropy means a more diverse and complex text and a better model.
  - **Likelihood**: Likelihood is a measure of how well a model fits the observed data. It is defined as the product of the probabilities assigned by the model to each word in a test set. A higher likelihood means a more accurate model.
  - **Cross-entropy**: Cross-entropy is a measure of how much the model differs from the true distribution of the data. It is defined as the average number of bits needed to encode each word in a test set using the true distribution instead of the model. A lower cross-entropy means a more similar model and a better model.
  - **BLEU**: BLEU (Bilingual Evaluation Understudy) is a measure of how well a model translates a text from one language to another. It is defined as the geometric mean of the n-gram precision scores multiplied by a brevity penalty. A higher BLEU score means a more fluent and adequate translation and a better model.