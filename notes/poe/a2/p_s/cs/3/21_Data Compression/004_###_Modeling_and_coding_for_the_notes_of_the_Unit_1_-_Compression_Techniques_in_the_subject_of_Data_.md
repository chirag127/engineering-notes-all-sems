 Here is the content in markdown format for the given topic:

### Modeling and coding for the notes of the Unit 1 - Compression Techniques

1. Prediction by Partial Matching (PPM):
- It is a statistical data compression technique.
- It scans the input data and makes predictions about the next symbol in the input.
- It maintains a list of symbols and their probabilities.
- The most probable symbol is encoded and the model is updated.
- This continues until the end of input.
- It gives better compression than Huffman coding for large files.
- Disadvantage: Complex and slower than Huffman coding.

2. Arithmetic coding:
- It is a form of entropy encoding that encodes a message into a fractional value within a given range.
- It uses the probabilities of symbols to allocate portions of the range to symbols.
- As each symbol is encoded, the range is narrowed down to the portion allocated to the encoded symbol.
- This continues until the end of the input.
- The final range represents the compressed message.
- It usually compresses better than Huffman coding.
- Disadvantage: Complex and slower than Huffman coding.

[Detailed explanations, examples, diagrams, etc. can be included here for better understanding.]

Advantages of data compression:
- Reduces storage space.
- Decreases transmission time.
- Optimizes the use of storage and bandwidth resources.

Applications of data compression:
- Multimedia (audio, video, images).
- Text and document files.
- Executable files.
- Archival and backup systems.
- Communication applications.

[More details and points can be included for the advantages and applications based on the requirements.]