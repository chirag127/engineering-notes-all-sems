# Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters in a more efficient way.
- Text compression can save storage space, bandwidth, and transmission time, and can also improve security and privacy by making the text less readable by humans or machines.
- Text compression can be lossless or lossy. Lossless compression preserves the original information and allows exact reconstruction of the text, while lossy compression discards some information and only allows approximate reconstruction of the text.
- One of the most popular and widely used lossless text compression algorithms is the Huffman coding algorithm, named after its inventor David Huffman.
- The Huffman coding algorithm assigns variable-length binary codes to the characters of a text based on their frequencies of occurrence. The more frequent a character is, the shorter its code will be, and vice versa. This way, the most common characters will take up less space than the less common ones, resulting in a smaller file size.
- The Huffman coding algorithm consists of the following steps:

  1. Create a frequency table that counts the number of occurrences of each character in the text.
  2. Create a priority queue (or a min-heap) that contains the characters as nodes, sorted by their frequencies in ascending order.
  3. While the queue has more than one node, do the following:
     - Dequeue the two nodes with the lowest frequencies and create a new internal node with the sum of their frequencies as its frequency.
     - Assign the left child of the new node to be the first dequeued node and the right child to be the second dequeued node.
     - Enqueue the new node back to the queue.
  4. The remaining node in the queue is the root of the Huffman tree, which represents the optimal prefix-free code for the text.
  5. Traverse the Huffman tree and assign a 0 to every left edge and a 1 to every right edge. The code for each character is the concatenation of the edge labels along the path from the root to the leaf node corresponding to that character.
  6. Encode the text by replacing each character with its code and output the compressed file.
  7. To decode the compressed file, use the Huffman tree to convert each code back to its original character and output the decompressed file.