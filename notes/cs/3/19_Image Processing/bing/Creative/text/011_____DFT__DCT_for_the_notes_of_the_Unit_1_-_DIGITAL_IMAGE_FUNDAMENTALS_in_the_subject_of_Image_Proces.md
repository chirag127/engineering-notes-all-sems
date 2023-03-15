### DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- DFT stands for Discrete Fourier Transform, which is a technique for transforming a discrete signal into its frequency domain representation.
- DCT stands for Discrete Cosine Transform, which is a technique for transforming a real-valued discrete signal into its frequency domain representation using only cosine functions.
- Both DFT and DCT are useful for image processing, as they can reveal the frequency components of an image, which can be used for filtering, compression, enhancement, etc.
- DFT and DCT have some similarities and differences, which are summarized below:

| DFT | DCT |
| --- | --- |
| Can handle complex-valued signals | Can only handle real-valued signals |
| Uses both sine and cosine functions | Uses only cosine functions |
| Symmetric about the origin | Even about the origin |
| Has both real and imaginary parts | Has only real parts |
| Can represent both low and high frequency components | Emphasizes low frequency components |
| Better for general spectral analysis | Better for image and speech coding |

- DFT can be computed using the Fast Fourier Transform (FFT) algorithm, which reduces the computational complexity from O(N^2) to O(N log N), where N is the number of samples in the signal.
- DCT can be computed using the DFT of an even extension of the signal, or using a DCT transform matrix, which is a precomputed matrix that can be multiplied with the signal vector to obtain the DCT coefficients.
- DCT has several variants, such as DCT-I, DCT-II, DCT-III, and DCT-IV, which differ in the boundary conditions and the scaling factors. DCT-II is the most commonly used variant in image processing, as it is the basis of the JPEG compression standard.