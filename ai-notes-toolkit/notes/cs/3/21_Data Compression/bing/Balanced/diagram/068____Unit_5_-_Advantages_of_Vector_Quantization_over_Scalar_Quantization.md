## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique that compresses data by representing a set of similar vectors (such as image blocks or speech frames) by a single representative vector called a codevector.
- Scalar quantization (SQ) is a technique that compresses data by representing each individual sample (such as a pixel or a waveform amplitude) by a discrete value called a codeword.
- VQ has several advantages over SQ, such as:

  - VQ can achieve higher compression ratios than SQ by exploiting the correlation among the samples in a vector. SQ treats each sample independently and ignores the correlation.
  - VQ can reduce the quantization noise and distortion by minimizing the mean squared error (MSE) between the original and the reconstructed vectors. SQ minimizes the MSE between the original and the reconstructed samples, which may not reflect the perceptual quality of the data.
  - VQ can adapt to the statistics and characteristics of the data by using different codebooks for different regions or classes of vectors. SQ uses a fixed quantizer for the entire data, which may not be optimal for all samples.
  - VQ can perform rate-distortion optimization by varying the size and shape of the codevectors according to the desired bit rate and distortion level. SQ has a fixed relationship between the bit rate and the distortion, which may not match the user's requirements.

- An example of VQ and SQ applied to image compression is shown below:

  - The original image is divided into 4x4 blocks of pixels, each of which is a 16-dimensional vector.
  - VQ uses a codebook of 256 codevectors, each of which is also a 16-dimensional vector. Each block is assigned to the nearest codevector in terms of Euclidean distance. The index of the codevector is encoded using 8 bits. The reconstructed image is obtained by replacing each block with its corresponding codevector.
  - SQ uses a uniform quantizer with 256 levels, each of which is a scalar value. Each pixel is assigned to the nearest level in terms of absolute difference. The index of the level is encoded using 8 bits. The reconstructed image is obtained by replacing each pixel with its corresponding level.

  - The original image, the VQ-compressed image, and the SQ-compressed image are shown below:

  ```
  | Original image | VQ-compressed image | SQ-compressed image |
  |:--------------:|:-------------------:|:-------------------:|
  | ![Original image](original.png) | ![VQ-compressed image](vq.png) | ![SQ-compressed image](sq.png) |
  ```

  - The VQ-compressed image has a higher visual quality than the SQ-compressed image, as it preserves the edges and textures better. The SQ-compressed image has more artifacts and noise, as it introduces more quantization errors. The VQ-compressed image and the SQ-compressed image have the same bit rate of 8 bits per pixel, but the VQ-compressed image has a lower MSE of 18.7 than the SQ-compressed image, which has an MSE of 28.4.