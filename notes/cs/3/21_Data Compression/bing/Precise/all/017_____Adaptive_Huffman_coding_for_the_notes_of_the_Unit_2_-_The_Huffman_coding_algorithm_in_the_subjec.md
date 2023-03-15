### Adaptive Huffman coding

Adaptive Huffman coding is a variant of the Huffman coding algorithm. It is used for data compression and is particularly useful when the distribution of the data being compressed is not known in advance. Here are some key points to note about Adaptive Huffman coding:

1. Adaptive Huffman coding builds the Huffman tree incrementally as the data is being compressed. This is in contrast to the standard Huffman coding algorithm, which requires the entire data set to be known in advance in order to build the Huffman tree.

2. The algorithm starts with an initial tree that contains only a single node, called the NYT (Not Yet Transmitted) node. As new symbols are encountered in the data, they are added to the tree as children of the NYT node.

3. The tree is updated dynamically as the data is being compressed. This is done by incrementally adjusting the frequencies of the nodes in the tree and performing tree rotations to maintain the Huffman tree property.

4. Adaptive Huffman coding can be used for both compression and decompression. During decompression, the tree is built in the same way as during compression, by incrementally adding new symbols to the tree as they are encountered in the compressed data.

5. One advantage of Adaptive Huffman coding is that it can adapt to changes in the distribution of the data being compressed. This makes it well-suited for compressing data with non-stationary distributions.

6. Another advantage of Adaptive Huffman coding is that it does not require the transmission of the Huffman tree along with the compressed data. This can result in additional space savings, particularly when compressing small amounts of data.

Overall, Adaptive Huffman coding is a powerful and flexible algorithm for data compression that can adapt to changes in the distribution of the data being compressed. It is particularly useful when the distribution of the data is not known in advance.