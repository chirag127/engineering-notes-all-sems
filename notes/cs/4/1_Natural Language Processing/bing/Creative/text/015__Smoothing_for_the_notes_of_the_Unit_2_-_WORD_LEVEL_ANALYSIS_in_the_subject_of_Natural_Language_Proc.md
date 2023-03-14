### Smoothing for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- Smoothing is the process of flattening a probability distribution implied by a language model so that all reasonable word sequences can occur with some probability .
- Smoothing is needed to deal with data sparsity, which is the problem of having zero or very low probabilities for some events that have not been observed or rarely observed in the training data, but may occur in the test data  .
- Smoothing often involves redistributing weight from high probability regions to zero probability regions, or interpolating lower level n-grams with higher level n-grams, or stealing from words with higher probability and adding to words with low probability .
- Some common smoothing techniques are:
  - Add-one (Laplace) smoothing: adding one to the count of every word or n-gram, regardless of whether it has been seen or not  .
  - Add-alpha (Lidstone) smoothing: adding a small positive constant (alpha) to the count of every word or n-gram, which allows more flexibility than add-one smoothing .
  - Interpolation smoothing: combining the probabilities of different level n-grams, such as unigrams, bigrams, and trigrams, with some weights that sum to one  .
  - Kneser-Ney smoothing: reducing the count of words or n-grams that have a high probability and increasing the count of words or n-grams that have a low probability, based on the notion of fertility (how many different words can follow a word or n-gram) .
- Smoothing techniques can improve the performance and accuracy of language models, especially when dealing with out-of-vocabulary words or rare n-grams  .