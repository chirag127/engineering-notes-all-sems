#### Block Abstraction in HDFS
- HDFS block size is usually 64MB-128MB .
- Unlike other filesystems, a file smaller than the block size does not occupy the complete block size’s worth of memory .
- The block size is kept so large so that less time is made doing disk seeks as compared to the data transfer rate .
- In HDFS the abstraction is made over the blocks of a file rather than a single file which simplifies the storage subsystem .
- Since the size of the blocks is fixed it is easy to manage and calculate how many blocks can be stored on a single disk .
- HDFS exposes a file system namespace and allows user data to be stored in files .
- Internally, a file is split into one or more blocks and these blocks are stored in a set of DataNodes .
- The NameNode executes file system namespace operations like opening, closing, and renaming files and directories .
