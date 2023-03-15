### The Burrows-Wheeler Transform

- The Burrows-Wheeler Transform (BWT) is an algorithm used to prepare data for use with data compression techniques such as bzip2 .
- It was invented by Michael Burrows and David Wheeler in 1994 while Burrows was working at DEC Systems Research Center in Palo Alto, California. It is based on a previously unpublished transformation discovered by Wheeler in 1983.
- The BWT rearranges a character string into runs of similar characters. This is useful for compression, since it tends to be easy to compress a string that has runs of repeated characters by techniques such as move-to-front transform and run-length encoding .
- The BWT is a reversible permutation of the characters of a string . One procedure exists for turning a string T into BWT(T) and another exists for turning BWT(T) back into T.
- The procedure for computing BWT(T) is as follows  :
  - Append a special symbol $ to the end of T, which is lexicographically smaller than any other character in T.
  - Construct a table of all cyclic rotations of T$ sorted lexicographically.
  - The BWT(T) is the last column of the table.
- For example, if T = banana, then the table of cyclic rotations is:

| T$     |
|--------|
| banana$|
| anana$b|
| nana$ba|
| ana$ban|
| na$bana|
| a$banan|
| $banana|

- The last column is annb$aa, which is the BWT(banana).
- The procedure for recovering T from BWT(T) is as follows :
  - Construct the first column of the table of cyclic rotations by sorting the characters of BWT(T) lexicographically.
  - For each character in BWT(T), count how many times it appears before its position in BWT(T). This is called the rank of the character.
  - For each character in the first column, count how many times it appears before its position in the first column. This is called the index of the character.
  - For each character in BWT(T), find the character in the first column that has the same rank and index. This is called the LF-mapping (last-to-first mapping).
  - Starting from the $ symbol in BWT(T), follow the LF-mapping until reaching the $ symbol in the first column. The recovered string T is the sequence of characters visited in the first column, excluding the $ symbol.
- For example, if BWT(T) = annb$aa, then the first column is $aaabnn, and the ranks and indices are:

| BWT(T) | Rank | First column | Index | LF-mapping |
|--------|------|--------------|-------|------------|
| a      | 0    | $            | 0     | $ -> a     |
| n      | 0    | a            | 0     | a -> n     |
| n      | 1    | a            | 1     | n -> n     |
| b      | 0    | a            | 2     | n -> b     |
| $      | 0    | b            | 0     | b -> $     |
| a      | 1    | n            | 0     | $ -> a     |
| a      | 2    | n            | 1     | a -> a     |

- Following the LF-mapping from $ in BWT(T) to $ in the first column, we get the sequence $ -> a -> n -> n -> b -> $, which corresponds to the string annb, which is T without the $ symbol.