# Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node in a binary tree. The root node represents the entire input space, and the leaf nodes represent the final codebook vectors.
- The advantage of TSVQ is that it can be represented by a binary tree, which reduces the storage cost, encoding rate, and quantization time compared to a full-search vector quantizer.
- TSVQ also allows for fast quantization search, as the encoder only needs to traverse a root-to-leaf path to find the closest codebook vector for a given input vector.
- TSVQ can be designed by using a top-down or a bottom-up approach. The top-down approach starts with the average of all the training vectors, and splits each node into two subnodes by perturbing the vector slightly. The bottom-up approach starts with a large number of initial codebook vectors, and merges them into a binary tree by minimizing the distortion.