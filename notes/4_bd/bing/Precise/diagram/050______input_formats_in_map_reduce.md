#### Input Formats in MapReduce

Here is an ASCII diagram that illustrates the input formats in MapReduce:

```
+----------------+     +----------------+
|                |     |                |
|  InputFormat   |     |  InputSplit    |
|                |     |                |
+-------+--------+     +--------+-------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-------+--------+     +--------+-------+
|                |     |                |
|  RecordReader  |     |  Mapper        |
|                |     |                |
+----------------+     +----------------+
```

In MapReduce, an `InputFormat` is responsible for defining how input data is split into `InputSplits` and how these splits are read by the `RecordReader`. The `RecordReader` reads the data from the `InputSplit` and converts it into key-value pairs that are fed into the `Mapper` for processing.
