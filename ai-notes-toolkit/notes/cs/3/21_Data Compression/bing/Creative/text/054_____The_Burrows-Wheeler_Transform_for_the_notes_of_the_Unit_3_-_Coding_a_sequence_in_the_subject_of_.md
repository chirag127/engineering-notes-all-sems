### The Burrows-Wheeler Transform

- The Burrows-Wheeler Transform (BWT) is an algorithm used to prepare data for use with data compression techniques such as bzip2 .
- The BWT rearranges a character string into runs of similar characters, which makes it easier to compress by techniques such as move-to-front transform and run-length encoding .
- The BWT is reversible, meaning that the original string can be recovered from the transformed string without any loss of information  .
- The BWT is based on a lexicographical sorting of all the cyclic rotations of the original string, and appending a special symbol ($) to mark the end of the string  .
- The BWT of a string T is obtained by taking the last column of the sorted matrix of rotations, and the index of the original string in the matrix is called the primary index  .
- For example, the BWT of the string "banana" is computed as follows:

| Original string | Sorted rotations | BWT |
| --------------- | ---------------- | --- |
| banana$         | $banana          | a   |
| anana$b         | a$banan          | n   |
| nana$ba         | ana$ban          | a   |
| ana$ban         | anana$b          | b   |
| na$bana         | banana$          | $   |
| a$banan         | nana$ba          | a   |

- The BWT of "banana" is "annb$aa", and the primary index is 3, which is the position of "banana$" in the sorted matrix.
- The inverse BWT can be performed by using the first and last columns of the sorted matrix, and following the last-to-first mapping that links each character in the last column to its first occurrence in the first column.
- For example, the inverse BWT of "annb$aa" is computed as follows:

| First column | Last column | Last-to-first mapping |
| ------------ | ----------- | --------------------- |
| $            | a           | 0 -> 3                |
| a            | n           | 1 -> 4                |
| a            | n           | 2 -> 5                |
| a            | b           | 3 -> 6                |
| b            | $           | 4 -> 0                |
| n            | a           | 5 -> 1                |
| n            | a           | 6 -> 2                |

- Starting from the primary index 3, we follow the last-to-first mapping until we reach the end symbol $, and we get the original string "banana" by reading the characters in the last column.