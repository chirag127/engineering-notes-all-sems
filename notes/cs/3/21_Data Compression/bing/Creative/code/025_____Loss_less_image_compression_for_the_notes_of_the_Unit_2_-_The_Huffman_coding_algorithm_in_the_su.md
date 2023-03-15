### Lossless image compression using Huffman coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequencies of occurrence.
- The basic steps of Huffman coding are:

  - Create a frequency table that counts the number of occurrences of each symbol in the image.
  - Sort the symbols in the frequency table in ascending order of frequency.
  - Build a binary tree by repeatedly merging the two least frequent symbols into a new node with a frequency equal to the sum of their frequencies. The merged symbols become the left and right children of the new node. Repeat this process until there is only one node left, which is the root of the tree.
  - Assign a binary code to each symbol by traversing the tree from the root to the leaf. Append a 0 to the code when moving to the left child and a 1 when moving to the right child.
  - Encode the image by replacing each symbol with its corresponding binary code.
  - Decode the image by traversing the tree from the root to the leaf according to the binary code and outputting the symbol at the leaf.

- Huffman coding is optimal for images that have a skewed distribution of symbols, meaning that some symbols are much more frequent than others.
- Huffman coding can achieve a compression ratio of up to 50% for grayscale images and up to 25% for color images.
- Huffman coding is simple, fast, and widely used in lossless compression standards such as JPEG, PNG, and ZIP.