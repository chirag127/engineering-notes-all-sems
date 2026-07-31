### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies . The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized. The algorithm works as follows     :

- Create a leaf node for each character and assign it a weight equal to its frequency.
- Sort the nodes in ascending order of their weights.
- While there is more than one node in the list:
  - Remove the two nodes with the lowest weights from the list.
  - Create a new internal node with these two nodes as its children and the sum of their weights as its weight.
  - Insert the new node into the list in its sorted position.
  - Repeat until the list contains only one node, which is the root of the Huffman tree.
- Traverse the Huffman tree and assign a bit (0 or 1) to each edge, such that no two edges along any path have the same bit.
- For each character, concatenate the bits along the path from the root to the leaf node representing that character. This is the Huffman code for that character.

Here is an example of Huffman coding for the string "BANANA":

- The frequencies of the characters are: B: 1, A: 3, N: 2.
- The initial list of nodes is: [B: 1, N: 2, A: 3].
- The first iteration of the loop removes B and N and creates a new node with weight 3 and children B and N. The new list is: [[B, N]: 3, A: 3].
- The second iteration of the loop removes [B, N] and A and creates a new node with weight 6 and children [B, N] and A. The new list is: [[B, N], A]: 6].
- The loop ends and the root of the Huffman tree is [[B, N], A]: 6].
- The Huffman tree looks like this:

```
       [[B, N], A]: 6
       /          \
      /            \
     /              \
    /                \
[B, N]: 3            A: 3
 /    \              / \
B: 1  N: 2          0   1
/ \   / \
0   1 0   1
```

- The Huffman codes for the characters are: B: 00, N: 01, A: 1.
- The encoded string is: 001101011.