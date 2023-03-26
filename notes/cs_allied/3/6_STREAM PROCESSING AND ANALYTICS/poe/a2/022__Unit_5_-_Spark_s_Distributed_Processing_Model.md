 Here is the formal content in Markdown format without any emojis or external links:

## Unit 5 - Spark’s Distributed Processing Model

1. Spark executes on a cluster of nodes. The driver program coordinates the execution among the nodes.
2. The main abstraction in Spark is a resilient distributed dataset (RDD), which represents a collection of elements partitioned across the nodes of the cluster that can be operated on in parallel.
3. RDDs are created through deterministic operations on data in stable storage (e.g., files in a filesystem) or other RDDs.
4. Spark applications run as independent sets of processes on a cluster, coordinated by the driver program.
5. The driver program splits up processing into a set of stages, where each stage contains multiple tasks to be executed on executor nodes.
6. Data is partitioned across nodes, and tasks on each node work on the data local to that node as much as possible to reduce network I/O.
7. If a node fails, the RDDs on the node are automatically re-computed from original data or other RDDs. This provides fault tolerance.
8. Spark provides several APIs: RDDs API (lower-level), DataFrames API (higher-level), and SQL interface. The APIs have a shared runtime and provide transformations and actions.
9. Spark SQL can be used to query structured data via SQL or HiveQL, and the results are returned as DataFrames. DataFrames can be converted to/from RDDs.
10. Graphics Processing Units (GPUs) can be used to improve performance for certain computations and deep learning via libraries like CUDA and cuDNN.