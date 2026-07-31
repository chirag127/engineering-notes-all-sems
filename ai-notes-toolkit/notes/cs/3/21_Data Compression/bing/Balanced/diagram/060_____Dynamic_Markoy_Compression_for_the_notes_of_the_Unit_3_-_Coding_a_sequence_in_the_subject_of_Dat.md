### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, where each node represents a context (a sequence of bits) and has two children nodes corresponding to the next bit being 0 or 1 .
- The model is initialized with a single root node, and new nodes are created and added to the tree as new contexts are encountered in the input .
- Each node stores a count of how many times each bit has followed the context, and these counts are used to estimate the conditional probabilities of the next bit given the context .
- The arithmetic coder uses these probabilities to encode or decode each bit of the input, and updates the model accordingly .
- DMC is an adaptive algorithm, meaning that it adjusts to the changing characteristics of the input data as it processes it .
- DMC can achieve high compression ratios for various types of data, especially those with regular patterns or long-range dependencies .
- DMC is also relatively simple and fast, compared to other adaptive arithmetic coding algorithms .
- However, DMC has some limitations, such as the memory requirement for storing the model, the lack of a termination criterion for the coding process, and the sensitivity to noise or errors in the input .