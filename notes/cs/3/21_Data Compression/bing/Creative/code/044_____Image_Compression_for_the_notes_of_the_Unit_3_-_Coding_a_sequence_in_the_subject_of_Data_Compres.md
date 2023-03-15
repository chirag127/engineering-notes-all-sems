### Image Compression

Image compression is the process of reducing the size of an image file without compromising its quality or visual appearance. Image compression is useful for saving storage space, bandwidth, and transmission time, as well as for enhancing the performance of applications that use images.

Image compression techniques can be classified into two categories: lossless and lossy.

- Lossless compression techniques preserve the exact information of the original image, and allow the original image to be reconstructed from the compressed data without any loss of quality. Lossless compression techniques are suitable for images that require high fidelity, such as medical images, text documents, or icons.

- Lossy compression techniques discard some information of the original image, and allow the compressed data to be reconstructed into an approximation of the original image with some loss of quality. Lossy compression techniques are suitable for images that can tolerate some degradation, such as natural images, photographs, or web graphics.

Some of the common methods of image compression are:

- Deflate: The Deflate method is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. The LZ77 algorithm identifies and eliminates repeated sequences of pixels, while the Huffman coding assigns variable-length codes to the remaining pixels based on their frequency of occurrence. The Deflate method is used in formats such as PNG, GIF, and ZIP.

- Run-length encoding (RLE): Run-length encoding is a lossless image compression technique that is used to reduce the size of an image by encoding sequences of repeated pixels. For example, a sequence of 10 white pixels can be encoded as (10, white) instead of writing white 10 times. RLE is effective for images that have large areas of uniform color, such as cartoons or logos .

- Arithmetic coding: Arithmetic coding is a lossless image compression technique that assigns variable-length codes to the pixels based on their probability of occurrence. Unlike Huffman coding, which assigns codes to individual pixels, arithmetic coding assigns codes to entire sequences of pixels, resulting in higher compression ratios. Arithmetic coding is used in formats such as JPEG 2000 and JPEG XR.

- Transform coding: Transform coding is a lossy image compression technique that uses mathematical transformations to reduce the size of an image and commonly used for JPEGs. The idea behind transform coding is to convert the image data into a different representation that is more compact, making it easier to compress. One of the most widely used forms of transform coding is the discrete cosine transform (DCT), which converts the image data into a sum of cosine functions of different frequencies. The DCT coefficients that correspond to high frequencies are usually discarded or quantized, as they are less perceptible to the human eye. The remaining coefficients are then encoded using Huffman coding or arithmetic coding  .

- Other methods: There are many other methods of image compression, such as wavelet coding, fractal coding, vector quantization, and neural network coding, that use different techniques to exploit the properties of images and achieve high compression ratios. However, these methods are beyond the scope of this note.