# Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that are optimal for encoding data with a geometric distribution.
- Rice codes use a parameter k, which is a positive integer, to determine the length and value of the code words.
- To encode a non-negative integer x using Rice codes, the following steps are performed:
  - Divide x by 2^k and write the quotient in unary, i.e., as a sequence of 1s followed by a 0. This is the first part of the code word.
  - Write the remainder of x divided by 2^k in binary, using k bits. This is the second part of the code word.
  - Concatenate the first and second parts to form the final code word.
- For example, if k = 2 and x = 9, then the code word is 11001, because 9 / 4 = 2 (unary: 110), and 9 % 4 = 1 (binary: 01).
- To decode a Rice code, the following steps are performed:
  - Read the unary part of the code word and count the number of 1s. This is the quotient of x divided by 2^k.
  - Read the next k bits of the code word and interpret them as a binary number. This is the remainder of x divided by 2^k.
  - Multiply the quotient by 2^k and add the remainder to obtain x.
- For example, if k = 2 and the code word is 11001, then the quotient is 2 (unary: 110), and the remainder is 1 (binary: 01). Therefore, x = 2 * 4 + 1 = 9.
- Rice codes are simple and efficient to implement, especially when k is a power of 2. They are suitable for encoding data with a high probability of small values and a low probability of large values.
- Rice codes are often used in audio and video compression, where the difference between adjacent samples or pixels tends to follow a geometric distribution. For example, Rice codes are used in FLAC, a lossless audio codec, and JPEG-LS, a lossless image codec.