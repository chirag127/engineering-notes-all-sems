 Here is the content in markdown format as per your instructions:

### Data compression in application layer

1. Data compression reduces the number of bits needed to represent data. This saves bandwidth and storage space.
2. Application layer compression uses algorithms to compress data before it is sent over the network. This is different from link layer compression which compresses raw data packets.
3. Some popular application layer compression algorithms are:
- Gzip: Uses a combination of the LZ77 algorithm and Huffman coding. It can compress data by up to 80%.
- Bzip2: Uses the Burrows–Wheeler transform algorithm and Huffman coding. It provides higher compression ratios than Gzip but at the cost of lower speed.
- Lempel–Ziv–Markov chain algorithm (LZMA): Provides high compression ratios but is very CPU intensive. Used in 7-Zip archiver.
4. Advantages of application layer compression:
- Higher compression ratios resulting in more bandwidth and storage savings.
- Can compress specific types of data effectively (e.g. gzip for text, JPEG for images).
- Compressed data is portable and can be understood by any system that implements the compression algorithm.
5. Disadvantages of application layer compression:
- Compression and decompression require additional processing resulting in higher latency.
- The compression algorithm must be supported by both the sender and receiver for the data to be understood.

The above points cover the key aspects of data compression in the application layer. Let me know if you would like me to elaborate on any of the points or add more details to the answer.