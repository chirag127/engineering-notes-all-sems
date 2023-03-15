# Run Length Encoding

- Run Length Encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.
- RLE is most efficient on data that contains many such runs, for example, simple graphic images such as icons, line drawings, Conway's Game of Life, and animations.
- RLE compression algorithm works as follows :
  - For each row of pixels in the image, check for the consecutive runs of the current pixel value.
  - Replace each run with a pair of numbers: the length of the run and the pixel value.
  - For example, the first row of the image below contains 3 white pixels, 2 red pixels, 5 white pixels, 2 red pixels, then 4 white pixels:

  ![image](https://www.khanacademy.org/computer-programming/heart/4739770016.png)

  - The RLE representation of this row would be: 3 0 2 1 5 0 2 1 4 0, where 0 represents white and 1 represents red.
  - Repeat this process for each row of the image and concatenate the results to get the final RLE representation of the image.
- RLE has some advantages and disadvantages:
  - Advantages:
    - It is simple and easy to implement.
    - It can achieve high compression ratios for images with large areas of uniform color or repeated patterns.
    - It preserves the original quality of the image without any loss of information.
  - Disadvantages:
    - It is not effective for images with complex details or many color variations.
    - It can increase the size of the image if there are few runs or many single pixels.
    - It does not take advantage of any spatial or frequency correlations in the image.