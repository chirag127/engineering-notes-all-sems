 Here is the content in markdown format for the topic ### Arithmetic coding for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing:

### Arithmetic coding

- Arithmetic coding is a lossless data compression algorithm.
- It encodes the input data into a fractional number between 0 and 1.
- It divides the range of possible outputs into sub-ranges and assigns a sub-range to each symbol based on their probability of occurrence.
- The final output is the fractional part of the number that identifies the specific sub-range for the entire input sequence.
- It achieves a high compression ratio for sources that have a small alphabet and skewed distribution (ex: text).

Working:
- The range of outputs (0, 1) is divided into sub-ranges based on probability of symbols.
- Sub-range for the first symbol from input is selected based on the probability.
- The selected sub-range is further divided into sub-ranges for the next symbol and the process continues.
- This results in a fraction which is the final compressed output.

Example:

Input: 0 1 1 0
Probabilities: 0.4 0.3 0.2 0.1

 Initially, the range is (0, 1)
For 0, select range (0, 0.4)
For 1, select (0.3, 0.6)
For 1, select (0.5, 0.7)
For 0, select (0.6, 0.7)
Final output is 0.67 (0.6783)

Advantages:
- Achieves high compression.
- Simple and efficient implementation.
- Adaptive to changing input statistics.

Disadvantages:
- Complex decoding process.
- Slow compared to other algorithms like Huffman coding.
- Patent issues in the past.

Applications:
- Compressing text data.
- Medical imaging.
- Speech coding.
- JPEG image compression uses Arithmetic coding in its entropy encoding stage.