### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  `sum_{i=1}^n 2^{-l_i} <= 1`

- The Kraft inequality can be generalized to any code alphabet with size r, where r is the number of code symbols. In that case, the inequality becomes:

  `sum_{i=1}^n r^{-l_i} <= 1`

- The Kraft inequality can also be used to prove the existence of a uniquely decodable code with given codeword lengths, but not necessarily prefix-free. However, such a code may not be instantaneous.