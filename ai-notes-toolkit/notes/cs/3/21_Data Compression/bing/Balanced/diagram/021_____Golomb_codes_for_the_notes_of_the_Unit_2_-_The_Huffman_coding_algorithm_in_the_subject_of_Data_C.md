### Golomb codes

- Golomb codes are a form of parameterized coding that can be used to compress data with geometric or exponential distributions .
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder.
- The codeword for x consists of two parts: the unary code for q+1, followed by the truncated binary code for r .
- The unary code for q+1 is a sequence of q ones followed by a zero. For example, the unary code for 4 is 1110.
- The truncated binary code for r depends on whether M is a power of 2 or not .
  - If M is a power of 2, say M=2^n, then r is encoded using n bits in standard binary. For example, if M=8, then r=5 is encoded as 101 .
  - If M is not a power of 2, say M=2^n+k, where 0<k<2^n, then r is encoded using one of two methods :
    - If r<k, then r is encoded using n bits in standard binary. For example, if M=10, then r=3 is encoded as 011 .
    - If r>=k, then r is encoded using n+1 bits, where the first bit is 1 and the remaining n bits are the standard binary representation of r-k. For example, if M=10, then r=7 is encoded as 1011 .
- The length of the codeword for x is q+n or q+n+1 bits, depending on the value of r and M.
- Golomb codes are optimal for data with geometric distributions, where the probability of x is proportional to (1-p)^x for some p.
- Golomb codes are also useful for data with exponential distributions, where the probability of x is proportional to e^(-x/lambda) for some lambda.
- Golomb codes can be generalized to Rice codes, where M is restricted to be a power of 2, and Elias codes, where M is a function of x.