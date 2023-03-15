# Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the encoding process.
- To encode a number x using Rice codes, the following steps are performed :
  - Divide x by m and write the quotient in unary code. Unary code is a code that uses only one symbol, usually 1, to represent a number. For example, 5 in unary code is 11111.
  - Write the remainder of x/m in binary code, using k bits. For example, if k = 3 and the remainder is 6, then the binary code is 110.
  - Concatenate the unary code and the binary code to form the Rice code. For example, if x = 23, k = 3, m = 8, then the quotient is 2, the remainder is 7, the unary code is 11, the binary code is 111, and the Rice code is 11111.
- To decode a Rice code, the following steps are performed :
  - Count the number of 1s in the unary code until a 0 is encountered. This is the quotient of x/m.
  - Read the next k bits as the binary code for the remainder of x/m.
  - Multiply the quotient by m and add the remainder to obtain x.
  - For example, if the Rice code is 11111, k = 3, m = 8, then the quotient is 2, the remainder is 7, and x = 2*8 + 7 = 23.
- Rice codes are suitable for data sets that have a geometric or exponential distribution, where most of the values are small and the probability of larger values decreases rapidly.
- Rice codes are often used in audio and video compression, where the difference between adjacent samples or pixels tends to be small.