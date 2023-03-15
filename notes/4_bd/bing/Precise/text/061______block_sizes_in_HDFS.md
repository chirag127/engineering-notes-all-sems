#### Block Sizes in HDFS

- The size of the data block in HDFS is 64 MB by default, which can be configured manually .
- In general, the data blocks of size 128MB is used in the industry .
- The size of these HDFS data blocks is 128 MB by default .
- We can configure the block size as per our requirement by changing the dfs.block.size property in hdfs-site.xml .
- Hadoop distributes these blocks on different slave machines, and the master machine stores the metadata about blocks location .
- The default block size in HDFS was 64mb for Hadoop 1.0 and 128mb for Hadoop 2.0 .
- The block size configuration change can be done on an entire cluster or can be configured for specific blocks .
- The block size and replication factor are configurable per file .
- All blocks in a file except the last block are the same size .
- Users can start a new block without filling out the last block to the configured block size after the support for variable length block was added to append and hsync .