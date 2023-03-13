 Here is the content in Markdown format on the topic ##### Compression in Hadoop IO:

##### Compression in Hadoop IO

Hadoop provides infrastructure to handle big data and one of the key aspects of reducing data size and optimizing storage is compression. Some of the key points about compression in Hadoop IO are:

1. Hadoop supports compressing both input and output data using various compressions algorithms like Gzip, Bzip2, Lzo, Snappy, etc. This reduces the storage space and increases the I/O speed.
2. Compression can be applied at different levels in Hadoop:
- At DFS level - Files can be stored in a compressed format in HDFS.
- At MapReduce level - The mappers can compress the intermediate data which is shuffled between mappers and reducers. The reducers can also compress the final output.
- At application level - The input data can be read in a compressed format and processed and output can be written in a compressed format. The application has to handle compression/decompression in this case.
3. The selection of compression algorithm depends on various factors like compression ratio, CPU usage, decompression speed, etc. For e.g. Snappy has fast compression and decompression speed but Gzip gives a better compression ratio.
4. Hadoop provides APIs and command line tools to compress and decompress data. E.g. FileSystem class provides methods to compress/decompress files and distcp tool can be used with -p option to preserve compression while copying data.

Some mnemonics and learning tricks to remember compression in Hadoop:

- CACC - Compression at DFS, Application and MapReduce levels (C, A, CC)
- Gzip - Good compression ratio but slow
- Bzip2 - Better compression but even slower
- Lzo and Snappy - Faster compression and decompression but compression ratio is lesser than Gzip/Bzip2

Hope this helps you learn about Compression in Hadoop IO. Let me know if you would like me to elaborate on any of the points or add more details.