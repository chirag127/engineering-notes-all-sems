MapReduce is a programming model and a software framework for processing large amounts of data in parallel and distributed manner. It consists of two phases: map and reduce. The map phase applies a user-defined function to each input key-value pair and produces a set of intermediate key-value pairs. The reduce phase applies another user-defined function to all the values that share the same key and produces a set of output key-value pairs. The MapReduce framework handles the partitioning, shuffling, sorting and fault-tolerance of the data and tasks.

The following diagram illustrates the basic architecture of a MapReduce program using ASCII art:

```
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  Input Data 1   |     |  Input Data 2   |     |  Input Data 3   |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
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
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |     Map Task    |     |     Map Task    |     |     Map Task    |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
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
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    | Intermediate KV |     | Intermediate KV |     | Intermediate KV |
    |     Pairs 1     |     |     Pairs 2     |     |     Pairs 3     |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
            |                      |                      |
            |                      |                      |
            |                      |                      |
            |                      |                      |
            |                      |                      |
            |                      |                      |
            |                      |                      |
            |                      |                      |
            +----------------------+----------------------+------------------+
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           |
                                           v
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |     Reduce      |     |     Reduce      |     |     Reduce      |
    |      Task 1     |     |      Task 2     |     |      Task 3     |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
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
    +-----------------+     +-----------------+     +-----------------+
    |                 |     |                 |     |                 |
    |  Output Data 1  |     |  Output Data 2  |     |  Output Data 3  |
    |                 |     |                 |     |                 |
    +-----------------+     +-----------------+     +-----------------+
```