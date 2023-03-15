### Golomb codes

- Golomb codes are a type of parameterized codes that can encode positive integers with variable-length codewords.
- Golomb codes use a parameter M to divide an input value x into two parts: q, the quotient of x divided by M, and r, the remainder of x modulo M.
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r.
- The unary code for q+1 is a sequence of q ones followed by a zero. For example, the unary code for 4 is 1110.
- The binary code for r depends on the value of M. If M is a power of 2, say M=2^n, then the binary code for r is simply the n-bit binary representation of r. For example, if M=8, then the binary code for r=5 is 101.
- If M is not a power of 2, then the binary code for r is a truncated binary code, which uses fewer bits for the smaller values of r. For example, if M=5, then the binary code for r=0 is 0, for r=1 is 10, for r=2 is 110, for r=3 is 1110, and for r=4 is 1111.
- The length of the codeword for x is q+1 plus the number of bits needed to encode r. For example, if M=5 and x=17, then q=3, r=2, the unary code for q+1 is 11110, the binary code for r is 110, and the codeword for x is 11110110, which has length 8.
- Golomb codes are optimal for encoding geometric distributions, where the probability of x is proportional to (1-p)^x for some p. The optimal value of M is approximately -1/log(1-p).
- Golomb codes are widely used in data compression, especially for lossless compression of images and audio. Some examples of applications are run-length encoding, Rice coding, and exp-Golomb coding.