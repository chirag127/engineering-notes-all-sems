### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. The Huffman coding algorithm is a lossless data compression algorithm that assigns variable-length codes to input symbols based on their frequencies.
2. The algorithm constructs a binary tree where the leaves represent the input symbols and the path from the root to a leaf represents the code for that symbol.
3. The tree is constructed in a bottom-up manner by merging the two least frequent symbols into a new internal node with a frequency equal to the sum of the two symbols' frequencies.
4. This process is repeated until there is only one node left, which is the root of the tree.
5. The codes for the symbols are obtained by traversing the tree from the root to the leaves and assigning a 0 to the left branch and a 1 to the right branch at each internal node.
6. The code for a symbol is the sequence of 0s and 1s obtained by following the path from the root to the leaf representing that symbol.
7. The Huffman coding algorithm guarantees that the code for a symbol with a higher frequency is shorter than the code for a symbol with a lower frequency, thus achieving data compression.
