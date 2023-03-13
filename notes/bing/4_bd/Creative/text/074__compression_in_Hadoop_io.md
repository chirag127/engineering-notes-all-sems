##### Compression in Hadoop io

- Compression is a technique to reduce the size of data by encoding it in a different format that uses fewer bits.
- Compression is useful for Hadoop because it can save storage space, network bandwidth, and disk I/O time.
- Hadoop supports various compression codecs, such as DEFLATE, gzip, bzip2, LZO, LZ4, and Snappy.
- Only bzip2 is splittable, meaning that it can be processed by multiple map tasks in parallel without reading the entire file.
- Hadoop provides a CompressionCodecFactory class that can detect the compression format of an input file based on its extension and return the appropriate CompressionCodec object.
- A CompressionCodec object can create an InputStream or an OutputStream that can compress or decompress data on the fly.
- Some compression codecs can also work with direct bytebuffers, which are faster and more efficient than regular byte arrays.
- Compression can be applied to different stages of Hadoop processing, such as input, output, intermediate, and shuffle.
- Compression can improve the performance and scalability of Hadoop applications, but it also has some trade-offs, such as CPU overhead, memory usage, and compatibility issues.