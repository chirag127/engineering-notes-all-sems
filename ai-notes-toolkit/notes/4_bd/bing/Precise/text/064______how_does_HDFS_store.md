#### How does HDFS store

- HDFS stores data in a distributed manner by dividing the data into small pieces and storing it on different DataNodes in the cluster .
- When storing the data, HDFS will divide the files into blocks and store each in the form of DataNode .
- Several DataNodes are connected to the primary node in the cluster, which is known as the NameNode .
- The NameNode executes file system namespace operations like opening, closing, and renaming files and directories .
- The size of each data block is 128MB, which is configurable and can be changed according to your requirement in the hdfs-site.xml file in your Hadoop directory .
- HDFS provides a way for MapReduce to process a subset of large data sets broken into blocks, parallelly on several nodes .
- HDFS is often used by companies who need to handle and store big data .