### Natural Language Processing Word2Vec

- Word2vec is a technique for natural language processing (NLP) published in 2013.
- The word2vec algorithm uses a neural network model to learn word associations from a large corpus of text.
- Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence.
- Word2vec is not a singular algorithm, rather, it is a family of model architectures and optimizations that can be used to learn word embeddings from large datasets.
- Embeddings learned through word2vec have proven to be successful on a variety of downstream natural language processing tasks.
- Word2vec “vectorizes” words, and by doing so it makes natural language computer-readable – we can start to perform powerful mathematical operations on words to detect their similarities.
- A neural word embedding represents a word with numbers. It’s a simple, yet unlikely, translation.
- Word2vec model is used for word representations in vector space which is founded by Tomas Mikolov and a group of the research teams from Google in 2013.
- It is a neural network model that attempts to explain the word embeddings based on a text corpus. These models work using context.
- Word2vec can be implemented using two methods: skip-gram and continuous bag of words (CBOW).
- Skip-gram predicts the context words given a target word, while CBOW predicts the target word given the context words.
- Both methods use a softmax function to compute the probabilities of the words, and a negative sampling technique to reduce the computational complexity.
- Word2vec can capture both syntactic and semantic similarities among words, as well as analogical reasoning.
- For example, word2vec can infer that "king - man + woman = queen" or that "Paris is to France as Berlin is to Germany".
- Word2vec can also be used to find the most similar words to a given word, or to perform word clustering.