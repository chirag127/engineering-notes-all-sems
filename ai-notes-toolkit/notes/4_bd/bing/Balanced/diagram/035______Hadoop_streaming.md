Hadoop streaming is a utility that allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. It works by passing the input data to the mapper script as standard input, and collecting the output data from the standard output. Similarly, the reducer script receives the intermediate key-value pairs from the standard input, and writes the final output to the standard output. Hadoop streaming handles the communication between the nodes and the partitioning of the data.

Here is a possible ASCII diagram for Hadoop streaming:

#### Hadoop streaming

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Input data     |     |  Mapper script  |     |  Intermediate   |
|  (HDFS files)   | --> |  (any language) | --> |  key-value pairs|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                                   ||                      ||
                                   ||                      ||
                                   \/                      \/
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Partitioner    |     |  Sort and       |     |  Reducer script |
|  (Java class)   | --> |  Merge (Java)   | --> |  (any language) |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                                   ||                      ||
                                   ||                      ||
                                   \/                      \/
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Output format  |     |  Output data    |     |  Output files   |
|  (Java class)   | --> |  (key-value     | --> |  (HDFS files)   |
|                 |     |  pairs)         |     |                 |
+-----------------+     +-----------------+     +-----------------+
```