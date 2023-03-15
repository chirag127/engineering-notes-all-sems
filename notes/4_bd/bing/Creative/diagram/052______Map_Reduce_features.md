MapReduce is a programming model and a framework for processing large-scale data sets in parallel and distributed manner. It consists of two main phases: map and reduce. The map phase applies a user-defined function to each input record and produces a set of intermediate key-value pairs. The reduce phase aggregates the intermediate values associated with the same key and produces the final output. Some of the salient features of MapReduce are  :

- Scalability: MapReduce can handle huge amounts of data by distributing it across multiple nodes in a cluster. It can also scale up or down depending on the data size and the available resources.
- Flexibility: MapReduce can process various types of data, such as structured, semi-structured, or unstructured, and support different kinds of operations, such as filtering, sorting, grouping, joining, or aggregation.
- Security and Authentication: MapReduce can provide security and authentication mechanisms to protect the data and the access to the cluster. For example, it can use Kerberos or SSL to encrypt the data and authenticate the users and nodes.
- Cost-effectiveness: MapReduce can run on commodity hardware and open-source software, which reduces the cost of infrastructure and maintenance. It can also utilize the idle resources of the cluster and optimize the performance and efficiency.
- Fast: MapReduce can parallelize the computation and reduce the network communication by performing the map and reduce tasks close to the data. It can also leverage the in-memory processing and caching techniques to speed up the execution.
- Simplicity: MapReduce provides a simple and intuitive programming model that abstracts the complexity of distributed computing. The users only need to specify the map and reduce functions and the framework handles the rest of the details, such as data partitioning, scheduling, fault tolerance, or load balancing.
- Parallelism: MapReduce can exploit the parallelism inherent in the data and the computation by running multiple map and reduce tasks concurrently on different nodes. It can also adjust the level of parallelism dynamically according to the data size and the cluster capacity.
- Availability and Resilience: MapReduce can ensure the availability and resilience of the data and the computation by replicating the data across multiple nodes and by recovering from failures automatically. It can also handle the heterogeneity and the variability of the nodes and the network.

#### Map Reduce features

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Input data   |    | Intermediate   |    |   Output data  |
|                |    | key-value pairs|    |                |
+----------------+    +----------------+    +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+------+-----+-----+          |                      |
|     |     |     |          |                      |
| M1  | M2  | M3  |          |                      |
|     |     |     |          |                      |
+-----+-----+-----+          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       |     |     |          |                      |
       +-----+-----+          |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             |                |                      |
             +----------------+                      |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        |                            |
                        +------+-----+-----+          |
                        |     |     |     |          |