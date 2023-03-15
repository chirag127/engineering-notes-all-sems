### The Burrows-Wheeler Transform

The Burrows-Wheeler Transform (BWT) is an algorithm that rearranges a string of characters into runs of similar characters. This is useful for data compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding. The BWT is also reversible, meaning that the original string can be recovered from the transformed string.

The BWT works as follows:

- Given a string T, append a special symbol $ to the end of T. The symbol $ should be lexicographically smaller than any other character in T.
- Construct a matrix M that contains all possible cyclic rotations of T$. Sort the rows of M lexicographically.
- The BWT of T is the last column of M.

For example, given the string T = banana, the BWT is annb$aa, as shown below:

| | | | | | | |
|-|-|-|-|-|-|-|
|b|a|n|a|n|a|$|
|a|$|b|a|n|a|n|
|n|a|$|b|a|n|a|
|a|n|a|$|b|a|n|
|n|a|n|a|$|b|a|
|a|n|a|n|a|$|b|
|$|b|a|n|a|n|a|

To reverse the BWT, we can use the following algorithm:

- Given a string BWT(T), construct an array F that contains the first column of the sorted matrix M. This can be done by sorting the characters of BWT(T) lexicographically.
- Construct an array L that contains the last column of M, which is BWT(T).
- Construct an array C that counts the number of occurrences of each character in F up to a given position. For example, C[a][3] is the number of a's in F[0..3].
- Construct an array P that maps each character in L to its corresponding position in F. This can be done by using C to keep track of the next available position for each character. For example, P[0] is the position of L[0] in F, and C[L[0]] is incremented by one.
- Starting from P[0], follow the pointers in P until reaching the position of the $ symbol. The original string T can be obtained by concatenating the characters in L along the way, excluding the $ symbol.

For example, given the string BWT(T) = annb$aa, the reversal algorithm works as follows:

| | | | | | | |
|-|-|-|-|-|-|-|
|F|L|C[a]|C[b]|C[n]|C[$]|P|
|a|a|1|0|0|0|5|
|a|a|2|0|0|0|6|
|a|n|3|0|1|0|2|
|b|n|3|1|2|0|3|
|n|b|3|1|3|0|1|
|n|$|3|1|4|1|0|
|$|a|3|1|4|2|4|

The original string T can be recovered by following the pointers in P:

P[0] -> P[5] -> P[6] -> P[2] -> P[3] -> P[1] -> P[4]

L[0] -> L[5] -> L[6] -> L[2] -> L[3] -> L[1] -> L[4]

a -> a -> n -> a -> n -> a -> b

T = banana

Some properties of the BWT are:

- The BWT preserves the number and frequency of each character in the original string.
- The BWT is a permutation of the original string, meaning that no information is lost or added.
- The BWT tends to group similar characters together, creating long runs of repeated characters. This makes the BWT suitable for compression techniques that exploit redundancy.
- The BWT can also be used for efficient string matching and indexing, by using a data structure called the FM-index. The FM-index combines the BWT with additional information to allow fast queries on the original string without decompressing it.