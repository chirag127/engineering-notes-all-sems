# Word Similarity using Thesaurus and Distributional methods

Word similarity is a measure of the degree to which two words are related in meaning. There are two main approaches to measuring word similarity: thesaurus-based methods and distributional methods.

## Thesaurus-based methods

Thesaurus-based methods use a thesaurus, which is a reference work that lists words grouped together according to similarity of meaning, to determine the similarity between two words. The basic idea is that if two words are listed as synonyms in a thesaurus, they are considered to be similar in meaning.

There are several ways to measure the similarity between two words using a thesaurus. One approach is to measure the distance between the two words in the thesaurus hierarchy. The shorter the distance, the more similar the words are considered to be. Another approach is to measure the overlap between the sets of synonyms for the two words. The greater the overlap, the more similar the words are considered to be.

## Distributional methods

Distributional methods, on the other hand, use the distribution of words in large corpora of text to determine the similarity between two words. The basic idea is that if two words tend to occur in similar contexts, they are considered to be similar in meaning.

There are several ways to measure the similarity between two words using distributional methods. One approach is to use vector space models, where words are represented as vectors in a high-dimensional space, and the similarity between two words is measured by the cosine of the angle between their vectors. Another approach is to use probabilistic models, where the similarity between two words is measured by the probability that they co-occur in the same context.

Both thesaurus-based and distributional methods have their strengths and weaknesses. Thesaurus-based methods are good at capturing fine-grained distinctions in meaning, but they rely on the availability of a high-quality thesaurus, which may not always be available. Distributional methods, on the other hand, can be applied to any large corpus of text, but they may not be as good at capturing fine-grained distinctions in meaning. In practice, a combination of both methods is often used to achieve the best results.