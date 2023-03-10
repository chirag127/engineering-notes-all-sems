 Here is the content written in markdown format for the topic ### The Burrows-Wheeler Transform for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression:

## The Burrows-Wheeler Transform (BWT)

- The Burrows-Wheeler Transform (BWT) is a reversible permutation of a sequence that makes repetitive patterns more apparent.
- It is commonly used as a pre-processing step for data compression algorithms.
- The BWT rearranges the characters in the input string in such a way that identical characters are grouped together. This allows for more efficient compression.
- The steps to calculate the BWT of a string are:
1. Append a unique character $ (not present in the original string) to the end of the string. This is called the sentinel.
2. Create all circular rotations of the string.
3. Sort all rotations lexicographically.
4. The last column of characters from the sorted list of rotations is the Burrows-Wheeler Transform (BWT) of the input string.

- For example, the BWT of the string "abcd$" would be:
 rotations:  abcd$  bcd$a   cd$ab   d$abc
 sorted:    bcd$a   abcd$   cd$ab   d$abc
 BWT:        d      a       b       $

- The BWT is reversible. The original string can be reconstructed from the BWT and the first column of the sorted rotations.
- The BWT is useful for compression because it collects similar characters together, allows the use of statistical modelling and run-length encoding for better compression. It is used in algorithms like bzip2.
- The time complexity to calculate the BWT is O(n log n) due to the sorting of rotations. The space complexity is O(n) to store the rotations.