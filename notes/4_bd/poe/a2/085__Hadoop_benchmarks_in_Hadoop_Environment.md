 Here is the formal content on the given topic in Markdown format:

#### Hadoop benchmarks in Hadoop Environment

1. Terasort benchmark
- Measures the amount of data that can be sorted by a Hadoop cluster in a given time frame.
- Involves reading data, sorting it and writing it back.
- Tests the MapReduce paradigm and HDFS I/O capabilities.

2. Gridmix benchmark
- Simulates a cluster with multiple jobs running queries and tasks, competing for resources.
- Includes activities like scanning, sorting, joins etc.
- Measures performance under multi-user loads and identifies bottlenecks.

3. Hadoop TestDFSIO
- Tests the maximum throughput of HDFS for file system operations like read, write and append.
- Identifies performance of NameNode and DataNodes under stress.
- Useful for evaluating and tuning HDFS.

4. MRBench
- Analyses performance of multiple MapReduce activities on a Hadoop cluster.
- Includes tests for joins, aggregations, Grep, Terasort etc.
- Provides comparisons of different cluster configurations and scales.

The above points cover some standard benchmarks used to evaluate and optimize the performance of Hadoop clusters involving HDFS and MapReduce functionality. The results of these benchmarks help in configuration tuning and resource planning for Hadoop deployments as per the requirements.