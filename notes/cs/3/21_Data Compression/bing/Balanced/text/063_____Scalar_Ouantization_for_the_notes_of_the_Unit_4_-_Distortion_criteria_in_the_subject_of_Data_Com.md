### Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of symbols, called quantization levels or reconstruction values .
- Scalar quantization is one of the simplest and most general ideas in lossy compression, as it reduces the precision of the signal representation and introduces quantization error or distortion.
- Scalar quantization can be performed on signal samples one at a time, or on blocks of samples, depending on the application and the desired trade-off between complexity and performance .
- Scalar quantization can be classified into two types: uniform and nonuniform .
  - Uniform scalar quantization uses equal-sized intervals or bins to partition the signal range, and assigns a fixed reconstruction value to each bin .
  - Nonuniform scalar quantization uses variable-sized intervals or bins to partition the signal range, and assigns a reconstruction value to each bin based on some criterion, such as minimizing the mean squared error or maximizing the entropy .
- Scalar quantization can be further divided into two categories: midtread and midrise .
  - Midtread scalar quantization uses a zero bin that contains the origin, and assigns a zero reconstruction value to it .
  - Midrise scalar quantization uses a half bin that contains the origin, and assigns a nonzero reconstruction value to it .
- Scalar quantization can be optimized by using techniques such as Lloyd-Max algorithm, companding, dead-zone quantization, and adaptive quantization .
- Scalar quantization can be applied to various types of signals, such as speech, audio, image, and video, and can be combined with other compression methods, such as transform coding, differential coding, and entropy coding  .
- Scalar quantization is not optimal for signals that have correlation or dependence among samples, as it does not exploit the statistical properties of the signal . A better alternative is vector quantization, which quantizes blocks of samples as a whole.