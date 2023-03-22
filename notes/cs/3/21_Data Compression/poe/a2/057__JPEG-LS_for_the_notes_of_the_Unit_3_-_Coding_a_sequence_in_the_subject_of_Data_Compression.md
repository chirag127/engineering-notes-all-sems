 Here is the content in markdown format without any emojis or external links as per your instructions:

### JPEG-LS for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. JPEG-LS is a lossless and near-lossless image compression standard. It was created to improve upon the earlier JPEG standard.
2. JPEG-LS uses a linear predictor and Golomb-Rice coding for entropy coding. It gives better compression than JPEG for lossless compression and similar compression ratios for near-lossless compression while having lower computational complexity.
3. The steps in JPEG-LS are:
 - Split the image into non-overlapping blocks
 - Apply a linear predictor to each block to get a residual block
 - Apply Golomb-Rice coding to the residual block
4. The linear predictor uses neighboring samples to predict the current sample. The difference between the actual and predicted samples forms the residual block. Golomb-Rice coding efficiently encodes the residual values.
5. JPEG-LS provides a simple and fast mode suitable for low-end applications with the option to turn on more powerful features for higher compression. It also has features for error resilience to handle transmission errors.
6. JPEG-LS has applications in medical imaging, remote sensing, document image compression, etc. where lossless or near-lossless compression is required. It provides a good balance between compression efficiency and computational simplicity.