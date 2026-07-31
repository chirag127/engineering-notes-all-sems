 Here is the content in markdown format with formal tone and without emojis:

##### Compression in Hadoop IO

1. Why compression?
- Data volumes are huge in Hadoop, compression saves storage space and increases throughput.
- Reduces the number of I/O operations as fewer blocks need to be read/written.
- Faster processing due to reduced data size.

2. Types of compression
- Record-level compression: Compresses individual records/lines. Good for textual data. Example: Gzip
- Block-level compression: Splits input into blocks and compresses each block. Any record/block boundary is retained. Example: Gzip, Bzip2
- Columnar compression: Data is stored column-wise and each column is compressed separately. Achieves high compression ratios for columns with similar values. Example: RCFile format

3. Choosing a compression codec
- Algorithmic complexity vs compression ratio
- Processing overhead of compression/decompression
- Data characteristics (text vs numeric, structured vs unstructured)
- Available CPU resources

Commonly used compression codecs in Hadoop are Gzip, Bzip2, LZO and Snappy.
Trade-off between compression ratio and CPU usage. Test and choose the optimal codec for your use case.

[No external links included as instructed]