### Word Similarity using Thesaurus and Distributional methods

- Word similarity is a measure of how closely related two words are in terms of their meaning, usage, or association.
- Word similarity can be computed using different methods, such as thesaurus-based methods and distributional methods.
- Thesaurus-based methods rely on manually curated lexical resources, such as WordNet, that group words into synsets (sets of synonyms) and link them with semantic relations, such as hypernymy (is-a), meronymy (part-of), antonymy (opposite-of), etc.
- Thesaurus-based methods can compute word similarity by counting the number of steps or links between two words in the thesaurus hierarchy, or by comparing the features or attributes of the words, such as their definitions, examples, or glosses.
- Distributional methods rely on large corpora of text, such as Wikipedia, that provide statistical information about how words co-occur with other words in different contexts.
- Distributional methods can compute word similarity by representing words as vectors of numerical values, where each value corresponds to the frequency or weight of a word in a given dimension or feature, such as a document, a topic, or a word cluster.
- Distributional methods can compare word vectors using different similarity measures, such as cosine similarity, Jaccard similarity, or Euclidean distance, to obtain a score between 0 and 1, where 0 means no similarity and 1 means perfect similarity.
- Both thesaurus-based methods and distributional methods have advantages and disadvantages, such as:
  - Thesaurus-based methods can capture fine-grained semantic distinctions and relations, but they are limited by the coverage and quality of the thesaurus, and they may not reflect the current or dynamic usage of words in natural language.
  - Distributional methods can capture general and contextual similarity, but they may not capture the nuances or subtleties of meaning, and they may be affected by noise or sparsity of data in the corpus.