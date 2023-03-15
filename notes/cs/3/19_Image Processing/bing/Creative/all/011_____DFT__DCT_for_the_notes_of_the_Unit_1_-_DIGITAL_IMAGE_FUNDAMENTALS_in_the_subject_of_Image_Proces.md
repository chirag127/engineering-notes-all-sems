# DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- DFT stands for Discrete Fourier Transform, which is a technique for transforming a discrete signal into its frequency domain representation.
- DCT stands for Discrete Cosine Transform, which is a technique for transforming a real-valued signal into a sum of cosine functions of different frequencies.
- Both DFT and DCT are useful for image processing, as they can reveal the frequency components of an image and allow for compression, filtering, enhancement, etc.
- DFT and DCT have some similarities and differences, which are summarized below:

## Similarities

- Both DFT and DCT are linear transformations, meaning that they preserve the superposition principle and can be represented by matrices.
- Both DFT and DCT are invertible, meaning that they can be reversed to recover the original signal from the transformed one.
- Both DFT and DCT are orthogonal, meaning that the basis functions (complex exponentials for DFT, cosines for DCT) are mutually independent and have unit norm.
- Both DFT and DCT are periodic, meaning that they can be applied to finite-length signals by assuming that they are repeated infinitely.

## Differences

- DFT can handle complex-valued signals, while DCT can only handle real-valued signals.
- DFT produces complex-valued coefficients, while DCT produces real-valued coefficients.
- DFT has both positive and negative frequency components, while DCT has only positive frequency components.
- DFT is symmetric with respect to the origin, while DCT is symmetric with respect to the half-period.
- DFT has a higher computational complexity than DCT, as it requires complex arithmetic and more operations.
- DCT is more suitable for signals that have low frequency content and even symmetry, such as speech or image signals, as it can achieve better compression and energy compaction. DFT is more suitable for general spectral analysis and frequency domain processing, as it can capture all the frequency information and map it to physical frequencies more easily.

## Examples

- To compute the DFT of an N-point signal x[n], we can use the formula:

  X[k] = sum_{n=0}^{N-1} x[n] exp(-j 2 pi k n / N), for k = 0, 1, ..., N-1

  where X[k] is the k-th DFT coefficient, j is the imaginary unit, and exp is the exponential function.

- To compute the DCT of an N-point signal x[n], we can use the formula:

  X[k] = alpha(k) sum_{n=0}^{N-1} x[n] cos(pi k (n + 1/2) / N), for k = 0, 1, ..., N-1

  where X[k] is the k-th DCT coefficient, alpha(k) is a scaling factor given by:

  alpha(k) = sqrt(1/N), if k = 0
  alpha(k) = sqrt(2/N), if k > 0

  and cos is the cosine function.

- To compute the DFT of an image, we can use the function dct2 in MATLAB, which uses an FFT-based algorithm for fast computation. For example, if I is a grayscale image, we can write:

  F = dct2(I);

  where F is the DFT of the image.

- To compute the DCT of an image, we can use the function dctmtx in MATLAB, which returns the DCT transform matrix, and then multiply it with the image. For example, if I is a grayscale image, we can write:

  D = dctmtx(size(I,1)); % DCT matrix for rows
  E = dctmtx(size(I,2)); % DCT matrix for columns
  F = D * I * E'; % DCT of the image

  where F is the DCT of the image.