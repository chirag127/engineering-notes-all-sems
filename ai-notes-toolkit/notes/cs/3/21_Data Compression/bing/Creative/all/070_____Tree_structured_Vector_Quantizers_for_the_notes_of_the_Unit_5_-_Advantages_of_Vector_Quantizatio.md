# Tree structured Vector Quantizers

- Tree structured vector quantization (TSVQ) is a technique that reduces the complexity of vector quantization by imposing a hierarchical structure on the partitioning of the input space .
- In TSVQ, the input space is divided into a hierarchy of regions, each corresponding to a node of a binary tree .
- The root node represents the entire input space, and the leaf nodes represent the final codebook vectors .
- The advantage of TSVQ is that it can be represented and stored efficiently using a binary tree, and the quantization process can be performed fast by traversing the tree from the root to the leaf that matches the input vector .
- TSVQ can be designed to minimize the expected distortion subject to different cost functions, such as storage cost, encoding rate, or quantization time.
- TSVQ can also be adapted to non-stationary sources by using dynamic splitting and pruning algorithms.

## Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of input vectors using a smaller set of codebook vectors .
- Scalar quantization (SQ) is a special case of VQ where the input and codebook vectors are one-dimensional .
- VQ has several advantages over SQ, such as :
  - VQ can exploit the correlation among the components of the input vectors, while SQ treats each component independently.
  - VQ can achieve lower distortion than SQ for the same number of bits per vector, or equivalently, lower bit rate than SQ for the same distortion level.
  - VQ can handle multidimensional data more naturally and efficiently than SQ, which requires vectorization and devectorization operations.
  - VQ can adapt to the statistics of the input data more easily than SQ, which requires uniform quantization or non-uniform quantization with fixed parameters.