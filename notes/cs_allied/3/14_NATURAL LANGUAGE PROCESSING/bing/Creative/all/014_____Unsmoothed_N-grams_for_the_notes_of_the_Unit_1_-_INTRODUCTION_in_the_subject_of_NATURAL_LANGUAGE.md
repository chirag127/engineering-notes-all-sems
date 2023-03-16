# Unsmoothed N-grams

- An **n-gram** is a sequence of **n** words or symbols in a text or speech  .
- For example, "natural language processing" is a **trigram** (n = 3), "machine learning" is a **bigram** (n = 2), and "statistics" is a **unigram** (n = 1).
- An **n-gram model** is a probabilistic model that predicts the next word or symbol based on the previous **n - 1** words or symbols   .
- For example, a trigram model estimates the probability of a word given the previous two words, such as P(processing | natural language).
- An **unsmoothed n-gram model** is a simple n-gram model that uses the **maximum likelihood estimation** (MLE) to calculate the probabilities based on the **relative frequencies** of the n-grams in the training data .
- For example, the MLE of a trigram probability is given by:

![P(w_n | w_{n-2} w_{n-1}) = \frac{C(w_{n-2} w_{n-1} w_n)}{C(w_{n-2} w_{n-1})}](https://render.githubusercontent.com/render/math?math=P(w_n%20%7C%20w_%7Bn-2%7D%20w_%7Bn-1%7D)%20%3D%20%5Cfrac%7BC(w_%7Bn-2%7D%20w_%7Bn-1%7D%20w_n)%7D%7BC(w_%7Bn-2%7D%20w_%7Bn-1%7D)%7D)

where C(w<sub>n-2</sub> w<sub>n-1</sub> w<sub>n</sub>) is the **count** of the trigram w<sub>n-2</sub> w<sub>n-1</sub> w<sub>n</sub> and C(w<sub>n-2</sub> w<sub>n-1</sub>) is the count of the bigram w<sub>n-2</sub> w<sub>n-1</sub> in the training data.

- An unsmoothed n-gram model has some advantages and disadvantages  :
  - Advantages:
    - It is easy to implement and understand.
    - It captures the local context and order of the words or symbols.
    - It can be used for various tasks such as language identification, speech recognition, text generation, etc.
  - Disadvantages:
    - It suffers from **data sparsity** and **overfitting** problems, meaning that it assigns zero probability to unseen n-grams and high probability to frequent n-grams, which may not generalize well to new data.
    - It requires a large amount of training data and memory to store all the possible n-grams and their counts.
    - It ignores the long-range dependencies and semantic relations between the words or symbols.