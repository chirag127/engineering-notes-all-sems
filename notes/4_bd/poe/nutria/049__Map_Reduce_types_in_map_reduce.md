

#### Map Reduce Types in Map Reduce

1. **MapReduce** is a programming model used for processing large datasets. It is based on the concept of dividing a large task into smaller tasks that can be executed in parallel.

2. **Map** is the first step in the MapReduce process. It takes an input dataset and divides it into smaller chunks. The output of the Map phase is a set of key-value pairs.

3. **Reduce** is the second step in the MapReduce process. It takes the output of the Map phase and combines the data into a single result.

4. **Shuffle and Sort** is the third step in the MapReduce process. It takes the output of the Map phase and sorts the data according to the key.

5. **Combiner** is an optional step in the MapReduce process. It is used to reduce the amount of data sent to the Reducer.

6. **Partitioner** is an optional step in the MapReduce process. It is used to determine which Reduce task will receive which key-value pair.

7. **JobTracker** is a server-side component of the MapReduce framework. It is responsible for tracking the status of MapReduce jobs and coordinating the execution of tasks.