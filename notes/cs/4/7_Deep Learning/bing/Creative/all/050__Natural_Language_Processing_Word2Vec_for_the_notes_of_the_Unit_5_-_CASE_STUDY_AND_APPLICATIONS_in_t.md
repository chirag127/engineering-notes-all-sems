### Natural Language Processing Word2Vec for the notes of the Unit 5 - CASE STUDY AND APPLICATIONS in the subject of Deep Learning

- Word2vec is a technique for natural language processing (NLP) that uses a neural network model to learn word associations from a large corpus of text.
- Word2vec produces a vector space, typically of several hundred dimensions, with each unique word in the corpus being assigned a corresponding vector in the space.
- The vectors are chosen carefully such that they capture the semantic and syntactic qualities of words; as such, a simple mathematical function (cosine similarity) can indicate the level of semantic similarity between the words represented by those vectors.
- Word2vec is a group of related models that are used to produce word embeddings, which are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words.
- There are two main variants of word2vec: skip-gram and continuous bag of words (CBOW).
  - Skip-gram predicts the context words given a target word, while CBOW predicts the target word given the context words.
  - Skip-gram tends to perform better on rare words, while CBOW tends to perform better on frequent words.
- Word2vec can be implemented using TensorFlow, a popular framework for deep learning.
  - TensorFlow provides a high-level API for word2vec, as well as a low-level API for customizing the model.
  - TensorFlow also provides a visualization tool called TensorBoard, which can be used to explore the learned embeddings.
- Word2vec has many applications in NLP, such as machine translation, semantic analysis, question answering, etc.
  - Word2vec can help to find synonyms, antonyms, analogies, and other semantic relations between words.
  - Word2vec can also help to reduce the dimensionality of the input data, and improve the performance of downstream tasks.

Some possible mnemonics and learning tricks for word2vec are:

- Word2vec: 2 words, 2 models (skip-gram and CBOW)
- Skip-gram: skip the target, predict the context
- CBOW: bag the context, predict the target
- Cosine similarity: measure the angle between vectors
- TensorFlow: flow of tensors (multidimensional arrays) through a graph of operations
- TensorBoard: board for visualizing tensors and graphs