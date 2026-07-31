# Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing.
- A uniform quantizer can be characterized by its step size Δ, which is the distance between two adjacent output levels.
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero.
  - A mid-rise quantizer has a non-zero output level at the origin and the output levels are asymmetric around zero.
- A uniform quantizer can be combined with a companding technique to achieve non-uniform quantization, which can reduce the distortion for signals with non-uniform probability distribution.
  - A companding technique is a process of compressing the input signal before quantization and expanding the output signal after quantization.
  - Two common companding techniques are µ-law and A-law, which are used for PCM telephone systems.
    - µ-law companding has a mid-tread characteristic and is more suitable for signals with a large dynamic range.
    - A-law companding has a mid-rise characteristic and is more suitable for signals with a small dynamic range.
- A uniform quantizer can be applied to image compression by quantizing the feature maps between the encoder and decoder of a deep learning model.
  - A uniform quantizer can be approximated by different methods, such as rounding, stochastic rounding, additive uniform noise, or trellis coded quantization .
  - A uniform quantizer can be optimized by minimizing the rate-distortion trade-off, which is a measure of the compression efficiency and quality .
- A uniform quantizer can be analyzed by using the high-rate regime, which assumes that the input signal has a smooth probability density function and the quantization intervals are nearly flat.
  - A uniform quantizer can be evaluated by using the mean squared error (MSE) or the signal-to-noise ratio (SNR) as the distortion metrics.
  - A uniform quantizer can be compared with the optimal quantizer, which minimizes the distortion for a given number of output levels.
  - A uniform quantizer can be shown to achieve a performance that is very close to the optimal quantizer at high bit rates .