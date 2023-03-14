 Here is the content in markdown format for the topic ### Word Similarity using Thesaurus and Distributional methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing:

### Word Similarity using Thesaurus and Distributional methods

Thesaurus based methods:
- Calculate similarity between words based on overlap of synsets (synonym sets) from a thesaurus like WordNet.
- Higher the number of shared synsets, higher the similarity.
- Advantage: Incorporates semantic relationships between words.
- Disadvantage: Limited coverage of words and senses in thesauri.

Distributional methods:
- Calculate similarity based on co-occurrence patterns of words in large corpora.
- Words that occur in similar contexts are considered similar in meaning.
- Examples: Count-based cosine similarity, Predictive measures like Pointwise Mutual Information (PMI).
- Advantage: Scales to larger vocabularies and can capture contextual nuances.
- Disadvantage: Crippled by polysemy and semantic ambiguity without additional features or constraints.

Combined approaches:
- Integrate thesaurus-based and distributional similarities to overcome individual limitations.
- Examples: Extending distributional models with thesaurus-based similarities as features, or combining multiple measures via ensemble methods or dimensionality reduction techniques.
- These combined approaches have been shown to produce more robust semantic similarity estimates.

Mnemonics/Learning tricks:
- Shared synsets -> Higher similarity (Thesaurus method)
- Similar contexts -> Higher similarity (Distributional method)
- Combine advantages, overcome individual limitations (Combined approaches)

Detailed diagrams/examples/applications can be included if required. The content can be made more formal by avoiding contractions and colloquial language.