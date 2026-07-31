### Mean Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Mean filters are a type of spatial filters that are used to smooth images by reducing the amount of intensity variation between neighboring pixels  .
- Mean filters are also called average filters or low-pass filters, as they attenuate high-frequency components (such as noise or edges) and preserve low-frequency components (such as homogeneous regions) of the image .
- Mean filters work by moving through the image pixel by pixel, replacing each value with the average value of neighboring pixels, including itself  .
- The size and shape of the neighborhood can be defined by a mask or a structuring element, which is usually a square or a circle  .
- The average value of the neighborhood can be calculated by using different methods, such as arithmetic mean, geometric mean, harmonic mean, or contraharmonic mean.
- Mean filters can effectively reduce additive noise, such as Gaussian noise or salt-and-pepper noise, but they also blur the edges and fine details of the image .
- Mean filters can be modified to preserve edges and details by using adaptive or bilateral methods, which take into account the local variance or similarity of the pixels in the neighborhood .