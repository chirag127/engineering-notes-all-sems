 Here are the notes on Huffman coding for IMAGE COMPRESSION AND RECOGNITION:

### Huffman Coding

- Huffman coding is a lossless data compression algorithm.
- It uses variable-length binary codes to encode source symbols based on their probability of occurrence.
- More frequent symbols are assigned fewer bits, and less frequent symbols are assigned more bits.
- This results in an average code length that is shorter than the original average length, hence achieving compression.
- The Huffman code is prefix-free, meaning no codeword is a prefix of another codeword. This allows for efficient decoding as there is no ambiguity.
- To create Huffman codes:

1. Count the frequency of each symbol and store in a frequency table.
2. Create a leaf node for each symbol and add it to a min heap.
3. Repeatedly remove the two nodes with the smallest frequency from the heap.
4. Create a new internal node with these two nodes as children and with frequency equal to the sum of the two nodes.
5. Add the new node back to the heap.
6. Repeat steps 3-5 until there is only one node left in the heap. This is the root of the Huffman tree.
7. Assign binary codes to each symbol by traversing the Huffman tree in a depth-first manner and appending a 0 or 1 at each step.

- The time complexity to build a Huffman tree is O(nlogn) where n is the number of symbols.
- The space complexity is O(n) to store the frequency table and heap.
- Huffman coding is efficient when there are a small number of symbols with high probabilities and a large number of symbols with low probabilities.