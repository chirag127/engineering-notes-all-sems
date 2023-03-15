# CALIC for Data Compression

CALIC stands for Context-Based, Adaptive, Lossless Image Coding, and is an image codec that is made for obtaining a high degree of compression for continuous-tone gray-scaled images. It uses a single pass and self-correcting GAP (gradient adjusted predictor) to compress image efficiently and with a high compression ratio.

Some of the main features of CALIC are  :

- It puts heavy emphasis on image data modeling and adapts to varying source statistics.
- It uses a large number of modeling contexts to condition a non-linear predictor and make it adaptive to varying source statistics.
- The non-linear predictor adapts via an error feedback mechanism.
- It uses a bias cancellation technique to remove the systematic prediction errors in each context.
- It uses a Golomb-Rice code to encode the residuals with a context-dependent parameter.

The basic steps of the CALIC algorithm are:

1. Find the initial prediction using the GAP method based on the neighboring pixels.
2. Compute the prediction context based on the local image features and the prediction error of the previous pixel.
3. Refine the prediction by removing the estimate of the bias in that context.
4. Update the bias estimate based on the current prediction error.
5. Obtain the residual and remap it so the residual values lie between 0 and M, where M is the size of the initial alphabet.
6. Encode the residual using a Golomb-Rice code with a context-dependent parameter.

The following diagram illustrates the CALIC encoder and decoder:
