# Language Modeling

- Language modeling is the task of estimating the probability of a sequence of words or a word given some context  .
- Language models are useful for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc.
- Language models can be classified into two types: **generative** and **discriminative**.
  - Generative models learn the joint probability of the input and the output, and can generate new samples from the learned distribution. For example, a generative language model can generate a sentence given a topic or a keyword.
  - Discriminative models learn the conditional probability of the output given the input, and can predict the most likely output for a given input. For example, a discriminative language model can predict the next word given the previous words in a sentence.
- Language models can also be categorized based on the **order** of the words they consider.
  - **N-gram models** are the simplest and most widely used language models. They assume that the probability of a word depends only on the previous n-1 words, where n is a fixed parameter. For example, a bigram model (n=2) assumes that the probability of a word depends only on the previous word.
  - **Neural network models** are more advanced and powerful language models. They use neural networks to learn complex and non-linear relationships between words. They can consider longer contexts and capture semantic and syntactic information. For example, a recurrent neural network (RNN) model can process a sequence of words one by one and update its hidden state at each step.
- Language models can be evaluated using different metrics, such as **perplexity**, **accuracy**, **bleu score**, etc.
  - Perplexity measures how well a language model predicts a test set. It is the inverse of the average probability assigned to each word in the test set. A lower perplexity means a better language model.
  - Accuracy measures the percentage of correct predictions made by a language model. It is the ratio of the number of correct predictions to the total number of predictions. A higher accuracy means a better language model.
  - Bleu score measures the quality of a generated text by comparing it to one or more reference texts. It is based on the number of matching n-grams between the generated text and the reference texts. A higher bleu score means a better language model.