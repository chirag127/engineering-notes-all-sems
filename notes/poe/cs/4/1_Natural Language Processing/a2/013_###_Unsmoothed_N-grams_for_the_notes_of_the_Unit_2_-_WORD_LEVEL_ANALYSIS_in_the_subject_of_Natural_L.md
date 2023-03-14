 Here is the content in Markdown format:

### Unsmoothed N-grams for the notes of the Unit 2 - WORD LEVEL ANALYSIS in the subject of Natural Language Processing

Unsmoothed n-grams are a simple way to estimate the probability of a word sequence (n-gram) without any smoothing. They directly compute the maximum likelihood estimate (MLE) of the n-gram probabilities from the training data.

**Advantages:**

- Simple to implement.
- Uses all available data.

**Disadvantages:**

- High variance (volatile/unstable estimates).
- Zero probability problem: Any n-gram not seen in the training data will get a probability of zero, which is problematic.

**Examples:**

- Suppose we have a 2-gram model trained on the sequence "the cat chased the dog".
- The MLE probability of "the cat" would be 2/5 = 0.4 (appears 2 out of 5 words).
- The MLE probability of "chased the" would be 1/5 = 0.2.
- The MLE probability of "python program" would be 0 (never appeared in training data), causing the zero probability problem.

**Applications:**

- Can be used as a baseline/benchmark for more complex models.
- For very large datasets where smoothing may not be as crucial.
- In domains where the training data is representative of the test data and novel n-grams are unlikely.

**Mnemonics:**

- "Simple zip zero" - Refers to advantages (simple) and disadvantages (zero probability) of unsmoothed n-grams.

**Learning tricks:**

- Implement unsmoothed n-grams as a baseline to get an idea of how much smoothing helps in practice.
- Compare unsmoothed and smoothed n-gram probabilities on examples to visually see the effect of smoothing.