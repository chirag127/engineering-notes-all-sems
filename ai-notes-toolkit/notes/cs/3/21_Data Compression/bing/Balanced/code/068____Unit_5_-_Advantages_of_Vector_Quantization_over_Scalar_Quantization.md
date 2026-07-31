## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Vector quantization (VQ) is a technique for compressing data by representing a large set of vectors (such as image pixels or speech samples) by a smaller set of code vectors (or codebook).
- Scalar quantization (SQ) is a simpler technique that compresses data by representing each individual value (such as a pixel intensity or a speech amplitude) by a discrete level (or codeword).
- VQ has several advantages over SQ, such as:

  - VQ can achieve higher compression ratios than SQ, since it exploits the correlation and redundancy among the data vectors, while SQ treats each value independently.
  - VQ can preserve the quality of the data better than SQ, since it minimizes the distortion (or error) between the original and the reconstructed vectors, while SQ introduces quantization noise (or error) for each value.
  - VQ can adapt to the statistics and characteristics of the data better than SQ, since it can design the codebook based on the distribution and variation of the data vectors, while SQ uses a fixed and uniform quantization scheme for all values.
  - VQ can handle non-linear and complex data better than SQ, since it can approximate the data vectors by non-uniform and non-rectangular regions (or cells), while SQ can only partition the data values by uniform and rectangular intervals (or bins).