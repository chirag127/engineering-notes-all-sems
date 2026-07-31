### Word Similarity using Thesaurus and Distributional methods

- Word similarity is the degree to which two words share a common meaning or are semantically related.
- Thesaurus and distributional methods are two approaches to measure word similarity based on different sources of information.
- Thesaurus methods rely on manually curated lexical resources that group words into categories or list synonyms and antonyms for each word. For example, WordNet is a popular thesaurus that organizes words into synsets (sets of synonyms) and defines semantic relations between them, such as hypernymy, hyponymy, meronymy, etc.
- Distributional methods rely on large corpora of text that provide evidence of how words are used in natural language. The underlying assumption is that words that occur in similar contexts tend to have similar meanings. For example, the words "car" and "truck" are likely to appear near the word "driving", so they are distributionally similar.
- To construct a distributional thesaurus, the following steps are usually performed:
  - Define the target words and the contexts for which similarity will be computed. Contexts can be words, phrases, sentences, documents, etc.
  - Extract the co-occurrence frequencies of the target words and their contexts from a corpus. This can be done using a sliding window, a syntactic parser, or other methods.
  - Apply some weighting scheme to the co-occurrence frequencies to reduce the effect of noise and sparsity. This can be done using pointwise mutual information, log-likelihood ratio, tf-idf, etc.
  - Apply some similarity measure to compare the co-occurrence vectors of the target words and rank their neighbors by decreasing similarity. This can be done using cosine similarity, Jaccard coefficient, Dice coefficient, etc.
- The quality and stability of a distributional thesaurus can be influenced by several parameters, such as the similarity measure, the frequency threshold, and the association score. These parameters can affect the agreement between different thesauri and the performance on extrinsic tasks, such as word sense disambiguation or semantic relatedness.