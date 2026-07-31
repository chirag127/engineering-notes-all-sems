# Run Length Encoding

Run length encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.

- RLE is most efficient on data that contains many such runs, for example, simple graphic images such as icons, line drawings, Conway's Game of Life, and animations.
- RLE works best on binary images, where each pixel can be either black or white.
- RLE compression algorithm:
  - In RLE, the computer replaces each row with numbers that say how many consecutive pixels are the same color, always starting with the number of white pixels.
  - For example, the first row of the following image contains 3 white pixels, 2 red pixels, 5 white pixels, 2 red pixels, then 4 white pixels:

  ```
  | | | |R|R| | | | | | |R|R| | | |
  | | |R|R|R|R|R| | | |R|R|R|R| | |
  | |R|R|R|R|R|R|R| |R|R|R|R|R|R| |
  |R|R|R|R|R|R|R|R|R|R|R|R|R|R|R|R|
  |R|R|R|R|R|R|R|R|R|R|R|R|R|R|R|R|
  | |R|R|R|R|R|R|R| |R|R|R|R|R|R| |
  | | |R|R|R|R|R| | | |R|R|R|R| | |
  | | | |R|R| | | | | | |R|R| | | |
  ```

  - The RLE representation of the first row would be: 3 2 5 2 4
  - The RLE representation of the whole image would be: 3 2 5 2 4 3 4 1 4 4 2 4 2 2 6 2 6 2 2 8 2 8 2 16 16 2 8 2 8 2 2 6 2 6 2 3 4 1 4 4 2 4 2 3 2 5 2 4
  - The RLE representation is much shorter than the original image, which would require 256 bits to store each pixel as black or white. The RLE representation only requires 64 bits, which is a compression ratio of 4:1.
- RLE advantages and disadvantages:
  - RLE is simple and easy to implement.
  - RLE can achieve high compression ratios for images with large areas of uniform color.
  - RLE is not suitable for images with complex patterns or many colors, as it would result in long runs of different values and little or no compression.
  - RLE is not adaptive, meaning it does not adjust to the characteristics of the data.