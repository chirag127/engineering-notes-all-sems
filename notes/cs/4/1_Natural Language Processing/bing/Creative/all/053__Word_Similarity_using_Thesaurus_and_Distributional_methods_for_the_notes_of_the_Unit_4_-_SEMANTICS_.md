### Word Similarity using Thesaurus and Distributional methods for the notes of the Unit 4 - SEMANTICS AND PRAGMATICS in the subject of Natural Language Processing

- Word similarity is a measure of how closely related two words are in terms of their meaning.
- Word similarity can be used for various NLP tasks, such as word sense disambiguation, synonym identification, text summarization, sentiment analysis, machine translation, and chatbots.
- There are two main methods for computing word similarity: thesaurus-based and distributional-based.

#### Thesaurus-based methods
- Thesaurus-based methods rely on manually curated lexical resources, such as WordNet, that organize words into hierarchical structures based on their semantic relations, such as synonymy, antonymy, hypernymy, and hyponymy.
- Thesaurus-based methods compute word similarity by finding the shortest path between two words in the semantic network, or by comparing the features or definitions of the words.
- Thesaurus-based methods have the advantage of capturing fine-grained semantic distinctions and nuances, but they also have some limitations, such as:
  - They are not comprehensive and may not cover all the words or senses in a given domain or corpus.
  - They are not dynamic and may not reflect the changes or variations in word usage over time or across contexts.
  - They are not language-independent and may not be available or consistent for different languages.

#### Distributional-based methods
- Distributional-based methods rely on the distributional hypothesis, which states that words that occur in similar contexts tend to have similar meanings (Harris, 1985).
- Distributional-based methods compute word similarity by analyzing the co-occurrence patterns of words in large corpora, and representing them as numerical vectors in a high-dimensional space, where the dimensions correspond to the features or contexts of the words.
- Distributional-based methods have the advantage of being data-driven and scalable, but they also have some challenges, such as:
  - They require large and representative corpora to capture the diversity and richness of word meanings.
  - They may not distinguish between different senses or aspects of a word, and may conflate similarity with relatedness or association.
  - They may not capture the semantic relations or structure among words, and may depend on the choice of features, dimensions, or similarity measures.

#### Comparison and combination of thesaurus-based and distributional-based methods
- Thesaurus-based and distributional-based methods have complementary strengths and weaknesses, and can be combined to achieve better performance and coverage for word similarity tasks.
- For example, one can use a thesaurus to provide a coarse-grained semantic clustering of words, and then use a distributional method to refine the similarity within each cluster.
- Alternatively, one can use a distributional method to provide a dense and continuous representation of words, and then use a thesaurus to provide a sparse and discrete representation of words, and then combine them using a weighted or hybrid similarity measure.
- Some examples of hybrid methods are:
  - Patwardhan and Pedersen (2006) combined WordNet and corpus statistics to compute word similarity based on semantic nets and information content.
  - Mihalcea et al. (2006) combined WordNet and Wikipedia to compute word similarity based on knowledge-based and corpus-based features.
  - Agirre et al. (2009) combined WordNet and word embeddings to compute word similarity based on supervised learning and distributional features.