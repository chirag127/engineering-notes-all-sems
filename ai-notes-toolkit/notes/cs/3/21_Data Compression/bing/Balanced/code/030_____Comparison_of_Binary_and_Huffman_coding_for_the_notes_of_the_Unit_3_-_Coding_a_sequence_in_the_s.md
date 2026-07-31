```
### Comparison of Binary and Huffman coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Binary coding is a method of representing data using fixed-length binary words, where each character or symbol is assigned a unique binary code. For example, the ASCII code uses 8 bits to represent 256 characters.
- Huffman coding is a method of representing data using variable-length binary words, where each character or symbol is assigned a binary code based on its frequency of occurrence in the data. For example, the most frequent character may be assigned a single bit, while the least frequent character may be assigned a longer bit sequence.
- The main advantage of Huffman coding over binary coding is that it can achieve higher compression ratios, as it uses fewer bits to represent more frequent characters and symbols. This reduces the size of the data and saves storage space and bandwidth.
- The main disadvantage of Huffman coding over binary coding is that it requires an extra step of generating and storing the Huffman tree, which is a binary tree that shows the binary codes for each character or symbol. This adds some complexity and overhead to the compression and decompression process.
- Another disadvantage of Huffman coding is that it is not suitable for compressing data that has a uniform distribution of characters or symbols, as it will not reduce the number of bits needed to represent them. In such cases, binary coding may be more efficient or equivalent.
- A comparison of binary and Huffman coding for a sample text is shown below:

| Text | Binary coding | Huffman coding |
|------|---------------|----------------|
| A    | 01000001      | 0              |
| B    | 01000010      | 100            |
| C    | 01000011      | 101            |
| D    | 01000100      | 1110           |
| E    | 01000101      | 1111           |
| F    | 01000110      | 110            |

- Assume that the frequency of the characters in the text is as follows: A (50%), B (12.5%), C (12.5%), D (6.25%), E (6.25%), F (12.5%).
- The Huffman tree for this text is shown below:

```
     / \
    /   \
   /     \
  /       \
 /         \
0          1
|          |
A        / \
       /   \
      /     \
     /       \
    /         \
   1          0
  / \        / \
 /   \      /   \
1    0     1     0
|    |     |     |
E    D     C     B
```

- The total number of bits needed to represent the text using binary coding is 6 x 8 = 48 bits.
- The total number of bits needed to represent the text using Huffman coding is 6 x (0.5 x 1 + 0.125 x 3 + 0.0625 x 4) = 18 bits.
- The compression ratio achieved by Huffman coding over binary coding is 48 / 18 = 2.67, which means that Huffman coding reduces the size of the data by more than 50%.
```