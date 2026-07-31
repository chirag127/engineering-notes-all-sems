### Golomb codes

- Golomb codes are a form of parameterized coding that can be used to encode integers with a geometric distribution.
- Golomb codes use a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder.
- The codeword for x consists of two parts: a unary code for q+1, followed by a binary code for r.
- The binary code for r depends on whether M is a power of 2 or not:
  - If M is a power of 2, say M = 2^n, then r is encoded using n bits in standard binary representation.
  - If M is not a power of 2, say M = 2^n + k, then r is encoded using one of the following methods:
    - Rice coding: if r < 2^n, use n bits; otherwise, use n+1 bits and add 2^n to r.
    - Elias coding: use n bits for the first 2^n - k values of r; for the remaining k values, use n+1 bits and subtract k from r.
    - Quasi-Elias coding: use n bits for the first M - 2^n values of r; for the remaining 2^n values, use n+1 bits and add M - 2^n to r.
- Golomb codes are optimal for encoding a geometric distribution with parameter p when M is chosen to be the closest integer to -1/log(1-p).
- Golomb codes are widely used in data compression, especially for lossless compression of images and audio.

: https://www.geeksforgeeks.org/python-golomb-encoding-for-b2n-and-b2n/
: https://www.sciencedirect.com/topics/engineering/golomb-code
: https://en.wikipedia.org/wiki/Golomb_coding