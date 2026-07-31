# Tunstall codes

Tunstall codes are a form of entropy coding used for lossless data compression. They are based on the idea of parsing a stochastic source with codewords of variable length, and then encoding those codewords with fixed-length codes. Tunstall codes have some advantages and disadvantages compared to other entropy coding methods, such as Huffman coding and Lempel-Ziv coding.

## Advantages of Tunstall codes

- Tunstall codes are simple to implement and have low computational complexity.
- Tunstall codes can achieve optimal compression for memoryless sources with rational probabilities, such as geometric distributions.
- Tunstall codes can be easily adapted to changing source statistics by updating the codebook.

## Disadvantages of Tunstall codes

- Tunstall codes require a large codebook size, which increases the storage and transmission overhead.
- Tunstall codes are not universal, meaning they cannot achieve optimal compression for arbitrary sources.
- Tunstall codes are sensitive to errors, as a single bit error can corrupt the entire codeword.

## How to construct Tunstall codes

- Given a source alphabet S and a codebook size N, the goal is to find a set of N codewords C that minimizes the expected codeword length.
- The algorithm starts with a single codeword c0 that represents the entire source alphabet S.
- The algorithm iteratively splits the codeword with the highest probability into |S| new codewords, each appended with a symbol from S.
- The algorithm stops when the codebook size reaches N.
- The algorithm assigns a fixed-length binary code to each codeword in C, such that the most probable codewords have the shortest codes.

## Example of Tunstall codes

- Suppose the source alphabet is S = {a, b, c} with probabilities P(a) = 0.5, P(b) = 0.25, P(c) = 0.25.
- Suppose the codebook size is N = 8.
- The algorithm starts with c0 = S, with P(c0) = 1.
- The algorithm splits c0 into c1 = a, c2 = b, c3 = c, with P(c1) = 0.5, P(c2) = 0.25, P(c3) = 0.25.
- The algorithm splits c1 into c4 = aa, c5 = ab, c6 = ac, with P(c4) = 0.25, P(c5) = 0.125, P(c6) = 0.125.
- The algorithm splits c2 into c7 = ba, c8 = bb, with P(c7) = 0.125, P(c8) = 0.0625.
- The algorithm stops as the codebook size is 8.
- The algorithm assigns the following binary codes:

| Codeword | Probability | Binary code |
|----------|-------------|-------------|
| c4 = aa  | 0.25        | 00          |
| c1 = a   | 0.5         | 01          |
| c2 = b   | 0.25        | 10          |
| c3 = c   | 0.25        | 110         |
| c5 = ab  | 0.125       | 1110        |
| c6 = ac  | 0.125       | 11110       |
| c7 = ba  | 0.125       | 111110      |
| c8 = bb  | 0.0625      | 111111      |

- The expected codeword length is 2.5 bits per symbol, which is optimal for this source.