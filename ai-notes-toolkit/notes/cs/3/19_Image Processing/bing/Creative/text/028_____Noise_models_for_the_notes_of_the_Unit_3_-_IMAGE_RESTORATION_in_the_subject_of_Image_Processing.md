### Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Noise is unwanted information in digital images that degrades the quality and clarity of the image .
- Noise can be introduced during image acquisition, coding, transmission, and processing steps   .
- Noise can produce undesirable effects such as artifacts, unrealistic edges, unseen lines, corners, blurred objects and disturbs background scenes.
- To reduce these undesirable effects, prior knowledge of noise models is essential for further processing  .
- Noise models describe the statistical properties of noise and how it affects the image pixels.
- Some common noise models are:
  - Gaussian noise: This noise model assumes that the noise follows a normal or Gaussian distribution with a mean of zero and a standard deviation of sigma. This noise model is suitable for modeling thermal noise or sensor noise .
  - Salt-and-pepper noise: This noise model assumes that the noise is either very high (white) or very low (black) with a certain probability, and unaffected otherwise. This noise model is suitable for modeling transmission errors or faulty pixels.
  - Poisson noise: This noise model assumes that the noise follows a Poisson distribution, which depends on the intensity of the image. This noise model is suitable for modeling photon counting noise or low-light conditions .
  - Speckle noise: This noise model assumes that the noise is multiplicative, meaning that it is proportional to the image intensity. This noise model is suitable for modeling coherent imaging systems such as ultrasound or radar.
  - Uniform noise: This noise model assumes that the noise is uniformly distributed over a certain range. This noise model is suitable for modeling quantization noise or analog-to-digital conversion noise.