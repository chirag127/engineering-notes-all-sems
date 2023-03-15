### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of variable-length code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in applications that compress data, such as JPEG for images, MP3 for music, and Huffman coding for text .
- A prefix code can be represented by a binary tree, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- The length of a codeword is equal to the depth of the corresponding leaf node in the tree.
- The expected length of a prefix code is the weighted average of the codeword lengths, where the weights are the probabilities of the symbols.
- The optimal prefix code for a given probability distribution is the one that minimizes the expected length.
- One way to construct an optimal prefix code is to use Huffman's algorithm, which builds the tree from the bottom up by merging the two least probable symbols at each step.
- Another way to construct a prefix code is to use a universal code, which is a prefix code that works well for any monotonic probability distribution, without knowing the exact probabilities.
- Some examples of universal codes are Elias gamma code, Elias delta code, Fibonacci code, and Golomb code.