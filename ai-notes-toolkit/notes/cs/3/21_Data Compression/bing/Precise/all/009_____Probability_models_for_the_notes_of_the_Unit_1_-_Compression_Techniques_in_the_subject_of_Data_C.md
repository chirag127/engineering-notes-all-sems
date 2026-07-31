# Probability Models for Unit 1 - Compression Techniques in Data Compression

Probability models are used in data compression to predict the likelihood of occurrence of different symbols in the data. These models are used to assign shorter codes to more frequently occurring symbols and longer codes to less frequently occurring symbols, resulting in a more efficient compression of the data.

Some common probability models used in data compression include:

1. **Uniform distribution:** In this model, all symbols are assumed to have an equal probability of occurrence. This model is simple to implement but may not result in the most efficient compression if the data does not have a uniform distribution of symbols.

2. **Empirical distribution:** In this model, the probability of occurrence of each symbol is estimated based on its frequency in the data. This model can result in more efficient compression if the data has a non-uniform distribution of symbols.

3. **Markov models:** In this model, the probability of occurrence of a symbol is estimated based on the previous symbols in the data. This model can result in more efficient compression if there are dependencies between the symbols in the data.

4. **Context-based models:** In this model, the probability of occurrence of a symbol is estimated based on the context in which it appears in the data. This model can result in more efficient compression if there are patterns or regularities in the data.

These are some of the probability models used in data compression. The choice of model depends on the characteristics of the data being compressed and the desired level of compression efficiency.