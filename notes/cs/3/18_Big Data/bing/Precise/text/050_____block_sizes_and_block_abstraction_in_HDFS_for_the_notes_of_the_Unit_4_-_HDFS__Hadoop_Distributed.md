### Block Sizes and Block Abstraction in HDFS

- HDFS block size is usually 64MB-128MB .
- Unlike other filesystems, a file smaller than the block size does not occupy the complete block size’s worth of memory .
- The block size is kept so large so that less time is made doing disk seeks as compared to the data transfer rate .
- The block division in HDFS is just logically built over the physical blocks of the underlying file system (e.g. ext3/fat) .
- The file system is not physically divided into blocks (say of 64MB or 128MB or whatever may be the block size). It's just an abstraction to store the metadata in the NameNode .
- In HDFS, the block size controls the level of replication declustering .
- The lower the block size, your blocks are more evenly distributed across the DataNodes .
- The higher the block size, your data are potentially less equally distributed in your cluster .