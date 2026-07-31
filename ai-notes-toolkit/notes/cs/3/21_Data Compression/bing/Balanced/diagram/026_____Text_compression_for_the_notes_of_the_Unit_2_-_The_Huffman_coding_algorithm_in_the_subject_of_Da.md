### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters more efficiently.
- Text compression can save storage space, bandwidth, and transmission time.
- Text compression can be lossless or lossy. Lossless compression preserves the original information, while lossy compression discards some information to achieve higher compression ratios.
- The Huffman coding algorithm is a lossless compression method that assigns variable-length codes to the characters of a text file based on their frequencies.
- The Huffman coding algorithm works as follows:
  - Create a frequency table that counts the occurrences of each character in the text file.
  - Create a priority queue that stores each character and its frequency as a node, sorted by ascending frequency.
  - While the queue has more than one node, do the following:
    - Dequeue the two nodes with the lowest frequency and create a new node with the sum of their frequencies as its frequency and the two nodes as its left and right children.
    - Enqueue the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign a binary code to each character by appending 0 for left branches and 1 for right branches.
  - Encode the text file by replacing each character with its corresponding code.
  - Decode the text file by traversing the Huffman tree from the root to the leaves based on the bits of the code.