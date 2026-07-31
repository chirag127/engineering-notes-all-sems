### Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of values, called quantization levels or reproduction points .
- Scalar quantization can be used to reduce the bit rate of a signal by encoding each sample with a fixed number of bits, based on its quantization level.
- Scalar quantization can introduce distortion or error in the signal, as the quantized value may not be exactly equal to the original value.
- The performance of scalar quantization depends on the design of the quantizer, which includes the number of quantization levels, the spacing of the levels, and the mapping rule from the input to the output.
- The quantizer can be uniform or nonuniform, depending on whether the quantization levels are equally spaced or not. Uniform quantizers are simpler to implement, but may not be optimal for signals that have nonuniform probability distributions .
- The quantizer can be midtread or midrise, depending on whether the quantization levels include zero or not. Midtread quantizers have better performance for signals that have zero mean, while midrise quantizers have better performance for signals that have nonzero mean .
- The quantizer can be deterministic or stochastic, depending on whether the mapping rule is fixed or random. Deterministic quantizers are more predictable, but may introduce periodic errors or granular noise. Stochastic quantizers are less predictable, but may reduce the errors or noise by introducing dither or randomization .
- The distortion or error of scalar quantization can be measured by different criteria, such as mean squared error (MSE), signal-to-noise ratio (SNR), peak signal-to-noise ratio (PSNR), or perceptual quality. The optimal quantizer design depends on the distortion criterion and the signal characteristics .
- Scalar quantization can be applied to various types of signals, such as audio, image, or video. However, scalar quantization may not be efficient or effective for signals that have high correlation or dependency among the samples. In such cases, vector quantization or transform coding may be more suitable  .

: Scalar Quantization - an overview | ScienceDirect Topics
: Scalar Quantization - Introduction to Data Compression, 4th Edition [Book]
: Scalar Quantizer - an overview | ScienceDirect Topics
: The Wavelet /Scalar Quantization Compression Standard for ... - NIST
: Scalar Quantization - an overview | ScienceDirect Topics