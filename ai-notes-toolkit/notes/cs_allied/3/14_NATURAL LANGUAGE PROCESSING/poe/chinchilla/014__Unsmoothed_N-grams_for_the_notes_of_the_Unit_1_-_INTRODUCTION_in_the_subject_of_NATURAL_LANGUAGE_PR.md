### Unsmoothed N-grams for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

In natural language processing, N-grams are a type of language modeling technique. They are used to predict the probability of the next word in a sequence of words, given the previous words. Unsmoothed N-grams are a simple and straightforward way to model the probability of a sequence of words.

Here are some key points to understand about unsmoothed N-grams:

- An N-gram is a contiguous sequence of N items from a given sample of text, usually words.
- Unsmoothed N-grams are simply the frequencies of N-grams in a given corpus of text, without any additional smoothing or adjustments.
- Unsmoothed N-grams can be used to model the probability of a sequence of words, by simply multiplying the probabilities of each individual N-gram in the sequence.
- However, unsmoothed N-grams suffer from several limitations, including the sparsity problem and the inability to handle unseen N-grams.
- The sparsity problem arises because many N-grams will have zero frequency in a given corpus, making it difficult to accurately estimate their probability.
- The inability to handle unseen N-grams means that if a new N-gram appears in the test data that was not present in the training data, its probability will be estimated as zero, leading to poor performance.
- Despite these limitations, unsmoothed N-grams are still widely used as a baseline language modeling technique, and can be useful for quick prototyping and experimentation.

In summary, unsmoothed N-grams are a simple and easy-to-implement language modeling technique, but suffer from several limitations that can impact their performance. However, they are still a useful baseline technique for natural language processing tasks, and can be a good starting point for further experimentation and refinement.