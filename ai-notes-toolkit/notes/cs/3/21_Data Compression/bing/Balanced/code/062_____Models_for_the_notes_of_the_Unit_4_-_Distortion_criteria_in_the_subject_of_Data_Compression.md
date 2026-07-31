### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly recovered or not after decompression.
- Lossy compression introduces some distortion or error in the reconstructed data, which may be acceptable or not depending on the application and the user's preference.
- Distortion criteria are the measures that quantify how close the reconstructed data is to the original data, using some mathematical or perceptual metric.
- Some common distortion criteria are:
  - Mean squared error (MSE): the average of the squared differences between the original and the reconstructed data values.
  - Peak signal-to-noise ratio (PSNR): the ratio of the maximum possible value of the data to the noise or error introduced by compression, expressed in decibels (dB).
  - Structural similarity index (SSIM): a perceptual metric that compares the luminance, contrast and structure of the original and the reconstructed data, ranging from 0 (no similarity) to 1 (perfect similarity).
  - Bit error rate (BER): the fraction of bits that are different between the original and the reconstructed data.
- Rate-distortion theory is the branch of information theory that studies the trade-off between the compression rate (the number of bits per data unit) and the distortion (the error or loss of quality) introduced by compression.
- Rate-distortion theory defines the rate-distortion function R(D) as the minimum compression rate that can be achieved for a given distortion level D, or equivalently, the minimum distortion that can be achieved for a given compression rate R.
- The rate-distortion function R(D) depends on the source statistics (the probability distribution of the data values) and the distortion measure (the metric used to quantify the error).
- The rate-distortion function R(D) can be calculated using an iterative algorithm called the Blahut-Arimoto algorithm, which alternates between finding the optimal probability distribution of the compressed data and the optimal distortion measure for a given distortion level.
- The rate-distortion function R(D) provides a theoretical lower bound for the performance of any practical compression system. The closer a compression system is to the rate-distortion function, the more efficient it is.