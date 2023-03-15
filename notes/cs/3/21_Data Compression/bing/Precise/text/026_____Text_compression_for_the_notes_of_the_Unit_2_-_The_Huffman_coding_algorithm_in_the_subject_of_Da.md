### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Text compression is the process of reducing the size of a text file by encoding its content in a more efficient manner.
2. Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies.
3. The most frequent characters are assigned the shortest codes, while the least frequent characters are assigned the longest codes.
4. Huffman coding is an optimal prefix code, meaning that no code is a prefix of another code.
5. The Huffman coding algorithm involves building a binary tree where the leaves represent the input characters and their frequencies.
6. The tree is built from the bottom up, by merging the two nodes with the lowest frequencies until there is only one node left, which represents the root of the tree.
7. The codes are then assigned by traversing the tree from the root to the leaves, assigning a 0 to the left branch and a 1 to the right branch at each step.
8. Huffman coding is widely used in data compression, including in file formats such as ZIP and GZIP.