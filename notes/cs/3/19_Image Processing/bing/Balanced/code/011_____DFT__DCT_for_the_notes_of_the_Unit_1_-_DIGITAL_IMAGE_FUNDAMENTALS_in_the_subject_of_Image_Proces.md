### DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- DFT stands for Discrete Fourier Transform, which is a technique for transforming a discrete signal into its frequency domain representation.
- DCT stands for Discrete Cosine Transform, which is a technique for transforming a real-valued signal into a sum of cosine functions of different frequencies.
- Both DFT and DCT are useful for image processing, as they can reveal the frequency components of an image, and allow for compression, filtering, enhancement, and other operations in the frequency domain.
- DFT and DCT have some similarities and differences, which are summarized below:

| DFT | DCT |
| --- | --- |
| Can handle complex-valued signals | Can only handle real-valued signals |
| Produces complex-valued coefficients | Produces real-valued coefficients |
| Symmetric with respect to the origin | Even with respect to the origin |
| Has both sine and cosine components | Has only cosine components |
| Better for general spectral analysis | Better for low-frequency content |
| Computed by FFT algorithm | Computed by DCT algorithm or DFT of even extension |

- DFT and DCT can be applied to images by using two-dimensional versions of the transforms, which operate on rows and columns of the image matrix.
- DFT and DCT can be used for image compression by discarding the high-frequency coefficients, which are less perceptible to the human eye, and retaining the low-frequency coefficients, which contain most of the image information.
- DFT and DCT can be used for image enhancement by applying filters in the frequency domain, such as low-pass, high-pass, band-pass, or notch filters, which can remove noise, sharpen edges, or emphasize certain features of the image.