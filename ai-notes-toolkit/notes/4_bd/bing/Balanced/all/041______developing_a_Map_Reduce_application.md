#### Developing a Map Reduce application

- MapReduce is a framework for processing parallelizable problems across large datasets using a large number of computers (nodes), collectively referred to as a cluster or a grid.
- Writing a program in MapReduce follows a certain pattern. You start by writing your map and reduce functions, ideally with unit tests to make sure they do what you expect .
- A map function takes a key-value pair as input and produces zero or more key-value pairs as output. A reduce function takes a key and a list of values as input and produces zero or more key-value pairs as output .
- A MapReduce application consists of the following components:
  - A driver class that configures and runs the job.
  - A mapper class that implements the map function.
  - A reducer class that implements the reduce function.
  - Optionally, a combiner class that implements a local aggregation function to reduce the amount of data transferred between the mapper and the reducer.
  - Optionally, a partitioner class that determines how the mapper output keys are partitioned among the reducers.
  - Optionally, a comparator class that defines the sort order of the mapper output keys.
- A MapReduce application can be run locally or in a cluster on test data. To run locally, you need to set the configuration property `mapreduce.framework.name` to `local`. To run in a cluster, you need to set it to `yarn`.
- A MapReduce application can be run using the `hadoop jar` command or using the `ToolRunner` class that provides some common command-line options  .
- A MapReduce application can be monitored and debugged using the MapReduce web UI, the Hadoop logs, and the counters that track the progress and statistics of the job  .
- A MapReduce application can be tuned to improve performance by adjusting the number of mappers and reducers, using compression, using custom data types, using custom input and output formats, and using combiners and partitioners  .

- A possible mnemonic to remember the components of a MapReduce application is **DR MAP COP** (Driver, Reducer, Mapper, Combiner, Partitioner, Comparator).
- A possible learning trick to understand the MapReduce framework is to use a word count example, where the map function emits each word and its count as one, and the reduce function sums up the counts for each word .