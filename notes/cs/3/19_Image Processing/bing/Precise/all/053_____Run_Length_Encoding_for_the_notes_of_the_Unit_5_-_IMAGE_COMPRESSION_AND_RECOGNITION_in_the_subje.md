# Run Length Encoding

Run Length Encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced by just one data value and count. It is most suited to compress data with many runs, for example, simple graphic images such as icons, line drawings, and animations.

Here are some key points to remember about RLE:
- RLE is a lossless compression technique, meaning that the original data can be perfectly reconstructed from the compressed data.
- RLE is most effective when the data contains many runs of the same value.
- RLE is not effective for compressing data with few runs or with runs of short length.
- RLE can be applied to any data type, including text, images, and audio.
- RLE is simple to implement and fast to encode and decode.

In the context of image compression, RLE can be applied to compress bitmap images. Bitmap images are represented as a two-dimensional array of pixels, where each pixel is represented by a value indicating its color. RLE can be applied to compress the rows or columns of the image, by replacing runs of the same pixel value with a single value and count.

For example, consider the following bitmap image:

```
1 1 1 1 0 0 0 0
1 1 1 1 0 0 0 0
0 0 0 0 1 1 1 1
0 0 0 0 1 1 1 1
```

If we apply RLE to compress the rows of the image, we get the following compressed representation:

```
4 1 4 0
4 1 4 0
4 0 4 1
4 0 4 1
```

Each row of the compressed image contains two pairs of values, where the first value in each pair is the count and the second value is the pixel value. For example, the first row of the compressed image `4 1 4 0` represents a run of 4 pixels with value 1, followed by a run of 4 pixels with value 0.

RLE can also be applied to compress the columns of the image, resulting in a different compressed representation.

In summary, RLE is a simple and effective technique for compressing data with many runs. It is most suited to compress simple graphic images, such as icons, line drawings, and animations. RLE is lossless, fast, and easy to implement. However, it is not effective for compressing data with few runs or with runs of short length.