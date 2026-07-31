# The LZ78 Approach

LZ78 is a lossless data compression algorithm that was proposed by Abraham Lempel and Jacob Ziv in 1978. It is based on the idea of building a dictionary of phrases from the input data, and replacing repeated occurrences of the phrases with references to the dictionary entries. The algorithm works as follows:

- Initialize an empty dictionary.
- Read the next symbol from the input.
- If the symbol is not in the dictionary, output the symbol and add it to the dictionary as a new entry with a unique index.
- If the symbol is in the dictionary, read the next symbol and form a pair with the previous symbol.
- If the pair is not in the dictionary, output the index of the previous symbol and the current symbol, and add the pair to the dictionary as a new entry with a unique index.
- If the pair is in the dictionary, repeat the previous step until a pair is not found or the input is exhausted.
- Output the index of the last pair found in the dictionary.

## Example

Suppose we want to compress the following string using LZ78:

`abracadabra`

The algorithm would produce the following output:

| Symbol | Pair | Output | Dictionary |
|--------|------|--------|------------|
| a      | N/A  | a      | {1: a}     |
| b      | N/A  | b      | {1: a, 2: b} |
| r      | N/A  | r      | {1: a, 2: b, 3: r} |
| a      | (b, a) | 2a     | {1: a, 2: b, 3: r, 4: ba} |
| c      | N/A  | c      | {1: a, 2: b, 3: r, 4: ba, 5: c} |
| a      | (d, a) | 4a     | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da} |
| b      | (r, a) | 3a     | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da, 7: ra} |
| r      | (a, b) | 1b     | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da, 7: ra, 8: ab} |
| a      | N/A  | 1      | {1: a, 2: b, 3: r, 4: ba, 5: c, 6: da, 7: ra, 8: ab} |

The final compressed string is:

`abr2ac4a3a1b1`

## Advantages and Disadvantages

LZ78 has some advantages and disadvantages compared to other compression algorithms. Some of them are:

- It does not require a sliding window or a look-ahead buffer, which simplifies the implementation and reduces the memory usage.
- It can adapt to different types of data and does not need a predefined dictionary or a fixed code length.
- It can achieve high compression ratios for data with long repetitions or regular patterns.
- It can suffer from dictionary overflow, which means that the dictionary can grow too large and exceed the available memory or the maximum index size.
- It can produce long codes for rare or single symbols, which can reduce the compression ratio or even increase the size of the output.
- It can be slow to encode and decode, especially for large dictionaries, as it requires searching and updating the dictionary for every symbol or pair.