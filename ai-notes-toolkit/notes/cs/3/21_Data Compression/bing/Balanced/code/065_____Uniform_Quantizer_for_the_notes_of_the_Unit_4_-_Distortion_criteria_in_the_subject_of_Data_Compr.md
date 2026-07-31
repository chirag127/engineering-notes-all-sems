### Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing.
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels, and its number of output levels $M$, which is usually a power of two.
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero. It is suitable for signals with zero mean and symmetric distribution.
  - A mid-rise quantizer has a non-zero output level at the origin and the output levels are asymmetric around zero. It is suitable for signals with non-zero mean and asymmetric distribution.
- A uniform quantizer can be combined with a companding function to achieve non-uniform quantization, which can reduce the quantization noise for signals with non-uniform distribution.
  - A companding function is a nonlinear function that compresses the input signal before quantization and expands the output signal after quantization.
  - Two common companding functions are the $\mu$-law and the A-law, which are used for PCM telephone systems.
- A uniform quantizer can be applied to image compression by quantizing the feature maps between the encoder and decoder of a deep learning model.
  - A uniform quantizer can be approximated by different methods, such as rounding, stochastic rounding, additive uniform noise, or trellis coded quantization .
  - A uniform quantizer can be optimized by minimizing the distortion or the rate-distortion trade-off of the image compression model .
- A uniform quantizer can be analyzed by using the high-rate or the low-rate regime, depending on the number of output levels or the bit rate .
  - In the high-rate regime, the quantization noise can be modeled as a uniform distribution and the distortion can be approximated by the mean squared error .
  - In the low-rate regime, the quantization noise can be modeled as a Laplacian distribution and the distortion can be approximated by the mean absolute error .