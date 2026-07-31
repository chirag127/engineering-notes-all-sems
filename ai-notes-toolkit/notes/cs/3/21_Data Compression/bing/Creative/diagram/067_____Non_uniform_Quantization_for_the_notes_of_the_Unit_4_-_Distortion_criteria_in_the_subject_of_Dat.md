### Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal intervals.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely than others.
- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions where the input values are more probable and less bits to the regions where the input values are less probable.
- Non uniform quantization can be implemented in different ways, such as:
  - Using a non-linear function to map the input values to the output values, such as the logarithmic function or the companding function.
  - Using an adaptive quantizer that changes the quantization intervals according to the statistics of the input signal.
  - Using an optimal quantizer that minimizes a distortion criterion, such as the mean squared error or the entropy, by adjusting the quantization intervals and levels.
  - Using a trainable quantizer that learns the quantization parameters from the data, such as the network gradients, by using back-propagation or other optimization methods .
- Non uniform quantization has some advantages and disadvantages, such as:
  - Advantages:
    - It can reduce the quantization noise and improve the signal-to-noise ratio.
    - It can preserve more information and details of the input signal.
    - It can be more expressive and flexible to approximate the original signal.
  - Disadvantages:
    - It can be more complex and computationally expensive than uniform quantization.
    - It can require more information to encode and decode the output values, such as the quantization parameters or the non-linear function.
    - It can introduce more distortion and error in the projection process, especially for nonuniformly quantized weights in neural networks.