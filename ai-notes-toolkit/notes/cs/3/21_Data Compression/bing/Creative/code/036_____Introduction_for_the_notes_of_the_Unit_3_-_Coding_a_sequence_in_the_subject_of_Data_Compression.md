### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or distorting its meaning.
- Data compression can be achieved by using various techniques, such as encoding, decoding, entropy, redundancy, and lossless or lossy compression.
- Encoding is the process of transforming data into a different format that uses fewer bits or symbols.
- Decoding is the process of recovering the original data from the encoded format.
- Entropy is a measure of the uncertainty or randomness of data. It indicates the minimum number of bits or symbols needed to represent the data without loss of information.
- Redundancy is the amount of extra or unnecessary information in data that can be removed or replaced without affecting its meaning.
- Lossless compression is a type of compression that preserves the exact information of the original data. It allows the original data to be reconstructed perfectly from the compressed data.
- Lossy compression is a type of compression that discards some information of the original data. It reduces the size of data more than lossless compression, but it may introduce some distortion or error in the reconstructed data.
- Coding a sequence is a technique of lossless compression that assigns codes to the symbols or characters of a data sequence based on their frequency or probability of occurrence.
- Coding a sequence can be done by using various methods, such as fixed-length coding, variable-length coding, Huffman coding, arithmetic coding, and run-length encoding.
- Fixed-length coding is a method of coding a sequence that assigns codes of equal length to all the symbols or characters of a data sequence.
- Variable-length coding is a method of coding a sequence that assigns codes of different lengths to the symbols or characters of a data sequence based on their frequency or probability of occurrence. The more frequent or probable symbols or characters have shorter codes, and the less frequent or probable symbols or characters have longer codes.
- Huffman coding is a type of variable-length coding that constructs an optimal binary tree that minimizes the average code length of a data sequence. It assigns codes to the symbols or characters of a data sequence by traversing the binary tree from the root to the leaves.
- Arithmetic coding is a type of variable-length coding that assigns codes to the symbols or characters of a data sequence by dividing a unit interval into subintervals based on their frequency or probability of occurrence. It assigns codes to the symbols or characters of a data sequence by narrowing down the subinterval that contains the data sequence.
- Run-length encoding is a type of variable-length coding that assigns codes to the runs or consecutive repetitions of the same symbol or character in a data sequence. It assigns codes to the runs by using a pair of values that indicate the symbol or character and the number of repetitions.