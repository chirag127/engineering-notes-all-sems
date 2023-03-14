Pig is a high-level platform or tool which is used to process large datasets. It provides a high-level of abstraction for processing over the MapReduce. It provides a high-level scripting language, known as Pig Latin which is used to develop the data analysis codes. Pig Latin and Pig Engine are the two main components of the Apache Pig tool. The following diagram illustrates the basic architecture of Pig:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Pig Latin    |       |    Pig Engine   |       |    MapReduce    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Script/Query   |       |                 |       |                 |
|                 |       |                 |       |                 |
|  Grunt Shell    |       |                 |       |                 |
|                 |       |                 |       |                 |
|  UDFs           |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |  Parser         |       |                 |
|                 |       |                 |       |                 |
|                 |       |  Optimizer      |       |                 |
|                 |       |                 |       |                 |
|                 |       |  Compiler       |       |                 |
|                 |       |                 |       |                 |
|                 |       |  Executor       |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |  Mapper         |
|                 |       |                 |       |                 |
|                 |       |                 |       |  Reducer        |
|                 |       |                 |       |                 |
|                 |       |                 |       |  Combiner       |
|                 |       |                 |       |                 |
|                 |       |                 |       |  Partitioner    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|                 |       |                 |       |  HDFS           |
|                 |       |                 |       |                 |
|                 |       |                 |       |  Local FS       |
|                 |       |                 |       |                 |
|                 |       |                 |       |  Other sources  |
|                 |       |                 |       |                 |
|                 |       |                 |       |  Other sinks    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```