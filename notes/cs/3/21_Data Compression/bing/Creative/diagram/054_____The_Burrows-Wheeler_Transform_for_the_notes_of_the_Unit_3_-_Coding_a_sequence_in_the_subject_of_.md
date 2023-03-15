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

| | |
|---|---|
|banana$|anana$b|
|anana$b|nana$ba|
|nana$ba|ana$ban|
|ana$ban|na$bana|
|na$bana|a$banan|
|a$banan|$banana|
|$banana|banana$|

- The last column is annb$aa, which is the BWT(banana).
- The procedure for recovering T from BWT(T) is as follows :
  - Construct the first column of the table by sorting the characters of BWT(T) lexicographically.
  - For each character in BWT(T), find its rank among the characters with the same value in BWT(T) from left to right.
  - For each character in the first column, find its rank among the characters with the same value in the first column from top to bottom.
  - Starting from the row with the $ symbol, follow the rank correspondence between the first and the last column until reaching the $ symbol again.
  - The recovered string T is the sequence of characters encountered along the way, excluding the $ symbol.
- For example, if BWT(T) = annb$aa, then the first column is $aaaabnn and the rank correspondence is:

| | | | | |
|---|---|---|---|---|
|BWT(T)|Rank|First|Rank|T|
|a|1|$|1|a|
|n|1|a|1|n|
|n|2|a|2|a|
|b|1|a|3|n|
|$|1|a|4|a|
|a|2|b|1|b|
|a|3|n|1|$|

- The recovered string T is banana, which is the original string.