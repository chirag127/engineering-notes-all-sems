### Adaptive Huffman coding

- Adaptive Huffman coding, also known as Dynamic Huffman coding, is an adaptive coding technique based on Huffman coding.
- It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution.
- This allows for one-pass encoding and adaptation to changing conditions in data.
- As characters are processed, frequencies are updated and codes are changed, or the coding tree is modified.
- The implementation of Adaptive Huffman coding is done using the Vitter Algorithm.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes based on the frequencies of input characters.
- A binary tree is built to organize characters based on frequency in order to determine what code to assign to each character.