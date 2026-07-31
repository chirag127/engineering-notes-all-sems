# Diagram Coding

Diagram coding is a lossless data compression method that replaces frequently occurring pairs of symbols (digrams) with unused codes. It is an example of an ad hoc compression algorithm, which means it does not rely on any prior knowledge of the source or the statistical properties of the data.

## Steps of diagram coding

1. Scan the source data and identify all the symbols and digrams that are used. Assign a code to each symbol, usually of fixed length, such as 8 bits for ASCII characters. Also, find the unused codes that can be used for digrams, such as control characters or extended ASCII codes.
2. Create a dictionary that maps each digram to an unused code. The dictionary can be sorted by the frequency of the digrams, so that the most common ones get the shortest codes. Alternatively, the dictionary can be built dynamically during the compression process, by adding new digrams as they are encountered.
3. Scan the source data again and output the codes for each symbol or digram. If the current symbol and the next one form a digram that is in the dictionary, output the code for that digram and skip the next symbol. Otherwise, output the code for the current symbol and move to the next one.
4. Optionally, repeat steps 2 and 3 until the dictionary is full or no further compression is possible. This is called iterative diagram coding, and it can improve the compression ratio by capturing longer patterns of symbols.

## Example of diagram coding

Suppose we want to compress the following text:

`Hello, world!`

Assume we use 8-bit ASCII codes for the symbols, and we have 32 unused codes from 128 to 159. The dictionary for the first iteration of diagram coding would look like this:

| Digram | Code  |
| ------ | ----- |
| He     | 128   |
| ll     | 129   |
| lo     | 130   |
| wo     | 131   |
| ld     | 132   |
| or     | 133   |
| !      | 134   |

The compressed output for the first iteration would be:

`128 130 44 32 131 133 132 134`

The compression ratio for the first iteration would be:

`(8 * 13) / (8 * 8) = 1.625`

If we repeat the process for the second iteration, the dictionary would look like this:

| Digram | Code  |
| ------ | ----- |
| 130 44 | 135   |
| 131 133| 136   |
| 132 134| 137   |

The compressed output for the second iteration would be:

`128 135 32 136 137`

The compression ratio for the second iteration would be:

`(8 * 13) / (8 * 5) = 2.6`

We can see that the compression ratio has improved by using iterative diagram coding. However, the dictionary is now full and no further compression is possible. Also, note that the dictionary has to be transmitted along with the compressed data, which adds to the overhead.