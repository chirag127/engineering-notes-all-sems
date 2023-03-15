#### File sizes in HDFS

- HDFS is designed to handle very large files. The default block size in HDFS is 128 MB, which means that files are split into 128 MB chunks and distributed across the cluster.
- Files smaller than the block size will not be split and will be stored as a single block.
- Files larger than the block size will be split into multiple blocks, with each block being stored on a different DataNode in the cluster.
- It is recommended to use large files in HDFS, as it is more efficient to store and process large files than many small files.
- One way to remember the default block size in HDFS is to use the mnemonic "HDFS: Hundreds of MBs Default Size" where "Hundreds" refers to the 128 MB default block size.
- It is important to note that the block size can be configured and changed to better suit the needs of the specific use case.
- When dealing with many small files, it may be more efficient to combine them into a larger file before storing them in HDFS. This can be done using tools such as Hadoop Archive (HAR) or Sequence Files.
- In summary, HDFS is designed to handle large files and it is recommended to use large files for better performance. The default block size is 128 MB, but it can be configured to better suit the needs of the specific use case. When dealing with many small files, it may be more efficient to combine them into a larger file before storing them in HDFS.