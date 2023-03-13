Task execution in map reduce is the process of running a map reduce job on a cluster of nodes. A map reduce job consists of a map function and a reduce function, which are applied to a set of input data to produce a set of output data. The map function takes a key-value pair as input and produces a list of intermediate key-value pairs as output. The reduce function takes a key and a list of values associated with that key as input and produces a list of output values for that key.

The following diagram illustrates the basic architecture of a map reduce job using ASCII art:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input data    |     |  Input data    |     |  Input data    |
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +-------+--------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-------+--------+     +-------+--------+     +-------+--------+
|                |     |                |     |                |
|  Map task      |     |  Map task      |     |  Map task      |
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +-------+--------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +---------------------->                      |
        |                      |                      |
        +-------------------------------------------->|
        |                      |                      |
        v                      v                      v
+-------+--------+     +-------+--------+     +-------+--------+
|                |     |                |     |                |
|  Reduce task   |     |  Reduce task   |     |  Reduce task   |
|                |     |                |     |                |
+-------+--------+     +-------+--------+     +-------+--------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Output data   |     |  Output data   |     |  Output data   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The map reduce framework takes care of scheduling tasks, monitoring them and re-executing the failed tasks. The framework also sorts the outputs of the map tasks, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a file-system .