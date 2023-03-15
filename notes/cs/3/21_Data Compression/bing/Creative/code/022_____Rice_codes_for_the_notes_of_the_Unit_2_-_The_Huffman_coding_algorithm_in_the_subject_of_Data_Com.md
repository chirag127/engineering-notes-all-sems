### Rice codes

- Rice codes are a subset of Golomb codes, which are a family of prefix codes that can efficiently encode positive integers .
- Rice codes are named after Robert F. Rice, who used them in an adaptive coding scheme.
- Rice codes depend on a parameter k, which determines the length of the unary part and the binary part of the code .
- The unary part of the code is a sequence of k zeros followed by a one, which indicates the quotient of the integer divided by 2^k^.
- The binary part of the code is the remainder of the integer divided by 2^k^, represented in k bits.
- For example, if k = 2 and the integer is 9, then the quotient is 2 and the remainder is 1. The unary part is 001 and the binary part is 01. The Rice code is 00101.
- Rice codes are optimal when the integers follow a geometric distribution with parameter 1/2^k^ .
- Rice codes are often used to encode entropy in audio and video codecs, where most of the values are small .