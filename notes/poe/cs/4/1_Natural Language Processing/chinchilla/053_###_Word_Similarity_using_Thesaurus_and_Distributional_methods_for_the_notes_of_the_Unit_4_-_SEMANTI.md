### Word Similarity using Thesaurus and Distributional methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

Word similarity is an important concept in the field of Natural Language Processing (NLP) as it helps in various applications like information retrieval, question answering, text classification, and others. Thesaurus and Distributional methods are two popular approaches to measure word similarity.

#### Thesaurus-based methods

Thesaurus-based methods rely on a pre-built knowledge source, like a dictionary or a thesaurus, to measure the similarity between two words. These methods use the structural and semantic information present in the knowledge source to identify the relatedness of the words.

Some popular thesaurus-based methods are:

- **Path-based methods:** These methods measure the similarity between two words based on the shortest path in the knowledge source. The path length indicates the level of similarity between the words. Some examples of path-based methods are Wu-Palmer Similarity and Leacock-Chodorow Similarity.
- **Information content-based methods:** These methods measure the similarity between two words based on the amount of information shared by them. The shared information is calculated using the entropy of the words in the knowledge source. Some examples of information content-based methods are Resnik Similarity and Jiang-Conrath Similarity.

#### Distributional methods

Distributional methods rely on the distributional hypothesis, which states that words that occur in similar contexts have similar meanings. These methods use statistical techniques to analyze the distributional patterns of words in a large corpus of text to measure their similarity.

Some popular distributional methods are:

- **Vector space models:** These models represent each word as a vector in a high-dimensional space based on its co-occurrence with other words in the corpus. The similarity between two words is measured by the cosine similarity between their vectors. Some examples of vector space models are Latent Semantic Analysis (LSA) and Word2Vec.
- **Pointwise Mutual Information (PMI):** PMI measures the co-occurrence of two words in a corpus and calculates their association strength. The similarity between two words is measured based on their PMI value. Some examples of PMI-based methods are Positive Pointwise Mutual Information (PPMI) and GloVe.

#### Mnemonics and learning tricks

- For Thesaurus-based methods, remember PATH and INFORMATION content as two important concepts.
- For Distributional methods, remember VECTOR space and POINTWISE mutual information as two important concepts.

#### Advantages and disadvantages

- Thesaurus-based methods are easy to interpret and provide human-readable information about the similarity between words. However, they rely heavily on the quality of the knowledge source.
- Distributional methods are data-driven and can capture the nuances of word meanings based on their context. However, they require a large amount of data and can be computationally expensive.

#### Applications

- Thesaurus and Distributional methods can be used for various NLP applications like text classification, information retrieval, and question answering.
- These methods can also be used to enhance the performance of other NLP tasks like sentiment analysis and named entity recognition.

In conclusion, both Thesaurus and Distributional methods are useful for measuring word similarity in NLP applications. The choice between the two methods depends on the specific requirements of the application and the availability of resources.