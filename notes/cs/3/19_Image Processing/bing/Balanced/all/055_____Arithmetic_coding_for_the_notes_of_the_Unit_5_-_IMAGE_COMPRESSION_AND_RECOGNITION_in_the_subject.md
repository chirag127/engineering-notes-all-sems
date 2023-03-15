# Arithmetic coding for image compression

Arithmetic coding is a lossless compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence. Unlike Huffman coding, which assigns codes to individual symbols, arithmetic coding encodes the entire message into a single fraction between 0 and 1.

The main steps of arithmetic coding are:

- Define a probability model for the source symbols. This can be static (fixed for the entire message) or adaptive (updated after each symbol).
- Initialize an interval [low, high) to [0, 1).
- For each symbol in the message, do the following:
  - Divide the interval into subintervals proportional to the symbol probabilities.
  - Narrow the interval to the subinterval corresponding to the current symbol.
  - If the interval becomes too small, output some bits and rescale the interval.
- Output the final interval as the code for the message.

Arithmetic coding can be applied to image compression by encoding the pixels or the coefficients of a transform (such as DCT) of the image. The probability model can be based on the pixel values, the neighboring pixels, or the previous coefficients. The advantage of arithmetic coding is that it can achieve near-optimal compression ratios, especially for skewed or small alphabets. The disadvantage is that it is more complex and slower than Huffman coding, and it is more sensitive to errors or loss of synchronization.