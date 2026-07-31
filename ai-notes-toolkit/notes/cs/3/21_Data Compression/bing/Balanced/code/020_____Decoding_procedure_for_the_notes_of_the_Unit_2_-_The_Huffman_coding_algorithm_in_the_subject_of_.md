### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol.
- Huffman coding is generally useful to compress the data in which there are frequently occurring characters.
- Huffman coding is an efficient method of compressing data without losing information.

The decoding procedure for the Huffman coding algorithm is as follows:

- Step 1: Construct a Huffman tree from the given frequency table of characters and their codes. The Huffman tree is a binary tree where each leaf node represents a character and its code, and each internal node represents the combined frequency of its children. The root node has the total frequency of all the characters.
- Step 2: Traverse the Huffman tree from the root node to the leaf node that corresponds to the first bit of the encoded message. If the bit is 0, move to the left child; if the bit is 1, move to the right child.
- Step 3: When a leaf node is reached, output the character that is stored in that node and return to the root node.
- Step 4: Repeat steps 2 and 3 until all the bits of the encoded message are processed.

Example:

Suppose the frequency table of characters and their codes is as follows:

| Character | Frequency | Code |
|-----------|-----------|------|
| a         | 5         | 0    |
| b         | 9         | 101  |
| c         | 12        | 100  |
| d         | 13        | 111  |
| e         | 16        | 1101 |
| f         | 45        | 1100 |

The Huffman tree for this table is:

```
        100
       /   \
      45   55
     / \   / \
    f  10 25  30
      / \ / \ / \
     a  b c d e  g
```

The encoded message is: 0110111010001001110111101100

The decoding procedure is:

- Start from the root node and read the first bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character f. Output f and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 30. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character e. Output e and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is an internal node with the frequency 25. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character c. Output c and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read the next bit of the encoded message: 0. Move to the left child.
- The left child is an internal node with the frequency 25. Read the next bit of the encoded message: 1. Move to the right child.
- The right child is a leaf node with the character b. Output b and return to the root node.
- Read the next bit of the encoded message: 0. Move to the left child.
- The left child is a leaf node with the character f. Output f and return to the root node.
- Read the next bit of the encoded message: 1. Move to the right child.
- The right child is an internal node with the frequency 55. Read