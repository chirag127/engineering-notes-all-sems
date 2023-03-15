### Unit 3 - Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is a framework for distributed computing on large datasets on clusters of computers.

Here are some key points to understand about the MapReduce framework:

1. MapReduce is a two-step process: the Map step and the Reduce step.
2. In the Map step, the input data is divided into chunks and processed in parallel by multiple map tasks. Each map task processes a chunk of the input data and produces a set of intermediate key-value pairs.
3. In the Reduce step, the intermediate key-value pairs are grouped by key and processed by reduce tasks. Each reduce task processes all the values associated with a single key and produces a set of output values.
4. The MapReduce framework takes care of scheduling the tasks, monitoring their progress, and re-executing failed tasks.
5. The framework is designed to be fault-tolerant and scalable, allowing it to handle large datasets on clusters of computers.
6. MapReduce is commonly used for processing large datasets in applications such as data mining, log analysis, and web indexing.
