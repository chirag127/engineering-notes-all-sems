### Unsmoothed N-grams

- An **n-gram** is a sequence of **n** words or tokens in a text document .
- For example, "natural language processing" is a **trigram** (n = 3), "machine learning" is a **bigram** (n = 2), and "statistics" is a **unigram** (n = 1).
- N-grams are used to model the probability of a word given its previous words in a sentence or document  .
- An **n-gram model** is a type of **statistical language model** that estimates the probability of a word or token by counting the frequency of n-grams in a large corpus of text  .
- For example, a **bigram model** estimates the probability of a word w given its previous word u as P(w|u) = C(uw) / C(u), where C(uw) is the count of the bigram uw and C(u) is the count of the unigram u in the corpus.
- Similarly, a **trigram model** estimates the probability of a word w given its previous two words u and v as P(w|uv) = C(uvw) / C(uv), where C(uvw) is the count of the trigram uvw and C(uv) is the count of the bigram uv in the corpus.
- An **unsmoothed n-gram model** is a simple n-gram model that does not apply any smoothing technique to deal with the problem of **zero probabilities** .
- A **zero probability** occurs when an n-gram does not appear in the corpus, resulting in a zero count and a zero probability estimate .
- For example, if the bigram "natural language" does not appear in the corpus, then P(language|natural) = 0, which means that the bigram model assigns zero probability to any sentence that contains the bigram "natural language".
- A zero probability can cause problems for applications that rely on n-gram models, such as **speech recognition**, **machine translation**, **text generation**, etc .
- Therefore, **smoothing techniques** are used to assign non-zero probabilities to unseen n-grams by redistributing some probability mass from seen n-grams to unseen n-grams  .
- Some examples of smoothing techniques are **additive smoothing**, **Good-Turing smoothing**, **Kneser-Ney smoothing**, etc .
- However, unsmoothed n-gram models can still be useful for some tasks, such as **text similarity**, **text classification**, **information retrieval**, etc., where the relative frequency of n-grams is more important than their absolute probability .