### The LZ78 Approach

- LZ78 is a lossless data compression algorithm that was published by Abraham Lempel and Jacob Ziv in 1978.
- LZ78 compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry  .
- LZ78 uses a trie data structure to store the dictionary, as it is more efficient for this compression technique. A trie is a tree-like data structure that stores strings as paths from the root to the leaves, where each node represents a character and each edge represents a prefix.
- The algorithm works as follows :
  - Initialize the dictionary with an empty string as the first entry.
  - Read the next character from the input and append it to the current token.
  - If the current token is already in the dictionary, continue reading the next character and appending it to the current token.
  - If the current token is not in the dictionary, output the index of the longest prefix of the current token that is in the dictionary, followed by the last character of the current token. Then, add the current token to the dictionary as a new entry, and reset the current token to an empty string.
  - Repeat until the end of the input is reached.
- For example, consider the input string "abracadabra" and the following dictionary:

| Index | Token |
| ----- | ----- |
| 0     | ""    |
| 1     | "a"   |
| 2     | "b"   |
| 3     | "r"   |
| 4     | "ab"  |
| 5     | "c"   |
| 6     | "ad"  |
| 7     | "ra"  |
| 8     | "abr" |
| 9     | "aca" |
| 10    | "dab" |

- The output of the LZ78 compression algorithm would be:

| Index | Character |
| ----- | --------- |
| 0     | a         |
| 0     | b         |
| 0     | r         |
| 1     | b         |
| 0     | c         |
| 1     | d         |
| 3     | a         |
| 1     | b         |
| 3     | a         |

- The output can be decoded by using the same dictionary and reversing the process. For each index-character pair, concatenate the token at the index with the character and output it. Then, add the new token to the dictionary as a new entry. For example, the first pair (0, a) would output "a" and add "a" to the dictionary. The second pair (0, b) would output "b" and add "b" to the dictionary. The third pair (0, r) would output "r" and add "r" to the dictionary. The fourth pair (1, b) would output "ab" and add "ab" to the dictionary, and so on.
- The advantages of LZ78 are that it does not require any parameterization, it can handle any type of data, and it can adapt to changes in the data distribution.
- The disadvantages of LZ78 are that it can produce a large dictionary that may not fit in memory, it can output long codes for rare tokens, and it can be slow to encode and decode.