### Lossless image compression using Huffman coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding are:

  - Create a frequency table that counts the number of occurrences of each symbol in the image.
  - Sort the symbols in the frequency table in ascending order of frequency.
  - Build a binary tree by repeatedly merging the two least frequent symbols into a new node with a frequency equal to the sum of their frequencies. The merged symbols become the left and right children of the new node. Repeat this process until there is only one node left, which is the root of the tree.
  - Assign a code to each symbol by traversing the tree from the root to the leaf. Append a 0 to the code when moving to the left child and a 1 when moving to the right child. The code of a symbol is the sequence of bits along the path from the root to the leaf corresponding to that symbol.
  - Encode the image by replacing each symbol with its code.
  - Decode the image by traversing the tree from the root to the leaf according to the bits in the code.

- Huffman coding is optimal for a given source if the symbol probabilities are powers of two. Otherwise, it is near-optimal and achieves the Shannon entropy bound asymptotically as the number of symbols increases.
- Huffman coding is widely used in lossless image compression formats such as PNG, GIF, and TIFF. It can also be combined with other techniques such as run-length encoding, arithmetic coding, dictionary techniques, and predictive coding to improve the compression performance.