# Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using only two symbols, usually 0 and 1. Each symbol is called a bit, and a sequence of bits is called a binary code. Binary coding is used to store and transmit data in computers and digital devices.
- Huffman coding is a form of lossless compression which makes files smaller using the frequency with which characters appear in a message. Huffman coding assigns variable length binary codes for each input character in the text file. The length of the binary code depends on the frequency of the character in the file. The most frequent characters are coded with the smaller binary words, thus, the size used to code them is minimal, which increases the compression.
- The main difference between binary and Huffman coding is that binary coding uses fixed length codes for all characters, while Huffman coding uses variable length codes for different characters. Binary coding is simpler and faster, but Huffman coding is more efficient and reduces the file size more.
- Some advantages of Huffman coding over binary coding are:
  - Huffman coding can achieve a compression ratio of more than 50%, which means that the compressed file is less than half the size of the original file .
  - Huffman coding is optimal, which means that no other prefix code can achieve a better compression for the same input.
  - Huffman coding is adaptive, which means that it can adjust to the changing frequencies of the characters in the input.
- Some disadvantages of Huffman coding compared to binary coding are:
  - Huffman coding requires more computation and memory to construct and store the Huffman tree, which is a data structure that represents the codes for each character.
  - Huffman coding requires an extra header to store the Huffman tree or the code table, which adds some overhead to the compressed file.
  - Huffman coding is not suitable for compressing files that have a uniform distribution of characters, as the compression ratio will be low or even negative.