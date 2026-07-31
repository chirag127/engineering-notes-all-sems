 Here are the notes in Markdown format on the given topic:

### Hadoop I/O: compression for the notes of the Unit 4 - HDFS (Hadoop Distributed File System)

1. HDFS supports compression of data to save space and increase throughput.
2. HDFS supports Gzip, Bzip2, and Lzo compression algorithms.
3. Compression reduces the size of data to be stored and transferred hence improving performance of reads and writes.
4. When choosing a compression codec, one needs to consider:
 - Compression ratio - higher the better
 - Compression speed - faster the better
 - Decompression speed - faster the better
 - Algorithmic complexity - lower the better
 - Error recovery - some codecs like Lzo allow resynchronization if there is corruption
5. One can enable compression at:
 - File level - compress individual files
 - Block level - compress blocks within files
 - Record level - compress records within blocks
 - Column level - compress columns within records (for structured data)
6. Choosing the right level of compression depends on:
 - Type of data - structured vs unstructured
 - Pattern in data - more regular patterns compress better
 - Acceptable reduction in throughput due to compression/decompression processing overhead
 - Importance of compression ratio vs performance

The notes are written in a formal tone with points and without any emojis or external links as per the given instructions. Please let me know if you would like me to modify or add any other points to the notes.