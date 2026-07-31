# Word Similarity using Thesaurus and Distributional methods

## Thesaurus-based methods

- A thesaurus is a collection of words grouped by their semantic similarity or relatedness, such as synonyms, antonyms, hypernyms, hyponyms, etc.
- A thesaurus can be used to measure the similarity between two words by finding the shortest path between them in the thesaurus hierarchy or graph.
- For example, WordNet is a popular thesaurus that organizes words into synsets (sets of synonyms) and links them with semantic relations.
- The similarity between two words can be computed by using various metrics based on the depth, distance, and density of the synsets and relations in WordNet, such as path length, Leacock-Chodorow, Wu-Palmer, Resnik, Jiang-Conrath, Lin, etc.
- Thesaurus-based methods have the advantage of capturing fine-grained semantic distinctions and relations, but they also have some limitations, such as:
  - They require manual construction and maintenance, which is costly and time-consuming.
  - They may not cover all the words and senses in a language, especially new or domain-specific terms.
  - They may not reflect the actual usage and context of words in natural language texts.

## Distributional methods

- Distributional methods are based on the assumption that words that occur in similar contexts tend to have similar meanings, also known as the distributional hypothesis.
- Distributional methods use large corpora of text to automatically learn vector representations of words, also known as word embeddings, that capture their semantic and syntactic features.
- The similarity between two words can be measured by computing the cosine similarity or other distance metrics between their word embeddings.
- For example, word2vec, GloVe, fastText, BERT, etc. are some of the popular methods for learning word embeddings from text data.
- Distributional methods have the advantage of being data-driven and scalable, but they also have some limitations, such as:
  - They may not capture the subtle nuances and relations between words that are not reflected by their co-occurrence patterns.
  - They may be sensitive to the choice of corpus, parameters, and algorithms used to learn the word embeddings.
  - They may not account for the polysemy and ambiguity of words that have multiple meanings or senses.