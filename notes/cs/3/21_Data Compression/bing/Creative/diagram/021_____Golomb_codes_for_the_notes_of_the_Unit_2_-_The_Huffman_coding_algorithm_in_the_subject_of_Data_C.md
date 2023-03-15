### Golomb codes

- Golomb codes are a form of parameterized coding that can be used to compress data with geometric or exponential distributions .
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder .
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r  .
- The binary code for r can be either fixed-length or variable-length, depending on the value of M .
- If M is a power of 2, the binary code for r is fixed-length and has log2(M) bits .
- If M is not a power of 2, the binary code for r is variable-length and uses a technique called truncated binary encoding .
- Truncated binary encoding splits the range of possible values of r into two subranges: the lower range [0, b-1] and the upper range [b, M-1], where b = 2^ceil(log2(M))^ - M.
- The lower range has b values and can be encoded with floor(log2(M)) bits, while the upper range has M-b values and can be encoded with ceil(log2(M)) bits.
- The binary code for r is then constructed by appending a 0 or a 1 to indicate which subrange r belongs to, followed by the binary representation of r in the corresponding subrange.
- Golomb codes are optimal for data with geometric distributions, where the probability of x is proportional to (1-p)^x^ for some p .
- The optimal value of M for geometric distributions is M = -1/log2(1-p) or the nearest integer .
- Golomb codes can also be used for data with exponential distributions, where the probability of x is proportional to e^-lambda x^ for some lambda.
- The optimal value of M for exponential distributions is M = 1/lambda or the nearest integer.
- Golomb codes have applications in lossless compression of text, images, audio, and video, especially for data with high skewness or long-tailed distributions .
- Golomb codes are also used in run-length encoding, where the lengths of runs of identical symbols are encoded with Golomb codes .
- Golomb codes are closely related to Rice codes, which are a special case of Golomb codes where M is a power of 2 .