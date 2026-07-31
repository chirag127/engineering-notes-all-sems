
### Resilient Distributed Datasets in Spark for the notes of the Unit 6 - Spark’s Resilience Model in the subject of STREAM PROCESSING AND ANALYTICS

* Resilient Distributed Datasets (RDDs) are the fundamental data structures of Apache Spark. They are immutable, meaning they cannot be changed once they are created.
* RDDs are distributed across the cluster, allowing for parallel processing of data.
* RDDs can be created from files, databases, or existing RDDs.
* RDDs are resilient, meaning they can be recovered from failure. This is done by tracking lineage information, which is used to recreate lost data.
* Spark’s resilience model is based on the concept of fault-tolerance. This means that the data stored in RDDs can be recovered in the event of a node failure.
* The data stored in RDDs is also replicated across multiple nodes, ensuring that the data is still available even if a node fails.
* RDDs can also be partitioned, meaning that the data is split across multiple nodes. This allows for parallel processing of data, which can improve performance.
* Spark also supports data locality, meaning that data can be stored on nodes that are close to the nodes that need to process it. This can further improve performance.