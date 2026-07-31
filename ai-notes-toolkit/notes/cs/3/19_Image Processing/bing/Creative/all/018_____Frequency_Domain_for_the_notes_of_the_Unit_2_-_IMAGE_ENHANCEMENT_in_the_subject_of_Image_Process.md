# Frequency Domain

- Frequency domain is a way of representing an image in terms of its spatial frequencies, which are the rates of change of pixel values in different directions.
- Frequency domain methods of image enhancement are based on the Fourier transform, which converts an image from the spatial domain to the frequency domain, and vice versa.
- The Fourier transform of an image F(u,v) is a complex function that contains both the magnitude and the phase of the spatial frequencies in the image.
- The magnitude of F(u,v) represents the amount of each frequency component present in the image, while the phase of F(u,v) represents the location of each frequency component in the image.
- Image enhancement in the frequency domain involves modifying the magnitude and/or the phase of F(u,v) to achieve the desired effect, and then applying the inverse Fourier transform to obtain the enhanced image in the spatial domain.
- Some common frequency domain methods of image enhancement are:

  - Low-pass filtering: This method reduces the high-frequency components of F(u,v), which correspond to the fine details and noise in the image. This results in a smoother and less noisy image, but also reduces the sharpness and contrast of the image edges.
  - High-pass filtering: This method reduces the low-frequency components of F(u,v), which correspond to the large and smooth regions in the image. This results in a sharper and more contrasted image, but also enhances the noise and artifacts in the image.
  - Band-pass filtering: This method preserves a certain range of frequencies in F(u,v), and attenuates the frequencies outside that range. This can be used to enhance specific features or details in the image, or to remove unwanted frequencies such as periodic noise or interference.
  - Notch filtering: This method removes or reduces a specific frequency or a set of frequencies in F(u,v), which are usually caused by some external source or defect in the image acquisition process. This can be used to eliminate or reduce the effects of noise, distortion, or artifacts in the image.
  - Homomorphic filtering: This method separates the illumination and reflectance components of an image, and applies different filters to each component. This can be used to improve the contrast and brightness of an image, or to correct the uneven illumination in the image.