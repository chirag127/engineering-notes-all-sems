### Structured Vector Quantizers

- Structured vector quantizers are a class of vector quantizers that impose some constraints on the codebook or the partition of the input space to reduce the complexity and the storage requirements of the quantizer .
- Structured vector quantizers can be classified into two types: tree-structured vector quantizers and lattice vector quantizers.
- Tree-structured vector quantizers (TSVQ) use a hierarchical partition of the input space, such that each node of the tree corresponds to a region and a codeword . The encoding and decoding processes are performed by traversing the tree from the root to a leaf node, which reduces the search complexity from linear to logarithmic in the codebook size.
- Lattice vector quantizers use a regular geometric structure of the codebook, such as a lattice, to generate the codewords algorithmically rather than storing them in a table . The encoding and decoding processes are performed by using fast algorithms that exploit the symmetry and the structure of the lattice.

### Advantages of Vector Quantization over Scalar Quantization

- Vector quantization can achieve better rate-distortion performance than scalar quantization, since it exploits the correlation and the structure of the input vectors .
- Vector quantization can avoid the granular noise and the contouring artifacts that are common in scalar quantization, especially at low bit rates.
- Vector quantization can adapt to the statistics and the characteristics of the input source, by using variable-length codes, variable-rate codes, or variable-dimension codes.