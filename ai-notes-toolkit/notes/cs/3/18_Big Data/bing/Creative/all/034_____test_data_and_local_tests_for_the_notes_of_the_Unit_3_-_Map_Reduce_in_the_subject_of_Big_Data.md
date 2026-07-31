# Test Data and Local Tests for Map Reduce

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- To test Map Reduce applications, it is important to have test data that is representative of the real data and covers various scenarios and edge cases.
- Local tests are useful for debugging and validating the logic of the map and reduce functions before deploying them to a Hadoop cluster.
- There are different ways to perform local tests for Map Reduce applications, depending on the tools and frameworks used.

## Testing with Hadoop Streaming

- Hadoop Streaming is a utility that allows users to write map and reduce scripts in any language that can read from standard input and write to standard output, such as Python, Ruby, Perl, etc.
- To test Hadoop Streaming scripts locally, one can use the following command:

```bash
cat input_file | map_script | sort -k1,1 | reduce_script
```

- This command simulates the Hadoop Streaming process by piping the input file to the map script, sorting the output by key, and piping it to the reduce script.
- The input file should be in the same format as the Hadoop input, and the map and reduce scripts should follow the Hadoop Streaming convention of writing key-value pairs separated by a tab character to standard output .

## Testing with MRUnit

- MRUnit is a Java library that provides a testing framework for writing unit tests for Map Reduce applications.
- MRUnit allows users to create mock input and output data, and run map, reduce, and combiner functions on them in isolation, without setting up a Hadoop cluster.
- MRUnit provides different drivers for testing different components of a Map Reduce job, such as:

  - MapDriver: for testing a mapper class
  - ReduceDriver: for testing a reducer class
  - MapReduceDriver: for testing a map/reduce pair or a combiner class
  - PipelineMapReduceDriver: for testing a workflow of map/reduce jobs

- MRUnit also supports testing with multiple inputs and outputs, counters, configuration, and custom comparators  .

## Testing with MiniCluster

- MiniCluster is a feature of Hadoop that allows users to run a Hadoop cluster on a single machine, using local file system and memory.
- MiniCluster is useful for testing the end-to-end functionality and performance of a Map Reduce application, as it mimics the behavior of a real Hadoop cluster.
- MiniCluster can be configured and launched programmatically using the MiniDFSCluster and MiniMRCluster classes, or using the command-line tool `hadoop jar`.
- MiniCluster requires more resources and setup than MRUnit, but provides more realistic and comprehensive testing.