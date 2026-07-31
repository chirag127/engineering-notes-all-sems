### Golomb codes

Golomb codes are a type of parameterized codes that are suitable for encoding values that follow a geometric distribution. They are often used in data compression applications, such as lossless image compression and entropy coding.

The main idea of Golomb coding is to divide the input value x into two parts: q, the quotient of x divided by a parameter M, and r, the remainder of x modulo M. The quotient q is encoded in unary code, which consists of q ones followed by a zero. The remainder r is encoded in a binary code, which depends on the value of M.

There are two cases for encoding the remainder r:

- If M is a power of 2, say M = 2^n, then r can be encoded in a fixed-length n-bit binary code. For example, if M = 4, then r can be 0, 1, 2, or 3, and can be encoded as 00, 01, 10, or 11, respectively.
- If M is not a power of 2, then r can be encoded in a variable-length binary code, which uses a prefix code to avoid ambiguity. One way to construct such a code is to use a truncated binary code, which divides the possible values of r into two subranges: the lower subrange, which contains floor(M/2) values, and the upper subrange, which contains ceil(M/2) values. The lower subrange values are encoded in a fixed-length floor(log2(M)) bit binary code, while the upper subrange values are encoded in a fixed-length ceil(log2(M)) bit binary code, with a leading 1 to distinguish them from the lower subrange values. For example, if M = 5, then r can be 0, 1, 2, 3, or 4, and can be encoded as 00, 01, 10, 110, or 111, respectively.

The parameter M can be chosen to optimize the compression performance, depending on the probability distribution of the input values. A common choice is to use M = floor(-1/log2(1-p)), where p is the probability of the most frequent value. This minimizes the expected codeword length for a geometric distribution with parameter p.

Here is an example of Golomb coding for a source x with geometric distribution, with parameter p(0) = 0.2, using Golomb code with M = 3.

| x | q | r | q (unary) | r (binary) | Codeword |
|---|---|---|-----------|------------|----------|
| 0 | 0 | 0 | 0         | 00         | 000      |
| 1 | 0 | 1 | 0         | 01         | 001      |
| 2 | 0 | 2 | 0         | 10         | 010      |
| 3 | 1 | 0 | 10        | 00         | 1000     |
| 4 | 1 | 1 | 10        | 01         | 1001     |
| 5 | 1 | 2 | 10        | 10         | 1010     |
| 6 | 2 | 0 | 110       | 00         | 11000    |
| 7 | 2 | 1 | 110       | 01         | 11001    |
| 8 | 2 | 2 | 110       | 10         | 11010    |
| 9 | 3 | 0 | 1110      | 00         | 111000   |
| 10| 3 | 1 | 1110      | 01         | 111001   |
| 11| 3 | 2 | 1110      | 10         | 111010   |

The average codeword length for this example is 3.2 bits, which is close to the entropy of the source, which is -log2(0.2) = 2.32 bits.