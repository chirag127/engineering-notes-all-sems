## Unit 2 - Hadoop and MapReduce

- Hadoop is a platform that allows for distributed storage and processing of large-scale data using a cluster of commodity hardware.
- MapReduce is a programming model and a software framework that facilitates the processing of big data stored on Hadoop Distributed File System (HDFS).
- MapReduce consists of two phases: map and reduce.
  - The map phase takes a set of input data and transforms it into intermediate key-value pairs.
  - The reduce phase takes the intermediate key-value pairs and aggregates them to produce the final output.
- MapReduce works by splitting the input data into chunks and assigning them to different nodes in the cluster, where the map tasks run in parallel.
- The output of the map tasks is then shuffled and sorted by the framework and sent to the reduce tasks, which also run in parallel on different nodes.
- The framework handles the scheduling, monitoring, and fault-tolerance of the tasks, and provides the user with a simple interface to specify the map and reduce functions and the job configuration.
- MapReduce applications can be written in various languages, such as Java, Python, Ruby, etc., using the Hadoop Streaming utility or other APIs.
- MapReduce is suitable for batch processing of large and structured or unstructured data, such as web logs, text documents, social media posts, etc.
- MapReduce can also support other useful features, such as counters, distributed cache, profiling, debugging, data compression, skipping bad records, etc.

Some possible mnemonics and learning tricks for Unit 2 are:

- Remember the word "Hadoop" as "HAve a DOzen Of Pancakes", which implies that Hadoop can handle a lot of data using multiple machines.
- Remember the word "MapReduce" as "MAP and REDUCE", which implies that MapReduce consists of two main phases: map and reduce.
- Remember the map phase as "MApping data to key-value pairs", which implies that the map phase transforms the input data into intermediate key-value pairs.
- Remember the reduce phase as "REDUCing key-value pairs to output", which implies that the reduce phase aggregates the intermediate key-value pairs to produce the final output.
- Remember the shuffle and sort phase as "SHUFFLE and SORT the cards", which implies that the shuffle and sort phase distributes and orders the intermediate key-value pairs by their keys.