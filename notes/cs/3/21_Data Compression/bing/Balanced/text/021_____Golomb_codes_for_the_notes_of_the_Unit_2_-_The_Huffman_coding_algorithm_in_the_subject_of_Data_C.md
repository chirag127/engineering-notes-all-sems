### Golomb codes

- Golomb codes are a type of parameterized codes that can be used to compress data with geometric or exponential distributions.
- Golomb codes use a positive integer parameter M to divide an input value x into two parts: q, the quotient of x divided by M, and r, the remainder of x modulo M.
- The codeword for x consists of two parts: the unary code for q+1, followed by the binary code for r.
- The unary code for q+1 is a sequence of q ones followed by a zero. For example, the unary code for 4 is 1110.
- The binary code for r depends on the value of M. If M is a power of 2, then r is encoded using log2(M) bits. For example, if M=4, then r can be 0, 1, 2, or 3, and can be encoded using 2 bits: 00, 01, 10, or 11.
- If M is not a power of 2, then r is encoded using a truncated binary code, which uses fewer bits for smaller values of r. For example, if M=5, then r can be 0, 1, 2, 3, or 4, and can be encoded using 2 bits for r<4 and 3 bits for r=4: 00, 01, 10, 110, or 111.
- The length of the codeword for x depends on the value of M and the distribution of x. If x has a geometric distribution with parameter p, then the optimal value of M is -log2(p), and the average codeword length is -log2(p) + 1/p bits.
- Golomb codes are useful for compressing data that has a large number of small values and a few large values, such as run-lengths, gaps between occurrences, or residuals in predictive coding.
- Golomb codes can be easily implemented using arithmetic operations such as division, modulo, and bit-shifting.