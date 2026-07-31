# Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using only two symbols, usually 0 and 1. Each symbol is called a bit, and a sequence of bits is called a binary code. Binary coding is used to store and transmit data in computers and other digital devices.
- Huffman coding is a form of lossless compression which makes files smaller using the frequency with which characters appear in a message. Huffman coding assigns variable length binary codes for each input character in the text file. The length of the binary code depends on the frequency of the character in the file. The most frequent characters are coded with the smaller binary words, thus, the size used to code them is minimal, which increases the compression.
- The main difference between binary and Huffman coding is that binary coding uses fixed length codes for all characters, while Huffman coding uses variable length codes for different characters. Binary coding is simpler and faster, but Huffman coding is more efficient and reduces the file size more.
- The advantages of Huffman coding over binary coding are:
  - Huffman coding achieves optimal compression, meaning that no other lossless compression method can produce a smaller output for the same input.
  - Huffman coding adapts to the data, meaning that it can compress any type of file, regardless of the distribution of characters in the file.
  - Huffman coding is easy to implement and decode, using a binary tree data structure that represents the codes for each character.
- The disadvantages of Huffman coding over binary coding are:
  - Huffman coding requires extra space to store the code table, which maps each character to its corresponding binary code. This code table has to be transmitted or stored along with the compressed file, which adds some overhead.
  - Huffman coding is slower than binary coding, as it involves sorting the characters by frequency and building the binary tree. It also requires more memory and processing power to encode and decode the variable length codes.