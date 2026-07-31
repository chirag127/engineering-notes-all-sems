# Non uniform Quantization

Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal intervals between the output values. Non uniform quantization is more suitable for sources with non-uniform distributions of values, such as speech or image signals.

Some points to note about non uniform quantization are:

- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions where the source values are more likely to occur.
- Non uniform quantization can be implemented by using a non-linear function to map the input values to a uniform quantizer, and then applying the inverse function at the decoder. This is called companding.
- Non uniform quantization can also be optimized by adjusting the quantization points according to the network gradients, such as in neural network compression.
- Non uniform quantization can be classified into two types: scalar and vector. Scalar non uniform quantization operates on each input value independently, while vector non uniform quantization operates on a group of input values jointly.
- Non uniform quantization can be evaluated by using distortion criteria, such as mean squared error (MSE), signal to noise ratio (SNR), or perceptual quality measures.