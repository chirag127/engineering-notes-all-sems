### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on the Huffman coding algorithm, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data.  

Some advantages of adaptive Huffman coding are:

- It can handle any source distribution, even if it is unknown or non-stationary (i.e., changing over time).
- It can achieve near-optimal compression, since the code is always updated to reflect the current frequencies of the symbols.
- It can encode and decode the data in one pass, without requiring any extra storage or communication for the code.

Some disadvantages of adaptive Huffman coding are:

- It requires more computation than Huffman coding, since the code tree has to be modified frequently.
- It may not be suitable for sources with very low entropy (i.e., high predictability), since the code tree may become unbalanced and inefficient.
- It may not be compatible with some applications that require fixed-length codes or random access to the data.

There are different algorithms for implementing adaptive Huffman coding, such as the FGK algorithm and the Vitter algorithm. These algorithms differ in how they update the code tree and how they handle new symbols that have not been seen before.  

The following diagram shows an example of adaptive Huffman coding using the Vitter algorithm for the string "ABRACADABRA". The algorithm starts with an empty code tree and a special symbol NYT (Not Yet Transmitted) that represents all unseen symbols. As each symbol is encoded, the algorithm updates the code tree by incrementing the frequencies of the nodes, swapping nodes to maintain the sibling property (i.e., nodes with the same frequency are ordered by decreasing weight), and splitting the NYT node into two new nodes for the new symbol and a new NYT node. The algorithm also outputs the code for each symbol, which is obtained by traversing the code tree from the root to the leaf. The code for a new symbol is the code for the NYT node followed by the binary representation of the symbol.

![Adaptive Huffman coding example](https://i.imgur.com/9cQ6y8N.png)

The final code for the string "ABRACADABRA" is:

```
A: 0000
B: 0001
R: 001
C: 0100
D: 0101
```

The total number of bits is 40, which is less than the 44 bits required by the static Huffman code for the same string. 

: https://en.wikipedia.org/wiki/Adaptive_Huffman_coding
: https://xlinux.nist.gov/dads/HTML/adaptiveHuffman.html
: https://www.geeksforgeeks.org/adaptive-huffman-coding-and-decoding/
: http://ben-tanen.com/adaptive-huffman/