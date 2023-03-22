 Here is the formal content in markdown format without any emojis or external links:

### Modeling and coding for the notes of the Unit 1 - Compression Techniques

1. Data compression is the process of encoding data in such a way that it takes fewer bits to represent the information. It reduces the amount of space data occupies on a storage medium or the amount of time it takes to transmit data over a network connection.
2. Lossless compression: The original data can be perfectly reconstructed from the compressed data. The compression ratio is relatively low. Example: ZIP file format.
3. Lossy compression: The original data cannot be perfectly reconstructed from the compressed data. Some amount of information is lost, but the lost information is negligible. The compression ratio is relatively high. Example: JPEG image format.
4. Entropy coding: Assigns variable-length codes to input characters/symbols based on their probability of occurrence. More frequent characters are assigned fewer bits. It achieves near-optimal compression. Examples: Huffman coding, arithmetic coding.
5. Dictionary coding: Maintains a dictionary (list) of frequently used strings/phrases and assigns variable-length codes to them. The decoder needs to have the same dictionary to decode the message. Example: LZW algorithm.
6. Prediction: Tries to predict the next symbol/pixel based on previous symbols/pixels and encodes only the difference (residual) from the predicted value. Example: DPCM.
7. Transform coding: Applies a mathematical transform to the data which concentrates the information into fewer coefficients. These coefficients are then quantized and entropy encoded. Example: JPEG uses Discrete Cosine Transform (DCT).

The points are written in a formal tone without any emojis or external links as instructed. Let me know if you would like me to modify or add any other points.