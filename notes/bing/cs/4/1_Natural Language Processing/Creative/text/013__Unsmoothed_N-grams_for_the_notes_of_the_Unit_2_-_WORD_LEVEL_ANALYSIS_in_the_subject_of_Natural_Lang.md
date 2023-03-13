### Unsmoothed N-grams

- An n-gram is a sequence of n words from a text or speech.
- N-grams are used to model the probability of a word given its previous words, based on the frequency of occurrence in a corpus.
- An unsmoothed n-gram model assigns zero probability to any n-gram that does not appear in the corpus, which is unrealistic and problematic for language modeling.
- Unsmoothed n-grams also suffer from data sparsity, meaning that many n-grams that are possible in a language have very low or zero frequency in a corpus, leading to unreliable estimates.
- Unsmoothed n-grams can be improved by using smoothing techniques, such as adding a small constant to the counts, interpolating lower-order n-grams, or using back-off models.