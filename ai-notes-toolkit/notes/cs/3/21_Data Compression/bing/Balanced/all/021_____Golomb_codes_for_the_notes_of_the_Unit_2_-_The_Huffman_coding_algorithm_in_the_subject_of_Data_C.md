# Golomb codes

- Golomb codes are a form of parameterized coding that can be used to compress data with geometric or exponential distributions .
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder.
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r .
- The binary code for r can be either fixed-length or variable-length, depending on the value of M .
- If M is a power of 2, the binary code for r is fixed-length and has log2(M) bits .
- If M is not a power of 2, the binary code for r is variable-length and uses a technique called truncated binary encoding .
- Truncated binary encoding splits the range of possible values of r into two subranges: a lower range of size b, where b is the largest power of 2 that is less than or equal to M, and an upper range of size M-b.
- The values in the lower range are encoded with log2(b) bits, while the values in the upper range are encoded with log2(b)+1 bits, with the extra bit indicating that the value belongs to the upper range.
- Golomb codes are optimal for data that follows a geometric distribution with parameter p, where p = 1/M.
- Golomb codes can also be used for data that follows a Zipfian distribution, where the frequency of the i-th most common symbol is proportional to 1/i.
- Golomb codes have applications in lossless compression of text, images, audio, and video, especially for data with high entropy or long-tailed distributions .