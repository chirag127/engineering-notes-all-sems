### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  . It is a greedy algorithm that builds a binary tree of the input characters, where the most frequent characters are near the root and the least frequent characters are far from the root  . The codes are then derived from the paths of the characters in the tree, where left branches are assigned 0 and right branches are assigned 1  . The codes are prefix-free, meaning that no code is a prefix of another code .

The encoding procedure for the Huffman coding algorithm can be summarized as follows :

- Create a leaf node for each character and add it to the priority queue.
- While there is more than one node in the queue:
  - Remove the two nodes of the highest priority (the lowest frequency) from the queue.
  - Create a new internal node with these two nodes as children and with a frequency equal to the sum of the two nodes' frequencies.
  - Add the new node to the queue.
- The remaining node is the root node and the tree is complete.
- Traverse the tree and assign codes to each character. The code of a character is the sequence of 0s and 1s from the root to the leaf node of that character.

Here is an example of applying the Huffman coding algorithm to the string "BANANA":

- The frequencies of the characters are: B: 1, A: 3, N: 2.
- Create a leaf node for each character and add it to the priority queue: [B: 1, A: 3, N: 2].
- Remove the two nodes of the highest priority (the lowest frequency) from the queue and create a new internal node with them as children: [A: 3, N: 2, (B: 1, *: 1): 2], where * is a dummy character to indicate an internal node.
- Repeat the previous step until there is only one node left in the queue: [(A: 3, (N: 2, (B: 1, *: 1): 2): 4): 7], which is the root node of the tree.
- Traverse the tree and assign codes to each character: B: 110, A: 0, N: 10.
- The encoded string is: 0110100110.