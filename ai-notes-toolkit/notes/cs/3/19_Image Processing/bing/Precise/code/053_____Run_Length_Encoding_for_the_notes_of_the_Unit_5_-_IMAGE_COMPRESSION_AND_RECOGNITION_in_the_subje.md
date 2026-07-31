### Run Length Encoding

Run Length Encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced by just one data value and count.

1. RLE is a lossless data compression technique, meaning that the original data can be perfectly reconstructed from the compressed data.
2. RLE is most effective on data that contains many such runs, for example, simple graphic images such as icons, line drawings, and animations.
3. RLE is not effective for compressing text or photographic images, as these types of data do not have many runs.
4. RLE is a very simple algorithm and can be implemented easily.
5. RLE is not suitable for compressing data that does not have many runs, as it may even increase the size of the data.

Example: Consider the following sequence of characters: `WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW`

Using RLE, this sequence can be compressed to: `12W1B12W3B24W1B14W`

Here, the runs of `W` characters are replaced by the number of `W` characters followed by a single `W`. Similarly, the runs of `B` characters are replaced by the number of `B` characters followed by a single `B`. This compressed sequence is much shorter than the original sequence.