### Task Execution for the Notes of the Unit 3 - Map Reduce in the Subject of Big Data

- MapReduce is a programming model that allows processing and generating big data sets with a parallel, distributed algorithm on a cluster.
- MapReduce consists of two phases: Map and Reduce.
- Map phase: This is the first phase in the execution of a MapReduce job. In this phase, the input data is split into small subsets of data called input splits. Each input split is assigned to a map task that runs on a node in the cluster. The map task applies a user-defined function to each record in the input split and produces a set of intermediate key-value pairs. The intermediate data is stored in the local disk of the node .
- Reduce phase: This is the second phase in the execution of a MapReduce job. In this phase, the intermediate data from the map tasks is shuffled and sorted by key and then sent to the reduce tasks. Each reduce task works on a subset of keys and applies a user-defined function to the values associated with each key. The reduce task produces a set of final key-value pairs as the output of the MapReduce job .
- MapReduce has the following features and advantages:
  - It can handle large-scale data sets that are distributed across multiple nodes in a cluster.
  - It can exploit the parallelism and locality of the data processing by running the map and reduce tasks on the nodes that have the input data or are close to them.
  - It can handle the failures and faults of the nodes by re-executing the failed or slow tasks on other nodes.
  - It can abstract the complexity of the distributed computing from the user by providing a simple and expressive programming model .
- MapReduce has the following applications and uses:
  - It can be used for various data analysis tasks such as word count, web log analysis, inverted index, recommendation systems, machine learning, etc.
  - It can be used for data transformation tasks such as filtering, sorting, joining, aggregating, etc.
  - It can be used for data mining tasks such as clustering, classification, pattern matching, etc.
  - It can be used for data visualization tasks such as generating graphs, charts, maps, etc .