### Measures of performance for compression techniques

- Compression techniques are methods to reduce the size of data by removing redundancy or irrelevant information.
- The performance of compression techniques can be measured by various metrics, depending on the type and purpose of the data.
- Some common metrics are:

  - Compression ratio (CR): The ratio of the number of bits required to represent the data before compression to the number of bits required to represent the data after compression. A higher CR means a higher compression efficiency. CR = (original size / compressed size) 
  - Compression factor (CF): The inverse of compression ratio. CF = (compressed size / original size) 
  - Bits per character (bpc) or bits per pixel (bpp): The average number of bits required to represent one character or pixel of the data after compression. A lower bpc or bpp means a higher compression efficiency. bpc = (compressed size / number of characters) or bpp = (compressed size / number of pixels)  
  - Mean squared error (MSE): The average of the squared differences between the original and the compressed data values. A lower MSE means a higher compression quality. MSE = (1 / N) * sum((original value - compressed value)^2) 
  - Root mean squared error (RMSE): The square root of the MSE. A lower RMSE means a higher compression quality. RMSE = sqrt(MSE) 
  - Peak signal-to-noise ratio (PSNR): The ratio of the maximum possible value of the data to the noise introduced by compression. A higher PSNR means a higher compression quality. PSNR = 10 * log10((max value)^2 / MSE) 
  - Structural similarity index (SSIM): A measure of the similarity between the original and the compressed data based on luminance, contrast, and structure. A higher SSIM means a higher compression quality. SSIM ranges from -1 to 1, where 1 means identical data. SSIM = (2 * mean(original) * mean(compressed) + c1) * (2 * covariance(original, compressed) + c2) / ((mean(original)^2 + mean(compressed)^2 + c1) * (variance(original) + variance(compressed) + c2)) 
  - Multi-scale structural similarity index (MS-SSIM): An extension of SSIM that considers different scales of the data. A higher MS-SSIM means a higher compression quality. MS-SSIM = product(SSIM(scale))^(weight(scale)) 
  - Accuracy: The percentage of correct or relevant information retained after compression. A higher accuracy means a higher compression quality. Accuracy = (number of correct or relevant information / number of total information) * 100 
  - Query execution time: The time required to execute a query on the compressed data. A lower query execution time means a higher compression performance. Query execution time = (end time - start time) 
  - Throughput: The rate of data processing or transmission after compression. A higher throughput means a higher compression performance. Throughput = (amount of data / time) 
  - Latency: The delay between the input and the output of the compression process. A lower latency means a higher compression performance. Latency = (output time - input time) 
  - Resource consumption: The amount of memory, CPU, disk, or network resources used by the compression process. A lower resource consumption means a higher compression performance. Resource consumption = (resource used / resource available) 

- Different compression techniques may have different trade-offs between these metrics, depending on the type and purpose of the data. For example, lossless compression techniques preserve the accuracy and quality of the data, but may have lower compression efficiency and performance than lossy compression techniques, which discard some information and introduce some noise or distortion to the data.   
- Therefore, the choice of compression technique and the measure of performance should be based on the specific requirements and constraints of the data and the application.