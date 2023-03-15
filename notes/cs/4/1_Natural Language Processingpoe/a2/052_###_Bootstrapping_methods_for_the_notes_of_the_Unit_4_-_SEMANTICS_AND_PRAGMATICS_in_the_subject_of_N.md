 Here is the content in markdown format:

### Bootstrapping methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

Bootstrapping methods are unsupervised learning techniques used to learn semantic lexicons from corpora without the need for manual annotation. Some of the popular bootstrapping methods are:

- Mutual Expectation Maximization (MEM): It initializes seed sets of words for different semantic classes and iteratively adds words to the class whose members most frequently co-occur with the word. It maximizes the mutual expectation of words and classes.
- Co-occurrence Likelihood Ratio (CLR): It computes the likelihood ratio of the empirical co-occurrence frequencies of a word with the words in a semantic class versus the co-occurrence frequencies expected by chance. If the ratio exceeds a threshold, the word is added to the class.
- Semantic Vectors (SV): Words are represented as vectors where each dimension corresponds to a semantic class and the values are pointwise mutual information scores with the class words. Similar words have similar vectors and can be clustered.

**Advantages:**

- Unsupervised: No manual annotation required.
- Scalable: Can learn from large corpora.

**Disadvantages:**

- prone to errors: May add noisy words or omit relevant words.
- Depend on seed sets: Quality of results depends on the choice of initial seed words.

**Examples:** Learning semantic lexicons of nouns, adjectives, verbs, etc.

**Applications:** Text classification, information retrieval, question answering, etc.

I have included points, advantages, disadvantages, examples and applications as requested. Let me know if you would like me to elaborate on any of the points or include additional details.