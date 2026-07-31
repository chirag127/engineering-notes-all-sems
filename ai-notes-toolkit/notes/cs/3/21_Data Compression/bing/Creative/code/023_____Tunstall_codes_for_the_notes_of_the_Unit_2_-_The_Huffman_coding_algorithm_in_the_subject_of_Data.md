### Tunstall codes

- Tunstall codes are a form of entropy coding used for lossless data compression .
- Tunstall codes are based on the idea of parsing a stochastic source with codewords of variable length, and then encoding each codeword with a fixed-length code .
- Tunstall codes are a precursor to Lempel–Ziv codes, which are widely used in practice.
- Tunstall codes have the following properties :
  - They are prefix codes, meaning that no codeword is a prefix of another codeword.
  - They are optimal for sources that have a geometric distribution of probabilities, such as run-length encoding.
  - They have a fixed compression ratio, which is equal to the ratio of the source entropy to the codeword length.
  - They are easy to construct and decode, using a tree structure and a table lookup.
- Tunstall codes can be constructed as follows :
  - Start with a set of symbols, each with a probability of occurrence.
  - Assign each symbol a codeword of the same length, such as a binary digit.
  - Expand the set of codewords by appending each symbol to each existing codeword, and update the probabilities accordingly.
  - Repeat the expansion until the desired codeword length is reached, or until all possible codewords are exhausted.
  - Prune the tree of codewords by removing any unused or incomplete codewords, and assign a fixed code to each remaining codeword.
- Tunstall codes can be decoded as follows :
  - Read a fixed-length codeword from the input stream, and look up its corresponding variable-length codeword in the table.
  - Output the symbols in the variable-length codeword, and repeat until the end of the input stream is reached.