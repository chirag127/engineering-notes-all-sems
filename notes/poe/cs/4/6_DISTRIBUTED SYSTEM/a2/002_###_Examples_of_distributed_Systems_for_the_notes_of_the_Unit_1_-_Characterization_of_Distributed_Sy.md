 Here is the content in markdown format for the topic ### Examples of distributed Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Examples of distributed Systems:

-   Distributed database system: Data is distributed across multiple servers. Query processing and transaction management are handled by the database system. Example: MySQL cluster.
-   Distributed file system: Files are distributed across multiple servers. Transparency of file distribution and fault tolerance are handled by the file system. Example: HDFS, GlusterFS.
-   Distributed web crawler: The task of crawling the web is distributed across multiple servers. The servers coordinate with each other to crawl the web efficiently and avoid re-crawling web pages.
-   Peer-to-peer system: There is no centralized server. All nodes in the system act as both clients and servers. Files are located using a distributed hash table. Example: BitTorrent, Freenet.
-   Cloud computing system: Computation is distributed across a large number of servers. Examples: Amazon EC2, Google App Engine.

Advantages of distributed systems:

- Fault tolerance: If one server goes down, the system continues to function using other servers.
- Scalability: It is easy to add more servers to handle higher loads.
- Low latency: Servers can be placed close to clients to reduce latency.

Disadvantages of distributed systems:

- Complexity: Distributed systems are more complex to program and debug.
- Inconsistency: The state of the system may be inconsistent due to delays in propagating updates.
- Partial failures: It is difficult to distinguish between slow servers and failed servers.

Applications of distributed systems:

- Web search engines
- E-commerce systems
- Content delivery networks
- Collaborative systems