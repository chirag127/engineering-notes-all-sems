### Golomb codes

Golomb codes are a form of parameterized coding in which integers to be coded are stored as values relative to a constant b. The coding of a positive number x is represented in two parts:

1. The first part is an unary representation of q+1, where q is the quotient floor((x/b)).
2. The second part is a special binary representation of the remainder r = x-qb. Note that there are b potential remainders.

Golomb codes divide all index values i into equal-sized groups of size m. The codeword is then constructed from a unary code that characterizes each group, followed by a fixed-length code that specifies the remainder of the index that has been encoded.

Golomb coding uses a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder. The quotient is sent in unary coding, followed by the remainder in truncated binary encoding.

For example, for a source x with geometric distribution, with parameter p(0) = 0.2, using Golomb code with M = 3. The 2-bit code 00 is used 20% of the time; the 3-bit codes 010, 011, and 100 are used over 38% of the time; 4 bits or more are needed in a minority of cases.