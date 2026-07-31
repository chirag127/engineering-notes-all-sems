### Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing .
- A uniform quantizer can be characterized by its step size Δ, which is the distance between two adjacent output levels .
- The quantization error of a uniform quantizer is the difference between the input value and the nearest output level .
- The quantization error can be reduced by increasing the number of output levels or decreasing the step size, but this also increases the bit rate of the quantized signal .
- The distortion of a uniform quantizer can be measured by the mean squared error (MSE) or the signal-to-quantization-noise ratio (SQNR), which are functions of the step size and the input signal statistics  .
- A uniform quantizer can be optimized for a given input signal by choosing the step size that minimizes the distortion or maximizes the SQNR  .
- A uniform quantizer can be combined with an entropy encoder to achieve lossy data compression, where the output levels are assigned variable-length codes based on their probabilities  .
- A uniform quantizer can also be modified by a companding function that compresses the input range before quantization and expands it after quantization, which can improve the performance for signals with non-uniform distributions .
- A uniform quantizer can be applied to image compression by quantizing the feature maps between the encoder and decoder of a deep learning model, where different approximations of the uniform quantization can affect the quality and efficiency of the compression .