### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, where each node represents a context (a sequence of bits) and has two children nodes corresponding to the next bit being 0 or 1.
- The model is initialized with a single root node, and new nodes are created as new contexts are encountered in the input.
- Each node stores a count of how many times each bit has followed the context, and these counts are used to estimate the probabilities of the next bit.
- The probabilities are then fed to an arithmetic coder, which encodes the input bit by bit using fewer bits for more probable symbols.
- The model is updated after each bit is encoded, so that it adapts to the changing statistics of the input.
- DMC is able to achieve high compression ratios for various types of data, especially those with long-range dependencies or non-stationary characteristics .
- However, it also has some drawbacks, such as high memory and computational requirements, and slow encoding and decoding speeds .