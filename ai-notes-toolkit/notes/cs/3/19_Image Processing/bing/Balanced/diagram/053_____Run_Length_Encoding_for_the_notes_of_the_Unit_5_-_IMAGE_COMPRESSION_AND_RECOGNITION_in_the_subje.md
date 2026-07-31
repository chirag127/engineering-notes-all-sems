### Run Length Encoding

- Run Length Encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.
- RLE is most efficient on data that contains many such runs, for example, simple graphic images such as icons, line drawings, Conway's Game of Life, and animations.
- RLE compression algorithm works as follows :
  - For each row of pixels in the image, check for the consecutive runs of the current pixel value.
  - Replace each run with a pair of numbers: the length of the run and the pixel value.
  - For example, the first row of the image below contains 3 white pixels, 2 red pixels, 5 white pixels, 2 red pixels, then 4 white pixels:

  ```
  WWWRRWWWWWRRWWWW
  ```

  - The RLE compressed representation of this row would be:

  ```
  3W2R5W2R4W
  ```

  - The compressed representation is shorter than the original row, and the compression ratio is the ratio of the lengths of the original and compressed data. In this case, the compression ratio is 16/10 = 1.6.
  - The compression ratio depends on the image and the number of runs. For binary images (images with only two colors), the compression ratio can be as high as 8, but for images with many colors and variations, the compression ratio can be less than 1, meaning that the compressed data is larger than the original data.
  - To decompress the data, the algorithm simply reads each pair of numbers and repeats the pixel value for the specified length.

- RLE is a simple and fast compression algorithm, but it has some limitations :
  - It is not suitable for images with high resolution, complex details, or many colors, as these images would have few runs and low compression ratios.
  - It is sensitive to noise and small changes in the image, as these would create more runs and reduce the compression ratio.
  - It does not exploit any spatial or frequency redundancy in the image, as it only considers one row at a time.
  - It does not provide any compression for data that does not have runs, such as text or random numbers.