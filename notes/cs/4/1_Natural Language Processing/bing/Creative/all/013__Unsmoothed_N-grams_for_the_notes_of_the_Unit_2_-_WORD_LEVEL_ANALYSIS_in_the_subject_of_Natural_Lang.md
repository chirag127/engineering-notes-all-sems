### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- An **n-gram** is a sequence of n words from a text or speech.
- An **unsmoothed n-gram** is an n-gram that is assigned a probability based on its frequency in the training data, without any adjustment for unseen or rare n-grams.
- The probability of an unsmoothed n-gram is calculated as follows:

    - P(w<sub>n</sub> | w<sub>n-1</sub>, ..., w<sub>1</sub>) = C(w<sub>n</sub>, w<sub>n-1</sub>, ..., w<sub>1</sub>) / C(w<sub>n-1</sub>, ..., w<sub>1</sub>)
    - where C(w<sub>n</sub>, w<sub>n-1</sub>, ..., w<sub>1</sub>) is the count of the n-gram (w<sub>n</sub>, w<sub>n-1</sub>, ..., w<sub>1</sub>) in the training data, and C(w<sub>n-1</sub>, ..., w<sub>1</sub>) is the count of the (n-1)-gram (w<sub>n-1</sub>, ..., w<sub>1</sub>) in the training data.

- For example, if we have a training data of 10 sentences, and we want to calculate the probability of the unsmoothed bigram (the, cat) using the formula above, we need to count how many times the bigram (the, cat) and the unigram (the) appear in the data. Suppose we have the following counts:

    - C(the, cat) = 3
    - C(the) = 5

- Then, the probability of the unsmoothed bigram (the, cat) is:

    - P(cat | the) = C(the, cat) / C(the) = 3 / 5 = 0.6

- The advantages of unsmoothed n-grams are:

    - They are easy to implement and compute.
    - They capture the local context and word order of the text or speech.

- The disadvantages of unsmoothed n-grams are:

    - They suffer from data sparsity, meaning that many n-grams that are possible in the language may not appear in the training data, and thus have zero probability.
    - They suffer from overfitting, meaning that they assign high probabilities to n-grams that are frequent in the training data, but may not generalize well to unseen data.
    - They do not account for the semantic or syntactic relations between words, and may produce nonsensical or ungrammatical n-grams.

- A mnemonic to remember the formula for unsmoothed n-gram probability is:

    - **N**-gram probability = **N**umerator / de**N**ominator
    - where the numerator is the count of the n-gram, and the denominator is the count of the (n-1)-gram.
    - Alternatively, you can think of the formula as:

    - P(last word | previous words) = count of (last word, previous words) / count of previous words