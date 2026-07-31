### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords, i.e., no ambiguity in the decoding process.
- A code is non-singular if no two distinct source symbols have the same codeword.
- A non-singular code is not necessarily uniquely decodable, as the following example shows:

  - Let the source symbols be {a, b, c, d} and the codewords be {0, 01, 011, 111}.
  - This code is non-singular, but not uniquely decodable, because the sequence 0111 can be decoded as either ab or cd.

- A code is called an instantaneous code if the end of any codeword is recognizable without examining subsequent code symbols.
- The instantaneous codes have the property that no codeword is a prefix of another codeword. For this reason, prefix-free codes are sometimes known as instantaneous codes.
- Every instantaneous code is uniquely decodable, but not vice versa, as the following example shows:

  - Let the source symbols be {a, b, c, d} and the codewords be {0, 10, 110, 111}.
  - This code is uniquely decodable, but not instantaneous, because 0 is a prefix of 10, and 110 is a prefix of 111.

- A code is called an optimal code if it minimizes the average codeword length for a given source distribution, i.e., it achieves the lowest possible redundancy.
- The Kraft inequality is a necessary and sufficient condition for the existence of an instantaneous code with given codeword lengths.
- The Kraft inequality states that for any instantaneous code with codeword lengths l1, l2, ..., ln, the following inequality holds:

  - Summation from i=1 to n of 2^(-li) <= 1

- The Kraft inequality can also be used to test whether a given code is uniquely decodable, by using the extended codeword lengths, which are the lengths of the codewords after appending a special delimiter symbol to each codeword.