### Adaptive Huffman coding

Adaptive Huffman coding, also known as Dynamic Huffman coding, is an adaptive coding technique based on Huffman coding. It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution, that allows one-pass encoding and adaptation to changing conditions in data .

- It is a near-minimal variable-length character coding that changes based on the frequency of characters processed. As characters are processed, frequencies are updated and codes are changed (or, the coding tree is modified) .

- The implementation is done using Vitter Algorithm. For example, when encoding a string containing alphabets, let m be the total number of alphabets (m = 26). For Vitter Algorithm, find parameters e & r such that .

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes based on the frequencies of input characters. In order to determine what code to assign to each character, a binary tree is built that will organize the characters based on frequency .