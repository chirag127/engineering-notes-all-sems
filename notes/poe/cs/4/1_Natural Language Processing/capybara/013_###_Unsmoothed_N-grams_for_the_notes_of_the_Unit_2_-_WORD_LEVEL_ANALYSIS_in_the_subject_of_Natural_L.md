### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

In natural language processing, N-grams are a sequence of N words that appear together in a text. Unsmoothed N-grams are a type of N-gram model that does not use any smoothing techniques to handle unseen or rare words.

Here are some important points to remember about Unsmoothed N-grams:

- Unsmoothed N-grams are a simple and straightforward way to model the probability of a sentence or text by counting the frequency of each N-gram in the corpus.
- The main advantage of Unsmoothed N-grams is their simplicity, which makes them easy to implement and understand.
- However, Unsmoothed N-grams suffer from the problem of sparsity, which means that some N-grams may have zero counts in the corpus, leading to zero probability estimates. This can cause issues when trying to predict the probability of unseen or rare words or phrases.
- One way to mitigate the problem of sparsity is to use smoothing techniques, such as Laplace smoothing or Good-Turing smoothing, which add a small amount of probability mass to unseen N-grams. However, this can also introduce some bias into the probability estimates.
- Mnemonic: When using Unsmoothed N-grams, it's like counting the number of times each phrase appears in a book, without any adjustments for how common or rare the words are. This can lead to some phrases being overestimated or underestimated in their probability, and can be improved by using smoothing techniques.

Overall, Unsmoothed N-grams are a simple but limited way to model the probability of text in natural language processing. While they can be useful in some cases, it's important to be aware of their limitations and consider using more advanced techniques when dealing with sparse or complex data.