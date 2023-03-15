### Physical models for data compression

- Physical models are mathematical representations of the source data that capture the statistical properties and dependencies of the data.
- Physical models are used to estimate the probabilities of the data symbols and sequences, which are then used to design optimal codes for compression.
- Physical models can be classified into two types: memoryless and memory-based models.
- Memoryless models assume that each symbol in the data is independent of the previous symbols, and has a fixed probability distribution. Examples of memoryless models are uniform distribution, geometric distribution, and Huffman coding.
- Memory-based models assume that the probability of a symbol depends on the previous symbols, and can vary over time. Examples of memory-based models are Markov models, finite context models, and arithmetic coding.
- Memory-based models can achieve higher compression ratios than memoryless models, but they are also more complex and require more computation and memory resources.