### The Exclusion Principle for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data file by using various techniques that exploit the redundancy or patterns in the data.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not after decompression.
- Coding a sequence is one of the methods of lossless data compression, where a sequence of symbols (such as characters or bytes) is encoded using a shorter sequence of bits.
- The exclusion principle is a technique used in some coding algorithms, such as PPM (Prediction by Partial Matching), to improve the compression ratio by excluding some symbols from the probability computation.
- The exclusion principle works as follows:
  - The unit interval [0, 1) is divided into subintervals, each of which represents a symbol in the alphabet.
  - The size of each subinterval is proportional to the probability of the symbol in the current context, which is determined by the previous symbols in the sequence.
  - The subinterval corresponding to the encoded symbol is further divided into smaller subintervals for the next symbol, and so on, until the end of the sequence is reached.
  - The exclusion principle applies when a symbol is not present in the current context, meaning that it has zero probability. In that case, the subinterval for that symbol is excluded from the division, and the remaining subintervals are scaled up to fill the gap.
  - This way, the exclusion principle avoids wasting bits on symbols that are impossible to occur, and increases the compression ratio by assigning more bits to the symbols that are more likely to occur.