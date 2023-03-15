# Components of Hadoop

Hadoop is an open-source software framework for storing and processing large datasets. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. The core components of Hadoop include:

1. **MapReduce**: A software programming model for processing large sets of data in parallel. It divides the input data into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks.

2. **Hadoop Distributed File System (HDFS)**: A Java-based distributed file system that can store all kinds of data without prior organization. It provides high-throughput access to application data and is suitable for applications that have large data sets.

3. **YARN**: A resource management framework for scheduling and handling resource requests from distributed applications. It is responsible for allocating system resources to the various running applications and managing their access to the shared resources.

These components work together to provide a reliable and scalable platform for data storage and processing.