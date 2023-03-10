 Here is the content written in markdown format for the given topic:

### CALIC

CALIC stands for 'Context-based Adaptive Lossless Image Compression'. It is a lossless image compression technique which makes use of the spatial correlation between the pixels of an image. The key steps involved in CALIC are:

1. Prediction - Predict the value of a pixel based on its neighboring pixels. The difference between the actual and predicted value is encoded. This reduces the entropy and improves compression.
2. Context modeling - The neighboring pixels of the pixel being encoded are used to determine a context. A separate statistical model is used to encode the difference value for each context. This adapts the encoding based on the local characteristics of the image.
3. Entropy coding - The difference values are encoded using an entropy coder like arithmetic coding which outputs a compressed bitstream.

Advantages:
- It is a lossless technique, so no information is lost and the original image can be reconstructed from the compressed bitstream.
- It adapts to the local characteristics of the image and achieves higher compression ratios than general purpose lossless compression techniques.
- The compression and decompression processes are relatively simple and fast.

Disadvantages:
- The compression ratios are not as high as lossy techniques like JPEG.
- The technique is more complex to implement than general purpose techniques like Gzip.

Applications:
- Archiving and storage of images where lossless compression and high quality reconstruction is desired.
- Transfer of medical images where lossless compression is necessary to avoid loss of diagnostic information.

[Detailed diagrams and examples can be added here to aid understanding]