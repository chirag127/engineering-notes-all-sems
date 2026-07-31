### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords back to the original source symbols.
- A code is non-singular if no two different source symbols have the same codeword.
- A code is instantaneous if the end of any codeword is recognizable without examining subsequent code symbols.
- A code is prefix-free if no codeword is a prefix of another codeword. Prefix-free codes are also instantaneous and uniquely decodable.
- A code is optimal if it minimizes the average codeword length for a given source distribution.
- The Kraft inequality is a necessary and sufficient condition for the existence of a prefix-free code with given codeword lengths. It states that for any prefix-free code with codeword lengths l1, l2, ..., ln and code symbols from an alphabet of size D, the following inequality holds:

  - Sum of D^(-li) from i = 1 to n <= 1

- The Kraft inequality can be extended to any uniquely decodable code by adding dummy code symbols to make it prefix-free.