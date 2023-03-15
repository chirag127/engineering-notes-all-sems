### Run Length Encoding

- Run length encoding (RLE) is a simple and lossless compression technique that reduces the size of an image by encoding consecutive runs of identical pixels with a single value and a count.
- A run is a sequence of adjacent pixels that have the same value (color or intensity).
- The value and the count of each run are stored as a pair of bytes, where the value is the pixel value and the count is the number of pixels in the run.
- RLE is suitable for images that have large areas of uniform color or intensity, such as cartoons, logos, text, etc.
- RLE is not efficient for images that have high spatial frequency or many details, such as natural scenes, photographs, etc.
- RLE can be applied to either binary or grayscale images, or to each color channel of a color image separately.
- RLE can be performed in either row-wise or column-wise order, depending on the image orientation and the desired compression ratio.
- RLE can be combined with other compression techniques, such as Huffman coding, arithmetic coding, etc., to further reduce the size of the encoded image.