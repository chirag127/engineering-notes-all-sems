### Unit 3 - Map Reduce

MapReduce is a programming model and an associated implementation for processing and generating large data sets. It is designed to work with large datasets across a large number of nodes. Here is how MapReduce works:

1. **Input data is divided into pieces**: MapReduce generally divides input data into pieces and distributes them among other computers. The input data is broken up into key-value pairs.

2. **Map task**: On computers in a cluster, parallel map jobs process the chunked data. The Map task takes a set of data and converts it into another set of data, where individual elements are broken down into tuples (key-value pairs).

3. **Reduce task**: After all the mappers complete processing, the framework shuffles and sorts the results before passing them on to the reduce tasks. The reduce task takes the output from the map task and combines the data tuples into a smaller set of tuples.

4. **Output**: The output of the reduce task is the final result of the MapReduce job.

MapReduce can perform distributed and parallel computations using large datasets across a large number of nodes. A MapReduce job usually splits the input datasets and then process each of them independently by the Map tasks in a completely parallel manner. The output is then sorted and input to reduce tasks.