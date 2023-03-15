### CALIC

- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a technique for compressing continuous-tone images without any loss of quality or information  .
- It achieves high compression ratios by using a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics  .
- The non-linear predictor adapts via an error feedback mechanism, which reduces the prediction error and the entropy of the residual signal  .
- The residual signal is then encoded using a binary arithmetic coder with adaptive probability estimation  .
- CALIC has relatively low time and space complexities, and can handle various types of images, such as grayscale, color, and compound images    .
- CALIC can also be extended to compress video data by using motion compensation to exploit the temporal redundancy between frames .
- CALIC is one of the most efficient lossless image coding techniques in the literature, and has been adopted as a standard by the International Organization for Standardization (ISO) and the International Telecommunication Union (ITU)  .