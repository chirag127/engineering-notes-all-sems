### Statistical LM for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Statistical language models (LMs) are mathematical models that assign probabilities to sequences of words or symbols in a natural language.
- Statistical LMs are useful for various natural language processing (NLP) tasks, such as speech recognition, machine translation, text summarization, spelling correction, and information retrieval.
- Statistical LMs can be classified into two main types: n-gram models and neural network models.
- N-gram models are based on the assumption that the probability of a word depends only on the previous n-1 words, where n is a fixed integer. For example, a bigram model (n=2) assumes that the probability of a word depends only on the previous word.
- Neural network models are based on the idea of using artificial neural networks to learn complex and nonlinear relationships between words and their contexts. For example, a recurrent neural network (RNN) model can capture long-term dependencies between words by using a hidden state that is updated at each time step.
- Statistical LMs can be estimated from a large corpus of text data, using various methods such as maximum likelihood estimation, smoothing techniques, or backpropagation.
- Statistical LMs can be evaluated using various metrics, such as perplexity, which measures how well a model predicts unseen data, or word error rate, which measures how many errors a model makes when generating text.

Some mnemonics and learning tricks for Statistical LM are:

- To remember the difference between a parameter and a statistic, think of the phrase "a parameter is a population property, a statistic is a sample summary".
- To remember the formula for the probability of a word given its context in an n-gram model, think of the acronym "PWC": P(word|context) = C(context word) / C(context), where C is the count function.
- To remember the difference between statistical significance and practical significance, think of the phrase "statistical significance is about the sample size, practical significance is about the effect size".