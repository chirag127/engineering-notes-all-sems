# Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which adapts to the changing statistics of the data as it is processed  .
- The Markov model consists of a tree of nodes, each representing a context of previous bits. Each node has two counters, one for the number of zeros and one for the number of ones that have occurred in that context  .
- The probability of the next bit being zero or one is estimated by the ratio of the corresponding counter to the total count in the current node  .
- The algorithm starts with a single node, the root, which has no context. As the input is read, new nodes are created and added to the tree as needed, to represent longer contexts  .
- The algorithm uses a threshold parameter to control the growth of the tree and the complexity of the model. If the total count in a node exceeds the threshold, the node is split into two child nodes, one for each possible next bit  .
- The algorithm also uses a halving parameter to prevent the counters from overflowing. If the total count in a node reaches a certain limit, the counters are halved and rounded up  .
- The algorithm achieves an excellent degree of data compression, comparable to or better than PPM, especially for highly structured or repetitive data.
- The algorithm is also fast and simple to implement, requiring only a small amount of memory.