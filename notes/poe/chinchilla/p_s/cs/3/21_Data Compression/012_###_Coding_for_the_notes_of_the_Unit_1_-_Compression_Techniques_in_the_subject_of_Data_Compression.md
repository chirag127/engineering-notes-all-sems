### Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

In Data Compression, coding refers to the process of representing data using fewer bits than the original representation. There are two types of coding techniques: lossless and lossy. Lossless coding techniques preserve all the information in the original data, while lossy techniques discard some information to achieve higher compression ratios.

#### Lossless Coding Techniques

1. Run-Length Encoding (RLE): This technique replaces consecutive identical values with a count and a single value. For example, the sequence "AAAAABBBBCCCCC" can be compressed to "5A4B5C".

2. Huffman Coding: This technique assigns shorter codes to more frequently occurring symbols and longer codes to less frequently occurring symbols. Huffman coding is widely used in image and audio compression.

3. Arithmetic Coding: This technique represents a message as a single rational number in the range [0,1]. The number is then encoded using a binary representation. Arithmetic coding can achieve higher compression ratios than Huffman coding.

#### Lossy Coding Techniques

1. Discrete Cosine Transform (DCT): This technique transforms a signal into its frequency domain representation. The high-frequency components are then discarded or quantized to achieve compression. DCT is widely used in image and video compression.

2. Wavelet Transform: This technique decomposes a signal into a set of wavelet coefficients. The coefficients can be quantized or discarded to achieve compression. Wavelet transform is used in image, audio, and video compression.

3. Vector Quantization: This technique groups similar vectors together and replaces them with a single representative vector. Vector quantization is used in speech and image compression.

Advantages of coding techniques:

- Reduced storage space required for data
- Faster transmission of data over networks
- Reduced bandwidth consumption 
- Lower costs for storage and transmission

Disadvantages of coding techniques:

- Lossy techniques may result in a loss of information
- Compression and decompression can be computationally expensive
- The quality of decompressed data may not be as good as the original data

Examples of applications of coding techniques:

- Image compression in JPEG, PNG, and GIF formats
- Audio compression in MP3 and AAC formats
- Video compression in MPEG and H.264 formats
- Data compression in ZIP and RAR formats

In conclusion, coding techniques are essential in data compression to achieve higher compression ratios and reduce storage and transmission costs. It is important to choose the appropriate coding technique depending on the type of data and the level of compression required.