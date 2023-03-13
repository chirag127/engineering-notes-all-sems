### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

- An **n-gram** is a sequence of n words from a text or speech.
- An **unsmoothed n-gram** is an n-gram that is estimated by counting the frequency of the n-gram in the text or speech, without any adjustment for unseen or rare n-grams.
- Unsmoothed n-grams are useful for modeling the probability of a word given its previous n-1 words, which is called the **conditional probability**.
- The conditional probability of a word w given its previous n-1 words, denoted by P(w|w1 w2 ... wn-1), can be estimated by the **maximum likelihood estimation (MLE)**, which is the ratio of the frequency of the n-gram to the frequency of the (n-1)-gram:

    P(w|w1 w2 ... wn-1) = C(w1 w2 ... wn) / C(w1 w2 ... wn-1)

    where C(w1 w2 ... wn) is the count of the n-gram w1 w2 ... wn in the text or speech, and C(w1 w2 ... wn-1) is the count of the (n-1)-gram w1 w2 ... wn-1 in the text or speech.

- For example, if we want to estimate the probability of the word "dog" given the previous two words "the brown" in a text, we can use the unsmoothed bigram (2-gram) model:

    P(dog|the brown) = C(the brown dog) / C(the brown)

    If the text contains 3 occurrences of "the brown dog" and 5 occurrences of "the brown", then the probability is:

    P(dog|the brown) = 3 / 5 = 0.6

- Unsmoothed n-grams have some advantages and disadvantages:

    - Advantages:
        - They are simple and easy to implement.
        - They can capture the local context and word order of the text or speech.
        - They can model the frequency and variability of the language data.

    - Disadvantages:
        - They suffer from **data sparsity**, which means that many n-grams may not occur in the text or speech, or occur very rarely, leading to zero or unreliable probability estimates.
        - They suffer from **overfitting**, which means that they may memorize the specific patterns of the text or speech, and fail to generalize to new or unseen data.
        - They suffer from **lack of generalization**, which means that they may not capture the semantic or syntactic relations between words, or the long-distance dependencies in the text or speech.

- To overcome the disadvantages of unsmoothed n-grams, various **smoothing techniques** have been proposed, which aim to adjust the probability estimates of n-grams by redistributing some probability mass from frequent n-grams to rare or unseen n-grams. Some examples of smoothing techniques are **add-one smoothing**, **Good-Turing smoothing**, **Kneser-Ney smoothing**, etc.