 Here is the content in markdown format for the given topic:

### Comparison of Binary and Huffman coding

Binary coding is the simplest form of coding where each symbol is represented by a fixed length binary codeword. For example, in ASCII coding, each character is represented by a 7-bit binary code.

Advantages:
- Simple to implement.
- Fixed length codewords enable easy synchronization.

Disadvantages:
- Inefficient if the symbols are not equally probable. Lengthy codewords are assigned to low probability symbols and short codewords to high probability symbols. This results in lower compression.

Huffman coding is an entropy encoding algorithm that produces a variable-length code based on the frequencies of symbols. Symbols with high frequencies are assigned shorter codewords and those with low frequencies are assigned longer codewords.

Advantages:
- Achieves higher compression than binary coding since it assigns codewords based on symbol probabilities.
- Simple to implement.

Disadvantages:
- Variable length codewords do not enable easy synchronization. Separate synchronization symbols are required to demarcate codeword boundaries.

Applications:
- Huffman coding is commonly used for data compression in file formats such as PNG and gzip.
- Binary coding is employed in ASCII and Unicode character encodings.

The choice between binary and Huffman coding depends on the application and compression requirements. If higher compression is desired and variable length codewords can be handled, Huffman coding is preferred. Otherwise, binary coding is used for its simplicity.

[Diagrams and examples can be added here for better understanding]