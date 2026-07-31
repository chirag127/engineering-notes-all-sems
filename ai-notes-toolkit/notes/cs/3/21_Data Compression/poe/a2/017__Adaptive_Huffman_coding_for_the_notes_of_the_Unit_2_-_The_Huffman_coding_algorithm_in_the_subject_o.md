 Here is the content in markdown format without any emojis or external links:

### Adaptive Huffman coding for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression.

- Huffman coding is a lossless data compression algorithm. It encodes the input symbols/characters into binary codes based on their occurrence frequency.
- The more frequent symbols are assigned shorter binary codes and less frequent symbols are assigned longer binary codes.
- This results in an average code length that is shorter than the original input and hence achieves compression.
- The Huffman coding algorithm has two passes:

1. First pass: The frequency of occurrence of each symbol is calculated.
2. Second pass: A binary tree is constructed based on the frequency counts. The symbols are assigned binary codes based on the path from the root to the symbol leaf node.

- The Huffman coding algorithm works well if the input data frequencies are relatively static. But if the input data frequencies change over time, the compression efficiency decreases.
- To handle this, Adaptive Huffman Coding is used. In this, the frequency table is updated dynamically after every input and the Huffman tree is reconstructed based on the updated frequencies.
- This enables achieving better compression as it adapts to the changing input data frequencies. The overhead of reconstructing the tree can be minimized by only updating the frequencies of symbols whose frequencies have changed and updating the Huffman tree only for the path from the root to the symbol whose frequency has changed.
- Adaptive Huffman Coding gives better compression as compared to the basic Huffman Coding for inputs with varying frequencies.

The content summarizes the key points about Adaptive Huffman Coding. Let me know if you would like me to elaborate on any of the points or modify the content in any way.