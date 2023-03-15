#### Map Reduce framework and basics

MapReduce is a programming model and an associated implementation for processing and generating large data sets. The model is inspired by the map and reduce functions commonly used in functional programming, although their purpose in the MapReduce framework is not the same as their original forms.

Here is an ASCII diagram that illustrates the basic flow of data in a MapReduce job:

```
  +--------+     +--------+     +--------+
  |        |     |        |     |        |
  | Mapper |     | Mapper |     | Mapper |
  |        |     |        |     |        |
  +---+----+     +---+----+     +---+----+
      |              |              |
      |              |              |
      v              v              v
  +---+----+     +---+----+     +---+----+
  |        |     |        |     |        |
  |Reducer |     |Reducer |     |Reducer |
  |        |     |        |     |        |
  +---+----+     +---+----+     +---+----+
      |              |              |
      |              |              |
      v              v              v
  +---+----+     +---+----+     +---+----+
  |        |     |        |     |        |
  | Output |     | Output |     | Output |
  |        |     |        |     |        |
  +--------+     +--------+     +--------+
```

In this diagram, the input data is split into multiple chunks and processed by multiple mapper tasks in parallel. The output of the mappers is then shuffled and sorted, and fed into the reducers. The reducers process the data and generate the final output.
