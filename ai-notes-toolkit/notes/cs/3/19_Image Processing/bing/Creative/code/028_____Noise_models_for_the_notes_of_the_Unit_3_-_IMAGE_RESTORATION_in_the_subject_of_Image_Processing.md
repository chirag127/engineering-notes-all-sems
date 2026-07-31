### Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Noise is unwanted information in digital images that degrades the quality and clarity of the image .
- Noise can be introduced during image acquisition, coding, transmission, and processing steps   .
- Noise can produce undesirable effects such as artifacts, unrealistic edges, unseen lines, corners, blurred objects and disturbs background scenes.
- To reduce these undesirable effects, prior knowledge of noise models is essential for further processing  .
- Noise models describe the statistical properties of noise and its relationship with the original image.
- Noise models can be used to estimate the noise level, type, and distribution in an image .
- Noise models can also be used to design appropriate filters or algorithms to remove or reduce noise from an image .
- Some common noise models in digital image processing are:
  - Gaussian noise: This noise has a normal or bell-shaped probability density function (PDF) and is characterized by a mean and a standard deviation. Gaussian noise is independent of the pixel intensity and is often caused by thermal fluctuations or electronic noise in the sensor or the circuitry.
  - Salt-and-pepper noise: This noise consists of random pixels that have either a very high (salt) or a very low (pepper) intensity value, creating a salt-and-pepper effect on the image. Salt-and-pepper noise is caused by errors in data transmission or bit errors in memory or communication channels.
  - Speckle noise: This noise is multiplicative, meaning that it is proportional to the pixel intensity. Speckle noise has a uniform or Rayleigh PDF and is often caused by coherent interference or scattering in imaging systems such as ultrasound, radar, or laser.
  - Poisson noise: This noise is also multiplicative and follows a Poisson PDF, which depends on the pixel intensity. Poisson noise is caused by the discrete nature of photons or electrons that are detected by the sensor, and is more noticeable in low-light or high-magnification images.