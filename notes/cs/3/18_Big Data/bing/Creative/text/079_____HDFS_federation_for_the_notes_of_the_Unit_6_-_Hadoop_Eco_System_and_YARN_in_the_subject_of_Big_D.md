### HDFS Federation

- HDFS Federation is a feature of Hadoop 2.x that allows the HDFS architecture to support multiple NameNodes or namespaces in a cluster  .
- Each NameNode manages a separate namespace and a subset of the data blocks in the cluster .
- The NameNodes are independent and do not require coordination with each other .
- The DataNodes are shared by all the NameNodes and can store blocks from multiple namespaces .
- The clients can access any namespace by specifying the NameNode address in the URI .
- HDFS Federation improves the scalability, performance, and isolation of the HDFS system by separating the namespace and storage layers  .
- HDFS Federation also enables future innovations such as block storage services, erasure coding, and tiered storage.