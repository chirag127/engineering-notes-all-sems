#### Block sizes in HDFS

- HDFS stands for Hadoop Distributed File System, which is a distributed file system that stores large amounts of data across multiple nodes in a cluster.
- HDFS splits a file into one or more blocks, and stores each block on a different node. The default block size in HDFS is 128 MB, which can be configured by changing the parameter `dfs.blocksize` in the `hdfs-site.xml` file.
- The block size in HDFS is much larger than the block size in a traditional file system, such as 4 KB or 8 KB. This is because HDFS is designed for storing and processing large files, and having a large block size reduces the number of disk seeks and network transfers required to access a file.
- Some of the advantages of having a large block size in HDFS are:
  - It improves the throughput of data transfer, as each block can be read or written in a single disk operation.
  - It reduces the metadata overhead, as each file requires fewer blocks and hence fewer entries in the namenode's memory.
  - It increases the fault tolerance, as each block can be replicated across multiple nodes and recovered in case of node failure.
- Some of the disadvantages of having a large block size in HDFS are:
  - It wastes disk space, as each block is padded to the full block size regardless of the actual file size. For example, if a file is 130 MB, it will occupy two blocks of 128 MB each, wasting 126 MB of disk space.
  - It increases the latency of data access, as each block may be located on a different node and require a network transfer to read or write.
  - It reduces the parallelism of data processing, as each block can be processed by only one mapper or reducer at a time.
- Some of the factors that affect the choice of block size in HDFS are:
  - The size and type of the files stored in HDFS. For example, if the files are small and text-based, a smaller block size may be preferred to avoid wasting disk space and increase parallelism. If the files are large and binary, a larger block size may be preferred to improve throughput and reduce metadata overhead.
  - The network bandwidth and latency of the cluster. For example, if the network is fast and reliable, a larger block size may be preferred to reduce the number of network transfers and disk seeks. If the network is slow and unreliable, a smaller block size may be preferred to increase the fault tolerance and recovery speed.
  - The processing framework and application logic used on the data. For example, if the processing framework is MapReduce, a larger block size may be preferred to match the input split size and reduce the number of mappers. If the processing framework is Spark, a smaller block size may be preferred to increase the number of partitions and parallelism.

- A possible mnemonic to remember the default block size in HDFS is: **128 MB = 1 HDFS block**. This can be associated with the fact that HDFS is a part of the Hadoop ecosystem, which has the letter H as its logo. The letter H has one horizontal line and two vertical lines, which can be seen as the digits 1, 2, and 8.