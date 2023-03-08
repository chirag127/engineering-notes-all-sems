 Here is the content in markdown format:

#### Map Reduce framework and basics

Map Reduce is a programming model and an associated implementation for processing and generating large data sets. It works in two phases:

1. Map phase: In this phase, the input data is divided into smaller chunks which are processed in parallel by multiple mapper tasks. Each mapper processes an independent partition of the input data and generates intermediate key-value pairs.

- The input data can be in the form of <key, value> pairs.
- The mapper processes each input pair and generates zero or more output pairs of the form <key, value>.
- The output pairs are then sorted and shuffled to send each pair to the reducer whose key matches.

2. Reduce phase: In this phase, the reducer tasks aggregate the values for each key and produce the final output. The number of reducers is configurable and can be adjusted based on the computation requirements.

- The input to the reducer is the aggregated values for each key.
- The reducer processes all the values for a given key and generates zero or more output pairs.
- The outputs of the reducers are the final output of the Map Reduce job.

Advantages:

- Scalability: Map Reduce is scalable to large clusters with thousands of nodes. It can handle petabytes of data.
- Fault tolerance: Map Reduce is fault tolerant and can handle failures of nodes or tasks. The tasks are re-executed on other nodes to complete the job.
- Locality: It tries to schedule the tasks on the nodes where the input data resides to minimize data transfers and takes advantage of data locality.
- Simplicity: The programming model is simple with map and reduce abstractions which makes it easy to parallelize and distribute computations.

Applications: Map Reduce is suited for processing large volumes of data and is used in various applications such as:

- Web indexing
- Log processing
- Data mining
- Machine learning
- Graph processing
- etc.