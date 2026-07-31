### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, where each node represents a context (a sequence of bits) and has two children nodes corresponding to the next bit being 0 or 1 .
- The model is initialized with a single root node, and new nodes are created as new contexts are encountered in the input .
- Each node stores a count of how many times each bit has occurred in that context, which is used to estimate the probability of the next bit .
- The arithmetic coder uses these probabilities to encode the input bits with variable-length codes, where more probable bits are assigned shorter codes and less probable bits are assigned longer codes .
- The model is updated after each bit is encoded, by incrementing the corresponding count in the current node and creating a new node if necessary .
- The model is also pruned periodically to remove nodes with low counts, to avoid overfitting and reduce memory usage .
- DMC is an adaptive algorithm, which means that it does not require any prior knowledge of the input data and can adjust to changes in the data distribution .
- DMC can achieve high compression ratios for various types of data, especially those with long-range dependencies or repetitive patterns .
- DMC is also relatively simple and fast, compared to other adaptive algorithms like PPM .