### Run Length Encoding

Run Length Encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced by just one data value and count. It is a lossless data compression technique that is well-suited for applications with simple graphic images such as icons, line drawings, and animations.

Here are some key points to remember about RLE:

1. RLE is a lossless data compression technique, meaning that the original data can be perfectly reconstructed from the compressed data.
2. RLE is best suited for data with many runs of the same value, such as simple graphic images with large areas of the same color.
3. RLE is not well-suited for compressing data with few runs or with runs of varying lengths, as it may actually increase the size of the data.
4. RLE is simple to implement and fast to encode and decode.
5. RLE is commonly used in fax machines, where the data being transmitted is mostly white space with occasional black lines.
