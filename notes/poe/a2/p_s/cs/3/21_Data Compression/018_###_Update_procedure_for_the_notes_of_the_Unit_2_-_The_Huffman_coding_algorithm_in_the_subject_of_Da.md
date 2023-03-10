 Here is the content in markdown format for the given topic:

### Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression:

1. Huffman coding is a lossless data compression algorithm. It encodes the input symbols/characters into variable-length bit sequences based on the frequencies of the symbols.

2. The Huffman coding procedure involves two steps:

i) Building a Huffman Tree - The frequently occurring symbols are assigned shorter bit sequences and the rarely occurring symbols are assigned longer bit sequences. This is done by creating a binary tree called the Huffman Tree.

ii) Generating Huffman Codes - Huffman codes are generated based on the Huffman tree by traversing the Huffman tree from the root to the leaves and noting down the branch taken at each node. `0` is assigned to the left branch and `1` is assigned to the right branch. The Huffman code for a symbol is the sequence of 0s and 1s obtained by traversing the path from the root to the symbol's leaf.

3. The advantages of Huffman coding are:

- It is an optimal prefix-free code as it generates the minimum average codeword length.
- It adapts to the actual symbol frequencies in the input.
- It is a lossless compression technique.

4. The disadvantages of Huffman coding are:

- The encoding and decoding processes are complicated.
- The Huffman codes for input symbols have to be transmitted/stored along with the compressed data so that the receiver can decode the data. This overhead can be significant for small data sets.

5. Examples and applications of Huffman coding:

- Huffman coding is used in file compression utilities such as Gzip.
- It is used in compressing images in JPEG image compression standard.
- It is used in compressing audio in MP3 audio format.

[Detailed diagrams and examples can be included here if required.]