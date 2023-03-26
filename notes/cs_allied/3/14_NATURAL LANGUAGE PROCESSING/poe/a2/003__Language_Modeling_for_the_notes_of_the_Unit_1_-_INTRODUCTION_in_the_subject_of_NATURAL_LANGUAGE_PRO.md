 Here is the content in markdown format without any emojis or external links:

### Language Modeling for the notes of the Unit 1 - INTRODUCTION in the subject of NATURAL LANGUAGE PROCESSING

1. Language modeling is a key component of many applications that involve processing and generation of text, such as machine translation, speech recognition, summarization, question answering, etc.
2. A language model is a probability distribution over sequences of words. It assigns a probability to a sequence of words (or tokens).
3. A language model can be used to determine the likelihood of a given sequence of words. This allows applications to determine the best choice from multiple options. For example, in speech recognition, the sequence of words with the highest probability given the acoustic signal is chosen.
4. The simplest language model is the unigram model which assumes that the probability of a word only depends on that individual word. However, this fails to capture the context and ordering of words.
5. N-gram models consider the previous N-1 words to compute the probability of the next word. For example, a bigram model considers the previous word, and a trigram model considers the previous two words. Higher order N-gram models can lead to better results but also suffer from data sparsity problems.
6. Smoothing techniques are used to tackle the data sparsity problem in N-gram models. Additive smoothing, interpolated smoothing, and backoff smoothing are some common smoothing techniques used.
7. Neural network based language models compute probabilities using a complex non-linear function and deep learning. They are able to capture long-range dependencies and generally lead to significant improvements in performance over N-gram models. Recurrent neural networks and transformer models are commonly used to build neural language models.

The content is written in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to modify or add any other content.