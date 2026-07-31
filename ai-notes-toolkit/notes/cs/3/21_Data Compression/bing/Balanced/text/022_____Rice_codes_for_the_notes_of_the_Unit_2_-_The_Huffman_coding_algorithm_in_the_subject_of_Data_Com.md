### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the encoding process.
- To encode a positive integer x using Rice codes, the following steps are performed:
  - Divide x by m and write the quotient in unary code, i.e., a sequence of 1s followed by a 0.
  - Write the remainder of x/m in binary code, using k bits.
  - Concatenate the unary and binary codes to form the final code.
- For example, if k = 2 and x = 11, then the Rice code is:
  - 11 / 4 = 2 with remainder 3, so the unary code is 110 and the binary code is 11.
  - The final code is 11011.
- Rice codes are generally used to encode entropy in audio/video codecs, where the data often follows a Laplacian distribution.
- Rice codes are also used in adaptive coding schemes, where the parameter k is adjusted according to the statistics of the data.