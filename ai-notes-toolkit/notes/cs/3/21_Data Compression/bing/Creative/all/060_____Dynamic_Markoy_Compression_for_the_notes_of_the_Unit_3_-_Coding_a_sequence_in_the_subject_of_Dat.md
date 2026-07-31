# Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It is based on the idea of Markov chains, which are mathematical models of systems that transition from one state to another with some probability.
- DMC builds a dynamic Markov model of the input data, which adapts to the changing patterns and frequencies of the bits.
- The model consists of a tree of nodes, each representing a context or a history of previous bits. The root node represents the empty context, and each child node represents a context with one more bit appended.
- Each node has two counters, one for the number of times a 0 bit has followed the context, and one for the number of times a 1 bit has followed the context.
- The counters are used to estimate the probability of the next bit given the context, which is then fed to the arithmetic coder.
- The model is initialized with a single root node, and new nodes are created as new contexts are encountered in the input.
- The model is also pruned periodically to remove nodes with low counts, to save memory and avoid overfitting.
- DMC is an effective and flexible compression algorithm that can adapt to various types of data and achieve high compression ratios. However, it is also computationally intensive and requires a large amount of memory.