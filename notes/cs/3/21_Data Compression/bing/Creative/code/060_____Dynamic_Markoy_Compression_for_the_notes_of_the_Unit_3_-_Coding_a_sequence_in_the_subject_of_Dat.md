### Dynamic Markov Compression

- Dynamic Markov Compression (DMC) is a lossless data compression algorithm developed by Gordon Cormack and Nigel Horspool .
- It uses predictive arithmetic coding similar to prediction by partial matching (PPM), except that the input is predicted one bit at a time (rather than one byte at a time) .
- It builds a dynamic Markov model of the input data, which is a probabilistic model that captures the dependencies between successive bits  .
- The model consists of a binary tree of nodes, each representing a context of previous bits and storing the probabilities of the next bit being 0 or 1  .
- The model is initialized with a single node, the root, which has equal probabilities for both 0 and 1  .
- As the input is read, the model is updated by creating new nodes or adjusting the probabilities of existing nodes  .
- The model adapts to the changing characteristics of the input data, and can handle any type of data, including text, images, audio, etc.  .
- The arithmetic coder encodes each bit of the input based on the probabilities given by the model, and produces a compressed output that is close to the entropy of the input   .
- DMC is a simple and elegant algorithm that achieves high compression ratios, but it is also slow and memory-intensive, as it requires a large tree to store the model   .
- DMC can be improved by using techniques such as pruning, merging, splitting, or smoothing the nodes of the tree, or by using higher-order contexts or multiple models   .