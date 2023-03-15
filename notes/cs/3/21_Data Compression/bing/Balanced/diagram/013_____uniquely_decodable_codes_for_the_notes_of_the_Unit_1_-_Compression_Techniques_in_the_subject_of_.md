### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  ![Kraft inequality](https://latex.codecogs.com/png.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20D%5E%7B-l_i%7D%20%5Cleq%201)

  where D is the size of the code alphabet.

- The Kraft inequality can be extended to any uniquely decodable code, not just prefix-free codes, by using the McMillan theorem, which states that for any uniquely decodable code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  ![McMillan theorem](https://latex.codecogs.com/png.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20D%5E%7B-l_i%7D%20%5Cleq%201)

  where D is the size of the code alphabet.

- The Kraft inequality and the McMillan theorem can be used to prove the optimality of certain codes, such as Huffman codes and Shannon-Fano codes, which are based on the source probabilities and the code alphabet size.

- Uniquely decodable codes are useful for data compression, as they allow the receiver to recover the original data without ambiguity or error. They also have applications in cryptography, error correction, and information theory.