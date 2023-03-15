### Lossy Compression

- Lossy compression is a class of data compression methods that uses inexact approximations and partial data discarding to represent the content.
- Lossy compression is most commonly used to compress multimedia data (audio, video, and images), especially in applications such as streaming media and internet telephony.
- Lossy compression reduces the data size for storing, handling, and transmitting content, but at the cost of losing some data permanently and degrading the quality of the content.
- There are two basic lossy compression schemes:
  - In lossy transform codecs, samples of picture or sound are taken, chopped into small segments, transformed into a new basis space, and quantized. The resulting quantized values are then entropy coded.
  - In lossy predictive codecs, previous and/or subsequent decoded data is used to predict the current sound sample or image frame. The error between the predicted data and the real data, together with an extra signal parameter, is quantized and coded.
- Lossy compression has some advantages and disadvantages:
  - Advantages:
    - Smaller file size and faster transmission
    - Suitable for web applications and streaming media
    - Can achieve high compression ratios with acceptable quality
  - Disadvantages:
    - Loss of detail and nuance in the content
    - Irretrievable data loss and no option to restore the original quality
    - File limitations and compatibility issues with some formats and devices