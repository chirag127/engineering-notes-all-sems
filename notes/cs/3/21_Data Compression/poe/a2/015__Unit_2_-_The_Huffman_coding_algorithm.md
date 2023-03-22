 Here is the formal content on the topic "Unit 2 - The Huffman coding algorithm" in markdown format without any emojis or external links:

## Unit 2 - The Huffman coding algorithm.

1. Huffman coding is a lossless data compression algorithm. It encodes the characters/symbols occurring in the given text into shorter binary codes based on their frequency of occurrence.
2. The most frequent character gets the smallest code and the least frequent character gets the longest code. This results in an average code length that is shorter than the original length.
3. The algorithm uses a binary tree (called Huffman tree) for encoding the characters. Each node of the tree contains a character and its frequency. The two nodes with the smallest frequencies are selected and a new node is created with these two nodes as children and with a frequency equal to the sum of the two nodes. This process is repeated until there is only one node left - the root node.
4. The Huffman codes are derived from the Huffman tree by traversing down from the root to the leaves and assigning 0 or 1 based on the direction (left or right respectively). The path thus spells out the code for the character.
5. The Huffman encoding proves optimal if the symbols are encoded based on their probability of occurrence. It leads to compression and is lossless as the original text can be recovered from the compressed text. It is useful in compressing datasets with skewed symbol distribution.