# Probability models for data compression

- Probability models are mathematical representations of the source data that assign probabilities to different symbols or sequences of symbols.
- Probability models are used to estimate the entropy or information content of the source data, which is the lower bound for the compression ratio.
- Probability models are also used to design optimal codes that assign shorter codewords to more probable symbols or sequences, and longer codewords to less probable ones.
- Probability models can be classified into two types: static and adaptive.
  - Static models are fixed and do not change during the compression process. They are based on some prior knowledge or analysis of the source data.
  - Adaptive models are dynamic and change during the compression process. They are based on the observed frequencies or statistics of the source data.
- Some examples of probability models are:
  - Uniform model: This model assumes that all symbols in the source alphabet have equal probability. It is suitable for random or unpredictable data, but not for data with patterns or structure.
  - Bernoulli model: This model assumes that the source data consists of binary symbols (0 or 1) that have a fixed probability p of being 1 and 1-p of being 0. It is suitable for data with a constant bias or skewness.
  - Markov model: This model assumes that the probability of a symbol depends on the previous k symbols, where k is the order of the model. It is suitable for data with dependencies or correlations among symbols, such as text or speech.
  - Dictionary model: This model assumes that the source data consists of words or phrases that are drawn from a finite set or dictionary. It is suitable for data with repetitions or commonalities, such as natural language or DNA sequences.