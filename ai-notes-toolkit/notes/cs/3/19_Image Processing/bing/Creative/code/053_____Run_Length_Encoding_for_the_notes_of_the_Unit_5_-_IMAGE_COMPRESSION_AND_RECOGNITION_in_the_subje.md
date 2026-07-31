### Run Length Encoding

Run length encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.

- RLE works best on binary images or images with large areas of uniform color .
- RLE reduces the size of the image by eliminating the redundancy in the data.
- RLE can be applied to each row or column of the image, or to the whole image as a single stream of data.
- RLE can be implemented in different ways, such as using a marker symbol to indicate the start of a run, or using a fixed-length or variable-length code to represent the count of a run.
- RLE can be combined with other compression techniques, such as Huffman coding, to achieve better compression ratios.

#### Example of RLE

Consider the following binary image:

```
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000011110000
0000000011110000
0000000011110000
0000000011110000
0000000000000000
```

One possible way to apply RLE to this image is to encode each row as a sequence of pairs, where each pair consists of the number of zeros followed by the number of ones. For example, the first row can be encoded as (16, 0), meaning 16 zeros and 0 ones. The 12th row can be encoded as (8, 4, 4, 0), meaning 8 zeros, 4 ones, 4 zeros, and 0 ones. The encoded image would look like this:

```
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(16, 0)
(8, 4, 4, 0)
(8, 4, 4, 0)
(8, 4, 4, 0)
(8, 4, 4, 0)
(16, 0)
```

The original image has 256 bits, while the encoded image has 64 bits, resulting in a compression ratio of 4:1.