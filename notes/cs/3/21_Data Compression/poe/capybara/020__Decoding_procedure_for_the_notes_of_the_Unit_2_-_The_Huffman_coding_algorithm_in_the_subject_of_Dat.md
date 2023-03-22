### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

When it comes to decoding the Huffman coded message, the following steps need to be followed:

1. To begin with, we need to start from the root node of the Huffman tree.
2. For every bit in the encoded message, we need to traverse the tree as per the bit value. For instance, if the bit is 0, we move towards the left subtree, and if the bit is 1, we move towards the right subtree.
3. We need to keep traversing the tree until we reach the leaf node. The leaf node represents a unique symbol in the original message.
4. Once we reach the leaf node, we have successfully decoded a symbol from the encoded message.
5. We repeat the above steps until we have decoded the entire message.

It is important to note that the decoding process requires the Huffman tree to be rebuilt using the same frequency table used to build the original tree. This is because the frequency table contains information about the unique symbols present in the original message, which is required to decode the message.

In conclusion, decoding a Huffman coded message involves traversing the Huffman tree and decoding each symbol until the entire message is decoded. With a clear understanding of the decoding procedure, one can effectively compress and decompress messages using the Huffman coding algorithm.