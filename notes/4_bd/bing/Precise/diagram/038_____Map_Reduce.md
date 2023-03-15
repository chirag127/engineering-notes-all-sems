### Map Reduce

MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the context of MapReduce is not the same.

Here is an ASCII diagram of the MapReduce process:

```
       +--------+     +--------+
       |        |     |        |
       |  Map   |     |  Map   |
       |        |     |        |
       +---+----+     +----+---+
           |               |
           |               |
           v               v
       +---+----+     +----+---+
       |        |     |        |
       | Reduce |     | Reduce |
       |        |     |        |
       +--------+     +--------+
```

In the MapReduce model, the data processing primitives are called mappers and reducers. The input data is split into independent chunks that are processed by the map tasks in a completely parallel manner. The framework sorts the outputs of the maps, which are then input to the reduce tasks. Typically both the input and the output of the job are stored in a distributed file system. The framework takes care of scheduling tasks, monitoring them and re-executing the failed tasks.
