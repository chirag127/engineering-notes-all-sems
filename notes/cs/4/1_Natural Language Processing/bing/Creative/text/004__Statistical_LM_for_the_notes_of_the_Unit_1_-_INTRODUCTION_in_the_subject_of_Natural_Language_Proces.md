### Statistical LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- A statistical language model (LM) is a probabilistic model that assigns a probability to a sequence of words or symbols, such as a sentence or a document.
- A statistical LM can be used for various natural language processing (NLP) tasks, such as speech recognition, machine translation, text summarization, text generation, etc.
- A statistical LM can be built from a large corpus of text data, by estimating the probabilities of word occurrences and word combinations based on their frequencies in the corpus.
- A statistical LM can be evaluated by measuring how well it predicts unseen text data, using metrics such as perplexity, which is the inverse of the average probability assigned to each word in the test data.
- A statistical LM can be improved by using various techniques, such as smoothing, which is the process of assigning some probability mass to unseen or rare word combinations, or back-off, which is the process of using lower-order probabilities when higher-order probabilities are not available.
- A statistical LM can be classified into different types, based on the assumptions and methods used to estimate the probabilities. Some common types of statistical LMs are:

  - N-gram models, which use the Markov assumption that the probability of a word depends only on the previous n-1 words, where n is the order of the model. For example, a bigram model uses the previous word, and a trigram model uses the previous two words, to predict the next word.
  - Neural network models, which use a neural network architecture, such as a recurrent neural network (RNN), a long short-term memory (LSTM), or a transformer, to learn the probabilities of word sequences from the text data. These models can capture long-range dependencies and semantic information that n-gram models cannot.
  - Topic models, which use a generative process to model the text data as a mixture of topics, where each topic is a distribution over words. These models can discover the latent topics and themes in the text data, and can be used for text analysis and summarization.