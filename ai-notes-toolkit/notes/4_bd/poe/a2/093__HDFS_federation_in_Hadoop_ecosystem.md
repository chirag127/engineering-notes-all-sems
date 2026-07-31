 Here is the content in markdown format with points on the given topic:

#### HDFS federation in Hadoop ecosystem

1. HDFS federation splits the namespace volume across multiple NameNodes. It essentially scales the namespace horizontally.
2. Each NameNode is independent and manages a portion of the file system namespace. The namespace volumes managed by the NameNodes do not overlap.
3. The Namenodes are federated, that is, the NameNodes are peers and none of them report to the others. There is no single point of failure and the cluster can sustain failure of multiple NameNodes.
4. The Cluster namespace configuration manages the federation by defining the block pools and locating them on the NameNodes. The clients must have the Cluster namespace configuration to navigate the file system namespace and locate the block pools and corresponding NameNodes.
5. HDFS federation provides scalability, isolation, and improved throughput for Hadoop applications. The HDFS capacity and throughput can be scaled by adding more NameNodes and block pools. Isolation also means failure of a NameNode only affects a part of the file system namespace thereby minimizing data loss.
6. HDFS federation is well suited for large clusters and also enables graceful upgrade of HDFS. New NameNodes and software upgrades can be added to the system without disturbing the existing NameNodes and data nodes.

The content is written in formal tone with points and no emojis or external links are included as per the given instructions. The content is written inside the mentioned header in markdown format. Please let me know if you would like me to modify or expand the content.