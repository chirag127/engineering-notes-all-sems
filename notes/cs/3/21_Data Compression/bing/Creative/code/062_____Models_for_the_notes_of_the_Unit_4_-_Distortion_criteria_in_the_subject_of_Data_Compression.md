### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not.
- Lossy compression introduces some distortion or error in the reconstructed data, which may be acceptable for some applications such as audio or image compression.
- Distortion criteria are the measures of how close the reconstructed data is to the original data, using some mathematical quantity.
- Distortion criteria can be based on different aspects of the data, such as the numerical difference, the perceptual quality, the statistical properties, or the functional performance.
- Some common distortion criteria are:

  - Mean squared error (MSE): the average of the squared differences between the original and the reconstructed data values.
  - Peak signal-to-noise ratio (PSNR): the ratio of the maximum possible value of the data to the root mean squared error, expressed in decibels.
  - Structural similarity index (SSIM): a measure of the similarity of the structural information between the original and the reconstructed data, based on luminance, contrast, and correlation.
  - Bit error rate (BER): the ratio of the number of bits that are different between the original and the reconstructed data to the total number of bits.
  - Mean opinion score (MOS): a subjective rating of the quality of the reconstructed data, usually on a scale from 1 (bad) to 5 (excellent).

- The choice of the distortion criteria depends on the application and the user preference. Different distortion criteria may lead to different optimal compression methods and rates.
- Rate-distortion theory is the branch of information theory that studies the trade-off between the compression rate and the distortion level. It defines the rate-distortion function as the minimum possible compression rate for a given distortion level, or the minimum possible distortion for a given compression rate.
- The rate-distortion function can be calculated using an iterative algorithm, such as the Blahut-Arimoto algorithm, or approximated using some models, such as the Gaussian model or the Laplacian model.
- The rate-distortion function provides a theoretical lower bound for the performance of any compression system. The closer a practical compression system is to the rate-distortion function, the better it performs.