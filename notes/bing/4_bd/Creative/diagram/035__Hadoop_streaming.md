Hadoop streaming is a utility that allows you to create and run MapReduce jobs with any executable or script as the mapper and/or the reducer. It works by passing the input data to the mapper script as standard input, and collecting the output data from the standard output. Similarly, the reducer script receives the intermediate key-value pairs from the standard input, and writes the final output to the standard output. Hadoop streaming handles the communication between the nodes and the partitioning of the data.

#### Hadoop streaming diagram

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input data    |     |  Mapper script |     |  Reducer script|
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +--------+-------+
        |                      |                       |
        |                      |                       |
        |                      v                       v
        |               +------+-------+        +------+-------+
        |               |              |        |              |
        +-------------->|  Hadoop      |        |  Hadoop      |
                        |  streaming   +------->|  streaming   |
                        |              |        |              |
                        +------+-------+        +------+-------+
                               |                       |
                               |                       |
                               v                       v
                        +------+-------+        +------+-------+
                        |              |        |              |
                        |  Intermediate|        |  Final output|
                        |  key-value   |        |  data        |
                        |  pairs       |        |              |
                        |              |        |              |
                        +--------------+        +--------------+
```