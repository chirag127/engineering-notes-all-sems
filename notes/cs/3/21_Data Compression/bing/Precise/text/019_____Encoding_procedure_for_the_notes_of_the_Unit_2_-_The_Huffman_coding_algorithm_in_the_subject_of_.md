### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. The Huffman coding algorithm is a lossless data compression algorithm that assigns variable-length codes to input symbols based on their frequencies of occurrence.
2. The first step in the Huffman coding algorithm is to create a frequency table that counts the number of occurrences of each symbol in the input data.
3. The next step is to build a binary tree, where each leaf node represents a symbol and its weight is the frequency of the symbol.
4. The tree is constructed by repeatedly merging the two nodes with the lowest weights until there is only one node left, which is the root of the tree.
5. The code for each symbol is obtained by traversing the tree from the root to the leaf node representing the symbol, with left branches adding a 0 to the code and right branches adding a 1.
6. The resulting codes are prefix-free, meaning that no code is a prefix of another code, which ensures that the encoded data can be uniquely decoded.
7. The Huffman coding algorithm is optimal in the sense that it produces the shortest possible average code length for a given set of symbol frequencies.
8. The algorithm can be implemented efficiently using a priority queue to keep track of the nodes with the lowest weights during the tree construction.
