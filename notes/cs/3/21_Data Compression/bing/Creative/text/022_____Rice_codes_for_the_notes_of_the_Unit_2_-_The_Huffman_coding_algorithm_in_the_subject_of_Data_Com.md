### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the Golomb codes.
- To encode a number x using Rice codes, the following steps are performed :
  - Divide x by m and write the quotient in unary code, i.e., a sequence of 1s followed by a 0.
  - Write the remainder in binary code, using k bits.
  - Concatenate the unary and binary codes to form the Rice code for x.
- For example, if k = 2 and x = 11, then the Rice code is 1110 11, where 1110 is the unary code for 11/4 = 2 and 11 is the binary code for 11%4 = 3.
- To decode a Rice code, the following steps are performed :
  - Read the unary code until a 0 is encountered and count the number of 1s, which is the quotient q.
  - Read the next k bits and interpret them as a binary number, which is the remainder r.
  - Multiply q by m and add r to obtain the original number x.
  - For example, if k = 2 and the Rice code is 1110 11, then the decoded number is 2*4 + 3 = 11.