### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that are optimal for encoding data with geometrically distributed probabilities.
- Rice codes use a parameter k, which is related to the parameter m of Golomb codes by m = 2^k^.
- Rice codes are simpler to implement than Golomb codes, but they may not be optimal for all distributions.
- Rice codes are often used to encode the entropy or the residual data in audio and video compression algorithms.
- The encoding process of Rice codes is as follows:
  - Given a positive integer x and a parameter k, divide x by 2^k^ and obtain the quotient q and the remainder r.
  - Encode q as a unary code, which is a string of q ones followed by a zero.
  - Encode r as a k-bit binary code, which is the binary representation of r with leading zeros if necessary.
  - Concatenate the unary code and the binary code to form the Rice code of x.
- For example, if x = 13 and k = 2, then q = 3 and r = 1. The unary code of q is 1110 and the binary code of r is 01. The Rice code of x is 111001.
- The decoding process of Rice codes is the reverse of the encoding process:
  - Given a Rice code and a parameter k, count the number of ones before the first zero and obtain the quotient q.
  - Read the next k bits and obtain the remainder r as a binary number.
  - Multiply q by 2^k^ and add r to obtain the original integer x.
  - For example, if the Rice code is 111001 and k = 2, then q = 3 and r = 1. The original integer x is 3 * 2^2^ + 1 = 13.