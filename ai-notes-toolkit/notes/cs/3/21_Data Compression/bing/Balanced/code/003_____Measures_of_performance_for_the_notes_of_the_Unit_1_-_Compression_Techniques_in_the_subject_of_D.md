# Measures of performance for compression techniques

- Compression techniques are methods to reduce the size of data by removing redundancy or transforming the data into a more compact representation.
- Compression techniques can improve the efficiency of data storage, transmission, and processing, but they may also introduce some trade-offs such as complexity, distortion, or loss of information.
- To evaluate the performance of compression techniques, we need to use some measures or metrics that can quantify the benefits and costs of compression.
- Some common measures of performance for compression techniques are:

  - Compression ratio (CR): The ratio of the original data size to the compressed data size. It indicates how much the data is reduced by compression. A higher CR means a higher compression efficiency.
  - Compression factor (CF): The inverse of the compression ratio. It indicates how many times the original data can fit into the compressed data. A lower CF means a higher compression efficiency.
  - Bit rate (BR) or bits per symbol (bps): The average number of bits used to represent each symbol (such as a character, a pixel, or a sample) in the compressed data. It indicates the compactness of the compressed data. A lower BR or bps means a higher compression efficiency.
  - Distortion or error: The difference between the original data and the reconstructed data after compression and decompression. It indicates the quality or fidelity of the compressed data. A lower distortion or error means a higher compression quality.
  - Peak signal-to-noise ratio (PSNR): The ratio of the maximum possible signal power to the noise power caused by compression. It is often used to measure the distortion or error of image or audio compression. It is expressed in decibels (dB). A higher PSNR means a higher compression quality.
  - Mean squared error (MSE): The average of the squared differences between the original data and the reconstructed data. It is another way to measure the distortion or error of compression. A lower MSE means a higher compression quality.
  - Root mean squared error (RMSE): The square root of the MSE. It is more intuitive than MSE as it has the same unit as the original data. A lower RMSE means a higher compression quality.
  - Structural similarity index (SSIM): A measure of the perceptual similarity between the original data and the reconstructed data. It considers the luminance, contrast, and structure of the data. It ranges from 0 to 1. A higher SSIM means a higher compression quality.
  - Multi-scale structural similarity index (MS-SSIM): An extension of SSIM that considers the similarity at different scales or resolutions of the data. It is more suitable for image or video compression. It also ranges from 0 to 1. A higher MS-SSIM means a higher compression quality.
  - Accuracy: The percentage of the original data that is correctly preserved or recovered by the compression technique. It is often used to measure the performance of lossless compression or specific application-oriented compression. A higher accuracy means a higher compression quality.