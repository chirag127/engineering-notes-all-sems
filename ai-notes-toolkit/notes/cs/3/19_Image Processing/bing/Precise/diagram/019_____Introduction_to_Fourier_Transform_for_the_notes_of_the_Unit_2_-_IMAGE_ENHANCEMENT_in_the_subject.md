### Introduction to Fourier Transform

Fourier Transform is a mathematical tool used to decompose an image into its sine and cosine components. It is a way to represent an image in the frequency domain, which can be useful for image enhancement and other image processing tasks.

1. The Fourier Transform of an image is computed by taking the 2D Discrete Fourier Transform (DFT) of the image.
2. The DFT is defined as: F(u,v) = sum(sum(f(x,y) * exp(-j * 2 * pi * (u * x / M + v * y / N)), x=0 to M-1), y=0 to N-1), where M and N are the dimensions of the image, and f(x,y) is the pixel value at location (x,y).
3. The magnitude of the Fourier Transform represents the amount of a particular frequency present in the image, while the phase represents the location of that frequency.
4. The Fourier Transform can be used for image enhancement by manipulating the magnitude and/or phase of the transform before taking the inverse transform to obtain the enhanced image.
5. Common image enhancement techniques using the Fourier Transform include high-pass filtering, low-pass filtering, and band-pass filtering.

This is a brief introduction to the Fourier Transform and its use in image enhancement. Further study is recommended to fully understand the concepts and techniques involved.