## Unit 2 - The Huffman coding algorithm

The Huffman coding algorithm is a lossless data compression algorithm that was developed by David A. Huffman in 1952. It is a variable-length coding algorithm that assigns shorter codes to more frequently occurring characters and longer codes to less frequently occurring characters.

The steps involved in the Huffman coding algorithm are as follows:

1. Create a frequency table for each character in the input data.
2. Create a priority queue and insert each character and its frequency as a node in the queue.
3. While the queue has more than one node, extract the two nodes with the lowest frequency and create a new internal node with these two nodes as children. The frequency of the new node is the sum of the frequencies of the two extracted nodes. Insert the new node into the queue.
4. The remaining node in the queue is the root of the Huffman tree.
5. Assign codes to the characters by traversing the tree from the root to the leaves. The code for a character is the sequence of 0s and 1s along the path from the root to the leaf representing the character.

The Huffman coding algorithm is widely used in data compression applications such as file compression and image compression. It is also used in the construction of optimal prefix codes. The algorithm has a time complexity of O(nlogn) where n is the number of unique characters in the input data.