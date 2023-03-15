### Uniquely Decodable Codes

- A code is a mapping from a set of source symbols to a set of codewords, which are sequences of code symbols.
- A code is uniquely decodable if there is only one way to decode any sequence of codewords, i.e., no ambiguity in the decoding process.
- A code is non-singular if no two distinct source symbols have the same codeword.
- A non-singular code is not necessarily uniquely decodable, as there may be more than one way to partition a sequence of codewords into individual codewords.
- For example, the code M2 = {a -> 0, b -> 01, c -> 011} is non-singular, but not uniquely decodable, as the sequence 0110 can be decoded as either ab or ca.
- A code is prefix-free or instantaneous if no codeword is a prefix of another codeword, i.e., no codeword can be extended by adding more code symbols to form another codeword.
- A prefix-free code is always uniquely decodable, as the end of any codeword is recognizable without examining subsequent code symbols.
- For example, the code M3 = {a -> 0, b -> 01, c -> 011} is prefix-free and uniquely decodable.
- A uniquely decodable code is not necessarily prefix-free, as there may be codewords that are suffixes of other codewords, i.e., no codeword can be shortened by removing code symbols from the beginning to form another codeword.
- For example, the code M4 = {a -> 0, b -> 10, c -> 110} is uniquely decodable, but not prefix-free, as c is a suffix of b.
- A code is optimal if it minimizes the average codeword length for a given source distribution, i.e., it achieves the lowest possible redundancy or the highest possible compression ratio.
- A code is optimal if and only if it satisfies the Kraft inequality, which states that for any uniquely decodable code with codewords of lengths l1, l2, ..., ln, the following inequality holds:

  ![Kraft inequality](https://latex.codecogs.com/png.latex?%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20r%5E%7B-l_i%7D%20%5Cleq%201)

  where r is the size of the code alphabet.
- The Kraft inequality provides a necessary and sufficient condition for the existence of a uniquely decodable code with given codeword lengths, but it does not guarantee that such a code is optimal or prefix-free.
- To construct an optimal prefix-free code, one can use algorithms such as Huffman coding or arithmetic coding, which are based on the source probabilities and the code alphabet size.