### Models for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

Data compression is the process of reducing the size of data to save storage space, transmission time, and other resources. In order to achieve compression, data is analyzed and modified to remove redundancy and irrelevance. However, the process of compression may introduce distortion or loss of information. In this unit, we will discuss the different models that can be used to measure and evaluate distortion in data compression.

#### 1. Signal-to-Noise Ratio (SNR) Model
- The signal-to-noise ratio (SNR) model is a measure of the ratio of the power of the signal to the power of the noise in a communication channel.
- It is commonly used to evaluate the quality of audio and video signals.
- The higher the SNR, the better the quality of the signal and the lower the distortion.
- The SNR can be calculated as:

  SNR = 10 * log10(Ps / Pn)

  where Ps is the signal power and Pn is the noise power.

#### 2. Mean Squared Error (MSE) Model
- The mean squared error (MSE) model is a measure of the average squared difference between the original and the compressed signal.
- It is commonly used in image and video compression.
- The lower the MSE, the better the quality of the compressed signal and the lower the distortion.
- The MSE can be calculated as:

  MSE = 1/N * Σ(i=1 to N) (x(i) - x'(i))^2

  where N is the number of samples, x(i) is the original signal, and x'(i) is the compressed signal.

#### 3. Peak Signal-to-Noise Ratio (PSNR) Model
- The peak signal-to-noise ratio (PSNR) model is a measure of the ratio of the maximum power of the signal to the MSE.
- It is commonly used in image and video compression.
- The higher the PSNR, the better the quality of the compressed signal and the lower the distortion.
- The PSNR can be calculated as:

  PSNR = 10 * log10(Pmax^2 / MSE)

  where Pmax is the maximum signal power.

#### 4. Structural Similarity Index (SSIM) Model
- The structural similarity index (SSIM) model is a measure of the similarity between the original and the compressed signal.
- It takes into account the luminance, contrast, and structure of the signal.
- It is commonly used in image and video compression.
- The higher the SSIM, the better the quality of the compressed signal and the lower the distortion.
- The SSIM can be calculated as:

  SSIM = (2μxμy + C1) * (2σxy + C2) / ((μx^2 + μy^2 + C1) * (σx^2 + σy^2 + C2))

  where μx and μy are the means of the original and compressed signals, σx and σy are the standard deviations of the original and compressed signals, σxy is the covariance of the original and compressed signals, and C1 and C2 are constants.

In conclusion, the models discussed in this unit provide a quantitative measure of distortion in data compression. By using these models, we can evaluate the quality of the compressed signal and optimize the compression algorithm to minimize distortion.