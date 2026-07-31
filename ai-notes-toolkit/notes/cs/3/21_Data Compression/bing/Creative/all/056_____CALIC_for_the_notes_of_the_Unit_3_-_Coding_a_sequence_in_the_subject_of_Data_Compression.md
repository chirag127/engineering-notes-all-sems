# CALIC for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a codec that obtains higher lossless compression of continuous-tone images than other lossless image coding techniques in the literature  .
- It has relatively low time and space complexities  .
- It can also be used to compress compound video with motion compensation.
- It puts heavy emphasis on image data modeling  .
- It uses a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics .
- The non-linear predictor adapts via an error feedback mechanism .
- It uses a binary arithmetic coder to encode the prediction residuals .
- It has a feedback loop that updates the context models based on the coding results .
- It has a special mode for coding smooth areas and edges .
- It has a high compression ratio and a low distortion rate .