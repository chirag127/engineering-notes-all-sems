# Lossless Image Compression Using Huffman Coding

- Lossless image compression is a technique that reduces the size of an image file without affecting its quality or information content.
- Huffman coding is a lossless data compression algorithm that assigns variable-length binary codes to the symbols (pixels) in an image based on their frequency of occurrence.
- The basic steps of Huffman coding for image compression are:

  - Step 1: Calculate the probability of each pixel value in the image and sort them in descending order.
  - Step 2: Create a binary tree with the pixel values as leaf nodes and their probabilities as weights. The two nodes with the lowest probabilities are combined to form a parent node with the sum of their probabilities as the weight. This process is repeated until there is only one root node left.
  - Step 3: Assign a binary code to each leaf node by traversing the tree from the root to the leaves. The code is formed by appending a 0 for a left branch and a 1 for a right branch.
  - Step 4: Encode the image by replacing each pixel value with its corresponding binary code. The encoded image is stored along with the Huffman tree for decoding.
  - Step 5: Decode the image by using the Huffman tree to map each binary code back to its pixel value.

- Huffman coding is an optimal and efficient lossless compression technique that achieves the Shannon bound, which is the theoretical limit of compression for a given source.
- Huffman coding can be applied to grayscale or color images, but it is more effective for images with a small number of distinct pixel values or a skewed distribution of pixel values.