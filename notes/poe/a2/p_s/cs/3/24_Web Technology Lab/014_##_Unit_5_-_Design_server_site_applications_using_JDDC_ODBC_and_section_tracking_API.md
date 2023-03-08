 Here is the content in markdown format for the topic #### file sizes in HDFS:

#### File Sizes in HDFS

- HDFS is designed to store very large files, typically in the range of gigabytes to terabytes.
- HDFS supports files of unlimited size. The only practical limit is the capacity of the hardware.
- HDFS is not suitable for a large number of small files as it can lead to:
-- Low throughput
-- Wastage of storage space due to increased replication overhead
-- Performance degradation due to excessive metadata operations
- To achieve high throughput and streaming access in HDFS, it is recommended to:
-- Have a reasonable number of large files
-- Combine multiple small files into a single large file using techniques like:
-- Sequence file format
-- Compression

To summarize, for optimal performance and efficiency in HDFS:

- Store large files (GBs-TBs)
- Avoid excessive number of small files
- Combine multiple small files into fewer large files

Here is an ASCII diagram to illustrate the concept:

Small Files -> Concatenation/Sequence Files -> Large Files -> HDFS

[A diagram showing the process of combining small files into large files for storing in HDFS can be included here for illustration]

The advantages of storing large files in HDFS are:

- High throughput
- Streaming access
- Efficient storage utilization
- Fast processing using MapReduce

Applications like log processing, scientific data processing, web crawling, etc. that generate large volume of data are suitable to use HDFS.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.