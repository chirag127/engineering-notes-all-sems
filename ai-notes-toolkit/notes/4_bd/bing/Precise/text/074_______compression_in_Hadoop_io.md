##### Compression in Hadoop IO

1. Hadoop provides support for various compression codecs and formats, such as gzip, bzip2, snappy, and lz4.
2. Compression can be used to reduce the size of data stored on HDFS, which can save storage space and reduce the amount of data that needs to be transferred between nodes during processing.
3. Compression can be applied at different stages of data processing, such as during input, output, or intermediate stages.
4. Hadoop provides a configurable and extensible framework for adding new compression codecs and formats.
5. Compression can be enabled or disabled for individual files or for entire directories.
6. Compression can be configured at the cluster level or at the job level.
7. Compression can have a significant impact on the performance of data processing, and the choice of compression codec and format should be carefully considered based on the characteristics of the data and the processing requirements.
8. Some compression codecs, such as gzip and bzip2, provide a high level of compression but can be computationally expensive, while others, such as snappy and lz4, provide faster compression and decompression but with a lower level of compression.
9. Hadoop provides tools for estimating the compression ratio and performance of different codecs and formats on sample data.
10. Hadoop also provides support for splittable compression formats, which allow data to be processed in parallel even when compressed. This can improve the performance of data processing by allowing multiple tasks to work on the same compressed file simultaneously. However, not all compression formats are splittable, and the choice of compression format should take this into consideration.