### Four Levels of Federation for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

- Federation in the cloud is the concept of integrating different cloud services and applications across multiple cloud providers and platforms.
- Federation can enhance the scalability, availability, interoperability, and security of cloud computing.
- Federation can be achieved at four levels: infrastructure, platform, application, and data.
- Infrastructure level federation involves sharing and pooling of physical and virtual resources, such as compute, storage, and network, among different cloud providers.
- Platform level federation involves sharing and integrating of cloud platforms, such as Hadoop, Google App Engine, and OpenStack, among different cloud providers.
- Application level federation involves sharing and composing of cloud applications, such as web services, workflows, and mashups, among different cloud providers.
- Data level federation involves sharing and synchronizing of data, such as files, databases, and streams, among different cloud providers.
- Hadoop is an open source platform for distributed processing of large-scale data using a cluster of commodity hardware.
- Hadoop consists of two main components: Hadoop Distributed File System (HDFS) and MapReduce.
- HDFS is a distributed file system that stores data in blocks across multiple data nodes in the cluster.
- MapReduce is a programming model that allows parallel processing of data using two functions: map and reduce.
- HDFS federation is a feature of Hadoop that allows multiple independent name nodes to coexist in the same cluster, each managing a separate namespace and a subset of data nodes.
- HDFS federation improves the scalability, availability, and performance of HDFS by allowing horizontal scaling of name nodes, reducing the load on a single name node, and increasing the throughput of data access.
- HDFS federation can be configured using the following steps:
  - Define the name nodes and their namespaces in the configuration file `hdfs-site.xml`.
  - Define the data nodes and their name node mappings in the configuration file `dfs.datanode.data.dir`.
  - Start the name nodes and the data nodes using the scripts `hdfs namenode` and `hdfs datanode`.
  - Use the command `hdfs dfsadmin -report` to check the status of the name nodes and the data nodes.