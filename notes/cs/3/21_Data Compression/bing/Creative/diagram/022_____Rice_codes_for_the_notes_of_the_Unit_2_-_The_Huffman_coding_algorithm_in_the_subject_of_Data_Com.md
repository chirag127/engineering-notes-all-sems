### Rice codes

- Rice codes are a subset of Golomb codes, which are a type of prefix codes that can be used to compress data with a skewed distribution.
- Rice codes are simpler than Golomb codes, but they may not be optimal for all data sets.
- Rice codes depend on a parameter k, which determines the divisor m = 2^k^ for the encoding process.
- To encode a positive integer x using Rice codes, the following steps are performed :
  - Divide x by m and obtain the quotient q and the remainder r.
  - Write q in unary code, which means using q ones followed by a zero.
  - Write r in binary code, using k bits.
  - Concatenate the unary code and the binary code to form the final code.
- For example, if k = 2 and x = 9, then:
  - Divide 9 by 4 and obtain the quotient 2 and the remainder 1.
  - Write 2 in unary code as 110.
  - Write 1 in binary code as 01, using 2 bits.
  - Concatenate 110 and 01 to form the final code 11001.
- Rice codes are generally used to encode entropy in audio/video codecs, where the data tends to have a geometric distribution.
- Rice codes are also adaptive, which means that the parameter k can be changed according to the statistics of the data.
- Rice codes have the advantage of being fast and easy to implement, but they may not achieve the best compression ratio for some data sets.

: Golomb coding - Wikipedia
: Rice Coding - unix4lyfe.org
: 22.(A). Rice Codes Algorithm: Step by Step Explanation. - YouTube