### Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of values, called quantization levels or reproduction points .
- Scalar quantization is one of the simplest and most general ideas in lossy compression, as it reduces the number of bits required to represent a signal by discarding some information.
- Scalar quantization can be performed by dividing the range of the signal into intervals, called quantization cells or bins, and assigning a quantization level to each cell .
- The quantization function Q(⋅) maps each input value x to the quantization level Q(x) that corresponds to the cell that contains x.
- The quantization error e(x) is the difference between the input value x and the quantization level Q(x), and it represents the amount of information lost due to quantization .
- The quantization error can be measured by various distortion criteria, such as mean squared error (MSE), signal-to-noise ratio (SNR), peak signal-to-noise ratio (PSNR), or perceptual quality .
- The goal of scalar quantization is to minimize the quantization error for a given number of bits per sample, or equivalently, to maximize the compression ratio for a given distortion level .
- Scalar quantization can be classified into two types: uniform and nonuniform .
  - Uniform scalar quantization uses equal-sized cells and equally spaced quantization levels, and it is suitable for signals that have a uniform distribution .
  - Nonuniform scalar quantization uses variable-sized cells and unequally spaced quantization levels, and it is suitable for signals that have a nonuniform distribution, such as Laplacian or Gaussian .
- Scalar quantization can be further improved by using techniques such as companding, entropy coding, or adaptive quantization .
- Scalar quantization is widely used in various applications, such as speech and audio coding, image and video compression, and fingerprint recognition .