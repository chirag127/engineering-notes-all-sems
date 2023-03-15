# Unit 3 - Coding a sequence

## Length of context

- The length of context is the number of symbols that are used to predict the next symbol in a sequence.
- The length of context affects the performance of compression algorithms, such as arithmetic coding and Lempel-Ziv coding.
- A longer context can capture more patterns and correlations in the data, leading to higher compression ratios.
- However, a longer context also requires more memory and computation to store and process the probabilities of each possible symbol given the context.
- Therefore, there is a trade-off between the length of context and the complexity of the compression algorithm.
- The optimal length of context depends on the characteristics of the data and the compression objective. For example, natural language texts may benefit from longer contexts that capture word and phrase frequencies, while images may require shorter contexts that capture pixel intensities and edges.
- A common way to determine the length of context is to use adaptive methods that adjust the context based on the data. For example, Lempel-Ziv coding uses a variable-length context that grows as new symbols are encountered, while arithmetic coding can use a sliding window that moves along the sequence.