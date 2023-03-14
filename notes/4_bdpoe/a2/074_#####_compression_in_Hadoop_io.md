 Here is the content in markdown format for the topic ##### compression in Hadoop io:

##### Compression in Hadoop IO

Hadoop supports compression of data at multiple levels for efficient storage and processing:

- File level: Files can be compressed using record-oriented or block-oriented compression codecs. This reduces storage space and also speeds up processing as compressed data can be processed faster than uncompressed data. Commonly used codecs are Gzip, Bzip2, LZO, Snappy, etc.
- Block level: Hadoop allows configuring a compression codec at the block level within a file. This is useful when record-oriented compression is not suitable for a file and different blocks have different characteristics suitable for different codecs.
- Record level: Some codecs like LZO and Snappy allow compressing at the level of individual records within a block. This is suitable for data which has high entropy and does not compress at a block level.

Advantages of compression:

- Reduced storage space: This allows storing more data in the same storage space.
- Faster processing: Compressed data can be processed faster as it is smaller in size.
- Network I/O: Lesser amount of data needs to be sent over the network, reducing bandwidth consumption.

Disadvantages of compression:

- Increased CPU usage: Compression and decompression require additional CPU cycles leading to increased processing overhead.
- Compression algorithms have parameters which need to be tuned for optimal performance. Wrong choice of algorithm or parameters can lead to adverse performance.

Some tips for choosing a compression codec:

- Test compression ratios and performance for your data using different codecs and choose the one which gives optimal results.
- Use record-oriented codecs if your data has high entropy and does not compress well at a block level.
- LZO and Snappy are good choices if fast compression and decompression speed is important.
- Gzip and Bzip2 give higher compression ratios but at the cost of speed.
- Level of compression can be traded off for speed, depending on your requirements.

[Additional details, diagrams, examples, etc. can be added if required to explain the concepts better.]