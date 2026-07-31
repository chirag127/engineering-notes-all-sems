# Text Compression: Unit 2 - The Huffman Coding Algorithm

Huffman coding is a lossless data compression algorithm that is used to compress text data. It is based on the idea of assigning shorter codes to more frequently occurring characters and longer codes to less frequently occurring characters. Here are the key points to remember about Huffman coding:

1. Huffman coding is a **greedy algorithm** that constructs an optimal prefix code called a Huffman code.
2. The algorithm uses a **priority queue** to store the characters and their frequencies, with the characters with the lowest frequencies having the highest priority.
3. The algorithm **merges** the two characters with the lowest frequencies into a single node with a frequency equal to the sum of their frequencies. This process is repeated until there is only one node left in the priority queue, which represents the root of the Huffman tree.
4. The **Huffman code** for each character is obtained by traversing the Huffman tree from the root to the leaf node representing the character, with left branches corresponding to 0 and right branches corresponding to 1.
5. Huffman coding is an **entropy encoding** technique, which means that it is optimal for compressing data with known probability distribution.
6. Huffman coding is widely used in **data compression** applications such as file compression and transmission of data over a network.