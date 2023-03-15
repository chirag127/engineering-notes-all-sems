# Facsimile Encoding

- Facsimile encoding is a form of lossless data compression that is often used for document imaging and fax transmission.
- Facsimile encoding reduces the amount of data needed to represent a binary image, such as a scanned document or a fax page, by exploiting the spatial redundancy and the high contrast between black and white pixels.
- Facsimile encoding consists of two steps: run-length encoding and Huffman encoding.

## Run-length encoding

- Run-length encoding is a simple technique that replaces consecutive identical symbols (runs) with a pair of the symbol and the run length.
- For example, the binary sequence 0000001111100000 can be encoded as (0,6)(1,5)(0,4), where each pair is a symbol and a run length.
- Run-length encoding is effective for binary images that have large areas of black or white pixels, such as text or line drawings.
- Run-length encoding can be further improved by using different codes for black and white runs, and by using variable-length codes for the run lengths.

## Huffman encoding

- Huffman encoding is a technique that assigns optimal variable-length codes to symbols based on their probabilities of occurrence.
- Huffman encoding builds a binary tree that represents the code assignments, where the most frequent symbols are assigned the shortest codes and the least frequent symbols are assigned the longest codes.
- Huffman encoding can compress the run-length encoded data by using shorter codes for the more common runs and longer codes for the less common runs.
- Huffman encoding can be adaptive, meaning that the code assignments can be updated based on the statistics of the data.

## Example

- Consider the following binary image of size 8x8 pixels:

```
00000000
00000000
00000000
00000000
00000000
00000000
00000000
00000000
```

- The run-length encoded data is:

```
(0,64)
```

- The Huffman encoded data is:

```
0
```

- The original image requires 64 bits to store, while the facsimile encoded data requires only 1 bit, achieving a compression ratio of 64:1.