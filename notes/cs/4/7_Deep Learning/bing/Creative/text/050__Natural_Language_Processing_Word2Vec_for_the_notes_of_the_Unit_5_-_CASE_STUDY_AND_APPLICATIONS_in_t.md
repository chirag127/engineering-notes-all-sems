### Natural Language Processing Word2Vec

- Natural Language Processing (NLP) is the field of computer science that deals with understanding and generating natural language texts and speech.
- Word2vec is a technique for NLP that was published in 2013 by Mikolov et al. 
- Word2vec uses a neural network model to learn word associations from a large corpus of text. Once trained, such a model can detect synonymous words or suggest additional words for a partial sentence.
- Word2vec represents each distinct word with a particular list of numbers called a vector. The vectors are chosen carefully such that they capture the semantic and syntactic qualities of words; as such, a simple mathematical function (cosine similarity) can indicate the level of semantic similarity between the words represented by those vectors.
- Word2vec is a group of related models that are used to produce word embeddings. These models are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words. Word2vec takes as its input a large corpus of text and produces a vector space, typically of several hundred dimensions, with each unique word in the corpus being assigned a corresponding vector in the space. 
- There are two main variants of word2vec: skip-gram and continuous bag of words (CBOW). Skip-gram predicts the context words given a target word, while CBOW predicts the target word given the context words. Both models use a sliding window to define the context of a word in a sentence. 
- Word2vec can be implemented using various frameworks, such as TensorFlow , PyTorch, or Gensim. Word2vec can also be applied to different tasks, such as text classification, sentiment analysis, machine translation, or question answering. 
- Word2vec is a powerful and popular technique for NLP that can capture the meaning and relationships of words in a vector space. Word2vec can be used to perform various downstream NLP tasks that require some notion of similarity and difference between words. 

: Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. In Advances in neural information processing systems (pp. 3111-3119).

: CS224n: Natural Language Processing with Deep Learning. Lecture Notes: Part I. Word Vectors I: Introduction, SVD and Word2Vec. Winter 2019.

: word2vec | TensorFlow Core. https://www.tensorflow.org/tutorials/text/word2vec

: A Beginner's Guide to Word2Vec and Neural Word Embeddings. https://wiki.pathmind.com/word2vec