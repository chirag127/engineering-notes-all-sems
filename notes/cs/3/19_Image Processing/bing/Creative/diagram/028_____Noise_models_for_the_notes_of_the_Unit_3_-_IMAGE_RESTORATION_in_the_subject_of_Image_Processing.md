### Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Noise is unwanted information in digital images that degrades the quality and clarity of the image .
- Noise can be introduced during image acquisition, coding, transmission, and processing steps   .
- Noise can produce undesirable effects such as artifacts, unrealistic edges, unseen lines, corners, blurred objects and disturbs background scenes.
- To reduce these undesirable effects, prior knowledge of noise models is essential for further processing  .
- Noise models describe the statistical properties of noise and how it affects the image pixels.
- Some common noise models are:
  - Gaussian noise: This noise has a normal or bell-shaped probability density function (PDF) and is characterized by its mean and variance. Gaussian noise is independent of the pixel intensity and can be caused by sensor noise, thermal noise, or quantization noise.
  - Salt-and-pepper noise: This noise has only two possible values, either very high (salt) or very low (pepper), and affects a small percentage of pixels randomly. Salt-and-pepper noise can be caused by transmission errors, faulty memory locations, or malfunctioning pixels.
  - Speckle noise: This noise has a multiplicative effect on the image and is proportional to the pixel intensity. Speckle noise can be caused by coherent interference, such as in ultrasound or radar imaging.
  - Poisson noise: This noise has a Poisson PDF and is dependent on the pixel intensity. Poisson noise can be caused by photon counting or shot noise, such as in low-light imaging or X-ray imaging.
- Noise models can be used to design noise filters, noise estimation algorithms, and image restoration techniques  .