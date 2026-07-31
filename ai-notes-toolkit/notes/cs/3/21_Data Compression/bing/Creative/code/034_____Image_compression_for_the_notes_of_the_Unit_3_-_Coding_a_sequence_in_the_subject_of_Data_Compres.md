# Image compression

Image compression is a process applied to a graphics file to minimize its size in bytes without degrading image quality below an acceptable threshold . By reducing the file size, more images can be stored in a given amount of disk or memory space. Image compression also reduces the bandwidth required to transmit or download images over the internet.

## Types of image compression

There are two main types of image compression: lossless and lossy.

- Lossless compression preserves the original image data exactly, without any loss of information. Lossless compression algorithms use techniques such as run-length encoding, Huffman coding, Lempel-Ziv-Welch (LZW) coding, and arithmetic coding to reduce the redundancy in the image data. Lossless compression is suitable for images that require high fidelity, such as medical images, text documents, and logos. Some common lossless image formats are PNG, TIFF, GIF, and BMP.

- Lossy compression discards some of the image data, resulting in some loss of quality. Lossy compression algorithms use techniques such as quantization, transform coding, and entropy coding to reduce the correlation and complexity in the image data. Lossy compression is suitable for images that can tolerate some degradation, such as natural scenes, photographs, and web graphics. Some common lossy image formats are JPEG, JPEG 2000, WebP, and HEIF.

## Factors affecting image compression

The amount of compression that can be achieved by an image compression algorithm depends on several factors, such as:

- The image format: Different image formats use different compression algorithms and have different capabilities and limitations. For example, JPEG is a lossy format that can achieve high compression ratios but may introduce artifacts such as blocking and ringing. PNG is a lossless format that can preserve the image quality but may not achieve high compression ratios.

- The image content: Different images have different characteristics and properties that affect the compression performance. For example, images with smooth regions, low contrast, and low frequency components are easier to compress than images with sharp edges, high contrast, and high frequency components.

- The image quality: The quality of an image is a subjective measure of how well the image represents the original scene or object. The quality of an image can be affected by the compression algorithm, the compression ratio, and the compression parameters. For example, increasing the compression ratio may reduce the file size but also degrade the image quality. Adjusting the compression parameters such as the bit rate, the quantization level, and the quality factor may trade off the file size and the image quality.

## Methods of image compression

There are many methods and techniques that can be used to perform image compression, such as:

- Run-length encoding (RLE): RLE is a simple lossless compression technique that replaces consecutive identical pixels with a single pixel value and a count of how many times it occurs. For example, the sequence of pixels 111111222233333 can be encoded as 16162353. RLE is effective for images with large areas of uniform color, such as cartoons and logos.

- Huffman coding: Huffman coding is a lossless compression technique that assigns variable-length codes to the pixels based on their frequency of occurrence. The more frequent pixels are assigned shorter codes and the less frequent pixels are assigned longer codes. For example, if the pixel values 0, 1, 2, and 3 occur with probabilities 0.5, 0.25, 0.125, and 0.125, respectively, they can be encoded as 0, 10, 110, and 111. Huffman coding is effective for images with non-uniform pixel distributions, such as natural scenes and photographs.

- Lempel-Ziv-Welch (LZW) coding: LZW coding is a lossless compression technique that builds a dictionary of variable-length codes for the pixels based on their patterns of occurrence. The dictionary is initialized with the basic pixel values and is updated dynamically as new patterns are encountered. For example, if the pixel values 0, 1, 2, and 3 are used, the dictionary can be initialized as {0:0, 1:1, 2:2, 3:3}. If the sequence of pixels 012301230123 is encountered, the dictionary can be updated as {0:0, 1:1, 2:2, 3:3, 01:4, 23:5, 012:6, 301:7, 230:8, 123:9} and the sequence can be