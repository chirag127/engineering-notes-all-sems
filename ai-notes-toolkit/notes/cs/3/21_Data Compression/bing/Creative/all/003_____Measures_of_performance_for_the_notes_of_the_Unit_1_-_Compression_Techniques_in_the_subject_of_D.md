# Measures of performance for compression techniques

Compression techniques are methods to reduce the size of data by eliminating redundancy or transforming the data into a more compact representation. Compression techniques can improve the efficiency of data storage, transmission, and processing. However, compression techniques also introduce some trade-offs, such as loss of information, increased complexity, and reduced performance. Therefore, it is important to measure the performance of compression techniques and compare them with the original data.

There are different measures of performance for compression techniques, depending on the type of data, the compression algorithm, and the application requirements. Some of the common measures of performance are:

- **Compression ratio (CR)**: This is the ratio of the size of the original data to the size of the compressed data. It indicates how much the data has been reduced by compression. A higher compression ratio means a higher compression efficiency. CR is defined as:

CR = (original size) / (compressed size)

- **Compression factor (CF)**: This is the inverse of the compression ratio. It indicates how many times the original data can fit into the compressed data. A lower compression factor means a higher compression efficiency. CF is defined as:

CF = (compressed size) / (original size)

- **Bits per character (bpc)**: This is the average number of bits used to represent each character in the compressed data. It indicates how compact the compressed data is. A lower bits per character means a higher compression efficiency. bpc is defined as:

bpc = (compressed size) / (number of characters)

- **Bits per pixel (bpp)**: This is the average number of bits used to represent each pixel in the compressed image. It indicates how compact the compressed image is. A lower bits per pixel means a higher compression efficiency. bpp is defined as:

bpp = (compressed size) / (number of pixels)

- **Mean squared error (MSE)**: This is the average of the squared differences between the original data and the decompressed data. It indicates how much the data has been distorted by compression. A lower mean squared error means a higher compression quality. MSE is defined as:

MSE = (1 / N) * sum((original data - decompressed data)^2)

- **Root mean squared error (RMSE)**: This is the square root of the mean squared error. It indicates how much the data has been distorted by compression. A lower root mean squared error means a higher compression quality. RMSE is defined as:

RMSE = sqrt(MSE)

- **Peak signal-to-noise ratio (PSNR)**: This is the ratio of the maximum possible value of the original data to the root mean squared error. It indicates how much the data has been distorted by compression relative to the original data. A higher peak signal-to-noise ratio means a higher compression quality. PSNR is defined as:

PSNR = 10 * log10((max value)^2 / RMSE)

- **Structural similarity index (SSIM)**: This is a measure of the similarity between the original image and the decompressed image based on the luminance, contrast, and structure of the images. It indicates how much the image has been distorted by compression perceptually. A higher structural similarity index means a higher compression quality. SSIM is defined as:

SSIM = (2 * mean(original image) * mean(decompressed image) + c1) * (2 * standard deviation(original image) * standard deviation(decompressed image) + c2) * (covariance(original image, decompressed image) + c3) / ((mean(original image)^2 + mean(decompressed image)^2 + c1) * (standard deviation(original image)^2 + standard deviation(decompressed image)^2 + c2) * (1 + c3))

where c1, c2, and c3 are small constants to avoid division by zero.

- **Multi-scale structural similarity index (MS-SSIM)**: This is an extension of the structural similarity index that considers the similarity between the original image and the decompressed image at different scales or resolutions. It indicates how much the image has been distorted by compression perceptually across different levels of detail. A higher multi-scale structural similarity index means a higher compression quality. MS-SSIM is defined as:

MS-SSIM = product(SSIM(l)^(w(l)))

where l is the scale index, w(l) is the weight for each scale, and SSIM(l) is the structural similarity index at scale l.

- **Percent root