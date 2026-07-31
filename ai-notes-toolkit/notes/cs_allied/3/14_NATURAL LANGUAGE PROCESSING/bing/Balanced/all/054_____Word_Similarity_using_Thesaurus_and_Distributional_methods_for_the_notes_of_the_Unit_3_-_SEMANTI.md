# Word Similarity using Thesaurus and Distributional methods

- Word similarity is the degree to which two words share a common meaning or are semantically related.
- Word similarity can be measured using different methods, such as thesaurus-based methods and distributional methods.
- Thesaurus-based methods rely on manually constructed lexical resources, such as WordNet, Roget's Thesaurus, or BabelNet, that group words into synonym sets or semantic categories.
- Thesaurus-based methods measure word similarity by counting the number of shared categories or the distance between words in a semantic hierarchy.
- Thesaurus-based methods have the advantage of capturing fine-grained semantic distinctions and relations, but they also have some limitations, such as:
  - They are incomplete and may not cover all the words or senses in a language.
  - They are static and may not reflect the dynamic and evolving nature of language use and meaning.
  - They are subjective and may not agree with the intuition or judgment of different users or domains.
- Distributional methods are based on the distributional hypothesis, which states that words that occur in similar contexts tend to have similar meanings.
- Distributional methods measure word similarity by analyzing the co-occurrence patterns of words in large corpora of text.
- Distributional methods represent words as vectors of numerical features, where each feature corresponds to a context word or a dimension of meaning.
- Distributional methods compute word similarity by applying mathematical functions, such as cosine similarity, Jaccard coefficient, or Dice coefficient, to compare the vectors of two words.
- Distributional methods have the advantage of being data-driven and scalable, but they also have some challenges, such as:
  - They require large and representative corpora to capture the diversity and richness of word meanings.
  - They may not distinguish between different senses or aspects of meaning of a word.
  - They may not capture the semantic relations or nuances that are not reflected by co-occurrence patterns.