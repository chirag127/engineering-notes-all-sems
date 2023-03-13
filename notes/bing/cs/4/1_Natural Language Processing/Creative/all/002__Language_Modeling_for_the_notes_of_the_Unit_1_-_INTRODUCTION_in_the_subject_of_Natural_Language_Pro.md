### Language Modeling for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Language modeling is the task of predicting the next word or character in a sequence of text, given the previous context .
- Language models are statistical tools that analyze the pattern of human language and assign probabilities to sequences of words or characters .
- Language models are the core component of many natural language processing (NLP) applications, such as speech recognition, machine translation, text summarization, question answering, sentiment analysis, and more   .
- Language models can be classified into two types: classical and neural.
  - Classical language models are based on counting the frequency of n-grams (sequences of n words or characters) in a large corpus of text, and using smoothing techniques to deal with unseen or rare n-grams.
  - Neural language models are based on using deep neural networks, such as recurrent neural networks (RNNs), convolutional neural networks (CNNs), or transformers, to learn the probability distribution of words or characters in a sequence, given the previous context .
- Language models can also be classified into two directions: unidirectional and bidirectional.
  - Unidirectional language models are trained to predict the next word or character, given the previous context, from left to right or from right to left.
  - Bidirectional language models are trained to predict the next word or character, given the previous and the following context, from both directions.
- Language models can be evaluated by two metrics: perplexity and accuracy.
  - Perplexity is a measure of how well a language model predicts a sample of text. It is defined as the inverse probability of the test set, normalized by the number of words or characters. A lower perplexity indicates a better language model.
  - Accuracy is a measure of how often a language model predicts the correct next word or character in a sequence. A higher accuracy indicates a better language model.
- Language models can be improved by using larger and more diverse corpora of text, using more complex and expressive neural architectures, using pre-training and fine-tuning techniques, and using regularization and optimization methods  .

Some mnemonics and learning tricks for language modeling are:

- To remember the definition of language modeling, think of LM as Language Modeling or Likelihood Maximization.
- To remember the types of language models, think of C as Classical or Counting, and N as Neural or Network.
- To remember the directions of language models, think of U as Unidirectional or Uni-directional, and B as Bidirectional or Both-directional.
- To remember the evaluation metrics of language models, think of P as Perplexity or Probability, and A as Accuracy or Answer.