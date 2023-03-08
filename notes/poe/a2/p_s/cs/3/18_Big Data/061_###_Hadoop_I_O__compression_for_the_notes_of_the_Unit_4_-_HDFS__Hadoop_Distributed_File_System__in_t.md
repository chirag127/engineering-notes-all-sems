 Here is the content in markdown format for the topic ### Hadoop I/O: compression for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

### Hadoop I/O: compression
- Hadoop provides built-in support for compression algorithms to compress the data stored in HDFS and improve I/O performance.
- The two main compression algorithms supported by Hadoop are:
	- Gzip - general purpose lossless data compression algorithm
	- Bzip2 - high-quality lossless data compression algorithm
- The benefits of compression are:
	- Reduced storage space - Store more data in the same space
	- Faster I/O - Read/Write performance is improved as the amount of data to be transferred is reduced
	- Network bandwidth usage - Lesser amount of data is transferred over the network, thereby reducing bandwidth usage
- However, compression also has some overhead in terms of CPU usage for compressing and decompressing the data. The trade-off should be evaluated based on the dataset and use case.
- In Hadoop, compression can be applied at:
	- Storage level - When storing data in HDFS, files/blocks can be compressed
	- Shuffling stage of a MapReduce job - Intermediate Map outputs can be compressed
	- Transfer level - Data sent over the network can be compressed for efficient transfer
- To enable compression for a file in HDFS, we can specify the compressionType and compressionCodec parameters when creating the file. For example:
hdfs dfs -create -compressionType gzip -encoding utf8 myFile.txt
- The NameNode tracks the compression codec and type used for each block in the HDFS metadata.
- To summarize, compression in Hadoop can significantly improve performance and reduce storage/network usage at the cost of some extra CPU usage. The choice of compression algorithm and compression points should be evaluated based on the use case to achieve the optimal benefits.