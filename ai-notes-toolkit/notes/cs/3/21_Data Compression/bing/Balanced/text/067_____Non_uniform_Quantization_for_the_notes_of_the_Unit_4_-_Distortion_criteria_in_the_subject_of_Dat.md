### Non uniform Quantization

- Non uniform quantization is a generalization of uniform quantization, where the quantization points are not distributed evenly  .
- Non uniform quantization can be optimized via the back-propagation of the network gradients, which makes it more expressive to approximate the original full-precision network compared to uniform quantization .
- Non uniform quantization can be applied to sources with an arbitrary distribution of values, such as speech signals, images, or neural networks  .
- Non uniform quantization can be classified into two types: companding and adaptive .
  - Companding is a technique that applies a nonlinear function to the input signal before quantizing it uniformly. The nonlinear function compresses the high-amplitude values and expands the low-amplitude values, resulting in a more uniform distribution of the quantization error .
  - Adaptive is a technique that adjusts the quantization intervals according to the statistics of the input signal. The quantization intervals are made smaller for regions with high probability density and larger for regions with low probability density, resulting in a lower average quantization error .
- Non uniform quantization can reduce the distortion and improve the signal-to-quantization-noise ratio (SQNR) compared to uniform quantization, especially for low-bit quantization   .