
### Run Length Encoding 
Run length encoding (RLE) is a simple form of data compression in which runs of data (that is, sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. RLE is used in many image file formats, such as GIF and TIFF, to reduce file size.

* RLE works by taking a sequence of characters and replacing each run of the same character with a count and the character.
* For example, the sequence `AAAABBBCCDAA` would become `4A3B2C1D2A`.
* This reduces the file size significantly, as the same characters are represented with fewer bytes.
* RLE can be used to compress both text and image data.
* For text files, RLE works by replacing repeated characters with the character and a count.
* For image files, RLE works by replacing runs of pixels with the color of the run and a count.
* RLE is effective for data with long runs of the same value, such as images with large areas of a single color.
* RLE is not effective for data with a high degree of randomness, such as audio or video data.