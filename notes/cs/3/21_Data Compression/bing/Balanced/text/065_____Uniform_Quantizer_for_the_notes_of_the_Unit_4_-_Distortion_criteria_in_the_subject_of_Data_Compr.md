### Uniform Quantizer

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values to a finite set of output levels with equal spacing .
- A uniform quantizer can be characterized by its step size $\Delta$, which is the distance between two adjacent output levels .
- A uniform quantizer can be classified into two types: mid-tread and mid-rise .
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero .
  - A mid-rise quantizer has no zero output level and the output levels are shifted by $\Delta/2$ from the mid-tread quantizer .
- A uniform quantizer can be used for data compression by encoding the output levels with a fixed number of bits .
- A uniform quantizer can achieve optimal performance in terms of mean squared error (MSE) when the input values are uniformly distributed .
- A uniform quantizer can be combined with a companding function to achieve non-uniform quantization, which can better match the input distribution and reduce the distortion .
  - A companding function is a nonlinear function that compresses the input values before quantization and expands them after quantization .
  - Two common companding functions are the $\mu$-law and the A-law, which are used for PCM telephone systems .
- A uniform quantizer can be incorporated into a deep learning based image compression framework, where the feature maps between the encoder and decoder are quantized .
  - A uniform quantizer can be approximated by different methods, such as rounding, stochastic rounding, additive uniform noise, or trellis coded quantization .
  - A uniform quantizer can be optimized by minimizing the rate-distortion trade-off, which balances the compression ratio and the reconstruction quality .