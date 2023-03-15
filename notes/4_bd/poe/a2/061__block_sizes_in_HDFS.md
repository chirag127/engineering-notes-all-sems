 Here is the content in formal tone with points and without emojis or external links:

#### Block Sizes in HDFS

- HDFS splits files into block of 128MB by default. This default size can be changed by configuring dfs.block.size parameter.
- Larger block size reduces the metadata overhead as there will be fewer blocks and block locations to track. However, it also increases the minimum amount of data that can be read or written.
- Smaller block size increases the I/O parallelism as more blocks can be read/written in parallel. However, it also increases the metadata overhead.
- The block size should be chosen based on the typical input file size and the desired I/O throughput. If file sizes are typically large and streaming throughput is important, larger blocks are good. If file sizes are small or random access I/O is important, smaller blocks are good.
- The number of replicas of a block can be 3, which is the default, or it can be changed by configuring dfs.replication parameter.
- The block location is chosen by the NameNode randomly in a rack-aware manner to minimize data loss due to rack or node failures.
- The changes made to block sizes or replication factors do not affect existing files. New files will use the new parameters and will decide block boundaries and replications accordingly.