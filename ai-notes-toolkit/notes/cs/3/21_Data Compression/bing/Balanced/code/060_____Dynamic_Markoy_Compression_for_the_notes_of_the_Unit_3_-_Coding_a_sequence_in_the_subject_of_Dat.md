### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits .
- The model consists of a tree of nodes, each representing a context or a history of previous bits. Each node has two counters, one for the number of zeros and one for the number of ones that have occurred in that context .
- The model is initialized with a single root node with zero counters. As each bit is read from the input, the model is updated by incrementing the corresponding counter of the current node, and creating a new child node if necessary .
- The model is used to predict the probability of the next bit, given the current context. This probability is then used to encode the bit using arithmetic coding .
- The model adapts to changes in the input data by pruning nodes that have low counts, and splitting nodes that have high counts. This ensures that the model is not too large or too complex, and that it reflects the most recent patterns in the data .
- DMC is an effective and efficient compression algorithm that can handle various types of data, such as text, images, audio, and binary files . It achieves compression ratios comparable to or better than other algorithms, such as PPM, LZW, and Huffman coding.