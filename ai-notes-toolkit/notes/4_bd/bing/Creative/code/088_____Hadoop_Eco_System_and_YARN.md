### Hadoop Eco System and YARN

Hadoop is a framework for distributed processing of large-scale data sets across clusters of computers. Hadoop consists of several components, such as HDFS, MapReduce, Hive, Pig, HBase, etc. These components form the Hadoop ecosystem, which provides various tools and services for data ingestion, storage, processing, analysis, and management.

YARN (Yet Another Resource Negotiator) is one of the core components of the Hadoop ecosystem. It is responsible for resource management and job scheduling in Hadoop clusters. YARN was introduced in Hadoop 2.0 to overcome the limitations of MapReduce, such as scalability, efficiency, and flexibility.

YARN architecture consists of two main components: a global ResourceManager (RM) and per-application ApplicationMaster (AM). The RM allocates resources (such as CPU, memory, disk, network) to different applications running on the cluster. The AM negotiates resources with the RM and coordinates the execution of tasks on the cluster nodes. Each node also has a NodeManager (NM) that monitors the resource usage and reports to the RM.

YARN enables Hadoop to support various types of applications, such as batch, interactive, streaming, graph, machine learning, etc. YARN also allows for dynamic resource allocation, high availability, security, and multi-tenancy. YARN is compatible with the existing MapReduce applications and supports new frameworks such as Spark, Flink, Storm, etc. YARN is the gateway to easier programming and better performance for Hadoop users.