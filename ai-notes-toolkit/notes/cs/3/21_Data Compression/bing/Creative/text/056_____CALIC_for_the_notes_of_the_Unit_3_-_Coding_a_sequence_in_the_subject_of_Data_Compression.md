### CALIC

- CALIC stands for **Context-based, Adaptive, Lossless Image Coding**  .
- It is a technique for compressing continuous-tone images without any loss of quality or information  .
- It achieves high coding efficiency with relatively low time and space complexities  .
- It can also be applied to compress compound video data, which consists of both text and graphics.
- The main components of CALIC are  :
  - A **non-linear predictor** that estimates the pixel value based on its neighboring pixels and their contexts.
  - A **context modeler** that assigns a probability distribution to the prediction error based on the local image features and the previous errors.
  - A **binary arithmetic coder** that encodes the prediction error using the probability distribution from the context modeler.
- The non-linear predictor and the context modeler are adaptive, meaning they adjust their parameters according to the image data and the prediction errors  .
- The non-linear predictor uses a **gradient-adjusted prediction (GAP)** scheme, which considers the gradients of the neighboring pixels to improve the accuracy of the prediction  .
- The context modeler uses a **large number of modeling contexts** to capture the local image features and the error feedback mechanism  .
- The binary arithmetic coder uses a **binary tree structure** to encode the prediction error in a bit-by-bit fashion, starting from the most significant bit  .
- The coding sequence of CALIC is as follows  :
  - For each pixel in the image, apply the non-linear predictor to obtain the predicted value and the prediction error.
  - For each prediction error, apply the context modeler to obtain the probability distribution and the modeling context.
  - For each prediction error, apply the binary arithmetic coder to obtain the encoded bits using the probability distribution and the modeling context.
  - Concatenate the encoded bits to form the compressed bitstream.