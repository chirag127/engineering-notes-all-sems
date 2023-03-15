 Here is the content in markdown format for the topic ### Examples of distributed Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Examples of distributed Systems

Some common examples of distributed systems are:

1. Internet - The internet is a distributed system that connects millions of smaller networks and enables communication between them.
2. Web - The World Wide Web is a distributed system of interlinked hypertext documents that can be accessed via the internet.
3. Distributed databases - Databases that have their data and processing distributed across multiple servers. Eg: MySQL cluster, Cassandra, HBase, etc.
4. Distributed file systems - File systems that allow accessing and managing files distributed across multiple servers. Eg: HDFS, GlusterFS, Ceph, etc.
5. Cloud computing platforms - Cloud platforms like AWS, Azure, GCP that provide on-demand computing resources distributed across data centers.
6. Peer-to-peer networks - Networks where nodes share resources like bandwidth, storage, etc directly with each other instead of a central server. Eg: BitTorrent, Bitcoin, etc.

Some key characteristics of distributed systems are:

1. Concurrency - Components interact and operate concurrently.
2. Lack of a global clock - Components can't rely on a synchronized global clock.
3. Independent failures - Components can fail independently, so the system must be fault-tolerant.
4. Dynamic membership - Components can join or leave the system, so the system must be able to adapt to changes.

Advantages of distributed systems:

1. Scalability - It is easy to scale by adding more machines to the cluster.
2. Fault tolerance - The system can tolerate failures of individual machines since processing is distributed.
3. Low latency - Computation and data can be placed close to clients to reduce latency.

Disadvantages of distributed systems:

1. Complexity - Distributed systems are more complex to build and debug.
2. Partial failures - It is difficult to handle and recover from partial failures.
3. Consistency - It is challenging to maintain consistency across the system.
4. Security - Distributed systems introduce additional security vulnerabilities.