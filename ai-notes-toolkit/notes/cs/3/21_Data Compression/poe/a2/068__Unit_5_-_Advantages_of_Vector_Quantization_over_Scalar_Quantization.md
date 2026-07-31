 Here is the formal content written in Markdown format without any emojis or external links:

## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

1. Better Reconstruction: Vector Quantization provides better reconstruction of the original signal as compared to Scalar Quantization. In Vector Quantization, the input signal is divided into vectors and each vector is quantized independently. This leads to lesser distortion and better reconstruction.

2. Higher Compression: Vector Quantization provides higher data compression as compared to Scalar Quantization. In Vector Quantization, the codebook contains a fixed set of vectors and the input signal is represented by the index of the closest vector in the codebook. This index contains lesser bits than the original input vector, thereby providing higher compression.

3. Graceful Degradation: Vector Quantization provides graceful degradation, i.e. the distortion increases gradually with decreasing bitrate. In Scalar Quantization, the distortion increases abruptly with decreasing bitrate which is undesirable. In Vector Quantization, as the bitrate decreases, lesser number of vectors are used from the codebook, thereby providing gradual increase in distortion.

4. Suitable for Memoryless Sources: Vector Quantization is more suitable for memoryless sources like Gaussian sources compared to Scalar Quantization. This is because Vector Quantization does not exploit the correlation between samples, so it is more suitable for uncorrelated data like memoryless sources. Scalar Quantization, on the other hand, provides higher compression for correlated data by exploiting the correlation between samples.