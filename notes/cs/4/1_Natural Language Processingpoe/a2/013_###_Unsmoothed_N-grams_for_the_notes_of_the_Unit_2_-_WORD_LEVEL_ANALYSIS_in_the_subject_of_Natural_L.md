 Here is the content in markdown format:

### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

Unsmoothed n-grams are the simplest n-gram models where the probability of a word is estimated directly from the training data without any smoothing techniques.

- Advantages: Simple to implement and train.
- Disadvantages: prone to overfitting and sparse data problems. The probability of unseen n-grams will be zero.

For example, consider the sentence "The cat chased the dog". The unigram, bigram and trigram models would be:

Unigram: P(The) = count(The)/count(all words)
         P(cat) = count(cat)/count(all words)
         ...

Bigram: P(The|start) = count(The cat)/count(all bigrams)
       P(cat|The) = count(The cat)/count(The _)
       ...

Trigram: P(The|start cat) = count(The cat chased)/count(all trigrams starting with "cat ")
        P(cat|The _) = count(The cat chased)/count(The __)
        ...

To overcome the sparse data problem and assign non-zero probabilities to unseen n-grams, smoothing techniques are used. The most common smoothing techniques are:

- Additive Smoothing (Laplace Smoothing)
- Good-Turing Smoothing
- Katz Backoff
- etc.

The above points and details can act as good notes to learn and read from for exams regarding Unsmoothed N-grams. Let me know if you would like me to elaborate on any of the points or add more details.