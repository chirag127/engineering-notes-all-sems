### Word Similarity using Thesaurus and Distributional methods

- Word similarity is the degree to which two words share a common meaning or are semantically related.
- Thesaurus and distributional methods are two approaches to measure word similarity based on different sources of information.
- Thesaurus methods rely on manually constructed lexical resources, such as WordNet, Roget's Thesaurus, or BabelNet, that group words into synonym sets or semantic categories.
- Distributional methods rely on automatically extracted statistical information from large corpora, based on the assumption that words that occur in similar contexts are similar in meaning.
- Thesaurus methods have the advantage of capturing fine-grained semantic distinctions and relations, but they are limited by the coverage and quality of the available resources, and they may not reflect the current usage of words in natural language.
- Distributional methods have the advantage of being scalable, adaptable, and data-driven, but they may not capture the nuances and subtleties of word meanings, and they may be sensitive to the choice of parameters, such as similarity measures, frequency thresholds, and association scores.
- Similarity measures are mathematical functions that quantify the degree of similarity between two words based on their representations, such as vectors, matrices, or graphs.
- Frequency thresholds are minimum values that filter out words or contexts that occur too rarely or too frequently in the corpus, to reduce noise and sparsity.
- Association scores are numerical values that indicate the strength of the association between a word and a context, such as pointwise mutual information, log-likelihood ratio, or cosine similarity.
- To construct a distributional thesaurus, the contexts in which a target word occurs are extracted from a corpus, and the frequencies of the co-occurring word-context pairs are computed. Then, a similarity measure is applied to compare the target word with other words based on their contexts, and a list of semantically related neighbors is generated for each target word, ranked by decreasing similarity.