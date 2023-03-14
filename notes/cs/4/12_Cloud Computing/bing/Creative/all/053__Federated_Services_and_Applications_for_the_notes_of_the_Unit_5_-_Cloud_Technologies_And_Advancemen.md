### Federated Services and Applications for the notes of the Unit 5 - Cloud Technologies And Advancements Hadoop in the subject of Cloud Computing

- Hadoop is an open-source software framework for storing data and running applications on clusters of commodity hardware.
- Hadoop provides massive storage for any kind of data, enormous processing power and the ability to handle virtually limitless concurrent tasks or jobs.
- Hadoop consists of two main layers: Namespace and Block Storage Service.
- Namespace consists of directories, files and blocks. It supports all the namespace related file system operations such as create, delete, modify and list files and directories.
- Block Storage Service consists of Block Management (performed in the NameNode) and Storage (provided by the DataNodes).
- Block Management provides DataNode cluster membership, processes block reports, maintains location of blocks, supports block related operations, manages replica placement, block replication and deletion.
- Storage allows DataNodes to store blocks on the local file system and allow read/write access.
- The prior Hadoop architecture allows only a single namespace for the entire cluster. In that configuration, a single NameNode manages the namespace.
- HDFS Federation addresses this limitation by adding support for multiple NameNodes/namespaces to HDFS.
- In HDFS Federation, the NameNodes are federated, meaning they are independent and do not require coordination with each other.
- The DataNodes are used as common storage for blocks by all the NameNodes.
- Each DataNode registers with all the NameNodes in the cluster and sends periodic heartbeats and block reports.
- Each namespace has its own set of blocks, called a Block Pool.
- A Block Pool is managed independently by its corresponding NameNode.
- A Namespace and its Block Pool together are called a Namespace Volume.
- A Namespace Volume is a self-contained unit of management and can be upgraded as a unit during cluster upgrade.
- A ClusterID identifier is used to identify all the nodes in the cluster.
- Users may use ViewFs to create personalized namespace views.
- ViewFs is analogous to client side mount tables in some Unix/Linux systems.

#### Benefits of HDFS Federation

- It allows horizontal scaling of the name service by adding more NameNodes/namespaces to the cluster .
- It improves the availability and reliability of the name service by isolating the impact of NameNode failures to a single namespace .
- It increases the throughput of the file system operations by distributing the load among multiple NameNodes .
- It reduces the load on the DataNodes by allowing them to communicate with only a subset of NameNodes at a time .
- It simplifies the administration and management of the cluster by allowing different namespaces to have different policies and configurations .

#### Mnemonics and learning tricks

- To remember the two main layers of Hadoop, think of **N**ame**s**pace and **B**lock **S**torage **S**ervice as **NBSS**.
- To remember the components of Block Storage Service, think of **B**lock **M**anagement and **S**torage as **BMS**.
- To remember the benefits of HDFS Federation, think of **S**caling, **A**vailability, **T**hroughput, **L**oad and **S**implicity as **SATLS**.