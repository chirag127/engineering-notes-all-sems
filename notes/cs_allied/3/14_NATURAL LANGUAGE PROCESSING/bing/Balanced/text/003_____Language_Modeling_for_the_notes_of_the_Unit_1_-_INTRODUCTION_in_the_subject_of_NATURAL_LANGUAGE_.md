### Language Modeling

- Language modeling is the task of estimating the probability of a sequence of words or a word given its context .
- Language models are useful for various natural language processing applications, such as speech recognition, machine translation, text summarization, text generation, etc .
- Language models can be classified into two types: **generative** and **discriminative**.
  - Generative models learn the joint probability of the input and the output, and can generate new samples from the learned distribution. Examples of generative models are n-gram models, hidden Markov models, etc.
  - Discriminative models learn the conditional probability of the output given the input, and can predict the most likely output for a given input. Examples of discriminative models are logistic regression, support vector machines, neural networks, etc.
- Language models can also be categorized based on the level of granularity they operate on: **word-level**, **character-level**, or **subword-level**.
  - Word-level models treat each word as an atomic unit and assign a probability to each word in the vocabulary. Word-level models suffer from data sparsity and out-of-vocabulary issues.
  - Character-level models treat each character as an atomic unit and assign a probability to each character in the alphabet. Character-level models can handle any word, but they require longer sequences and more computation.
  - Subword-level models split words into smaller units, such as syllables, morphemes, or byte-pair encodings. Subword-level models can balance between word-level and character-level models, and can capture both lexical and morphological information.
- Language models can also be distinguished based on the architecture they use: **statistical** or **neural** .
  - Statistical models rely on counting and smoothing techniques to estimate the probabilities of word sequences. Statistical models are simple, fast, and interpretable, but they have limited expressive power and cannot capture long-term dependencies .
  - Neural models use artificial neural networks to learn the probabilities of word sequences. Neural models are complex, slow, and opaque, but they have high expressive power and can capture long-term dependencies .
- Language models can be evaluated using two main metrics: **perplexity** and **likelihood** .
  - Perplexity measures how well a language model predicts a test set. It is the inverse of the geometric mean of the probabilities assigned to each word in the test set. Lower perplexity means better performance .
  - Likelihood measures how probable a test set is according to a language model. It is the product of the probabilities assigned to each word in the test set. Higher likelihood means better performance .