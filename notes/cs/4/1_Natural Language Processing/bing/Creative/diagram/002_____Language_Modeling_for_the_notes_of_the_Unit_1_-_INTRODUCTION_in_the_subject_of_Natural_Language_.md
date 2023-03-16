### Language Modeling

- Language modeling is the task of estimating the probability of a given sequence of words occurring in a natural language  .
- Language models are useful for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc.
- Language models can be classified into two types: **generative** and **discriminative**.
  - Generative models learn the joint probability of the input and output sequences, and can be used to generate new sequences.
  - Discriminative models learn the conditional probability of the output given the input, and can be used to select the best output among candidates.
- Language models can also be categorized based on the level of granularity they operate on: **word-level**, **character-level**, **subword-level**, or **multi-level**.
  - Word-level models treat each word as an atomic unit and assign probabilities to word sequences.
  - Character-level models treat each character as an atomic unit and assign probabilities to character sequences.
  - Subword-level models split words into smaller units, such as morphemes, syllables, or n-grams, and assign probabilities to subword sequences.
  - Multi-level models combine different levels of granularity and assign probabilities to mixed sequences of words, characters, and subwords.
- Language models can also be distinguished based on the method they use to estimate the probabilities: **count-based**, **neural**, or **hybrid**.
  - Count-based models use statistical methods, such as n-gram models, to count the frequency of word sequences in a large corpus and derive probabilities from them.
  - Neural models use deep learning methods, such as recurrent neural networks (RNNs), convolutional neural networks (CNNs), or transformers, to learn the probability distribution of word sequences from a large corpus in an end-to-end manner.
  - Hybrid models combine count-based and neural methods, such as neural network language models (NNLMs), to leverage the advantages of both approaches.