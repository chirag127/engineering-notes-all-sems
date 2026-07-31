# Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing.
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels.
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero.
  - A mid-rise quantizer has a non-zero output level at the origin and the output levels are asymmetric around zero.
- A uniform quantizer can be used for data compression by applying a companding technique, which is a nonlinear mapping of the input values to reduce the dynamic range before quantization.
  - Two common companding techniques are $\mu$-law and A-law, which are used for PCM telephone systems.
  - $\mu$-law companding compresses the input values more at higher amplitudes and less at lower amplitudes.
  - A-law companding compresses the input values more uniformly across the range.
- A uniform quantizer can also be used for deep image compression, where the feature maps between the encoder and decoder are quantized to reduce the bit rate .
  - Different approximations of the uniform quantizer can affect the performance and complexity of the deep image compression model .
  - Some examples of uniform quantizer approximations are scalar quantizer (SQ), trellis coded quantizer (TCQ), vector quantizer (VQ), and product quantizer (PQ) .
- A uniform quantizer can be analyzed in terms of its distortion, rate, and efficiency .
  - The distortion of a uniform quantizer is the mean squared error (MSE) between the input and output values .
  - The rate of a uniform quantizer is the number of bits per sample required to represent the output levels .
  - The efficiency of a uniform quantizer is the ratio of the rate to the entropy of the input source .
  - The performance of a uniform quantizer can be improved by increasing the rate or decreasing the distortion .
  - The optimal performance of a uniform quantizer can be achieved at high rates, where the distortion is minimized and the efficiency is maximized .