#### Task Execution in Map Reduce

Here is an ASCII diagram that illustrates the task execution in MapReduce:

```
       +----------------+
       |  Input Data    |
       +-------+--------+
               |
               |
               v
       +-------+--------+
       |   Map Tasks    |
       +-------+--------+
               |
               |
               v
       +-------+--------+
       |Shuffle & Sort  |
       +-------+--------+
               |
               |
               v
       +-------+--------+
       |  Reduce Tasks  |
       +-------+--------+
               |
               |
               v
       +-------+--------+
       |  Output Data   |
       +----------------+
```

In MapReduce, the input data is first divided into splits and assigned to map tasks. The map tasks process the data and generate intermediate key-value pairs. These key-value pairs are then shuffled and sorted, and assigned to reduce tasks. The reduce tasks process the data and generate the final output.
