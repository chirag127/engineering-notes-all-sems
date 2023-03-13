#### Test data and local tests in map reduce

- Map reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Test data is a set of input data that is used to verify the correctness and performance of a map reduce program.
- Local tests are tests that run on a single machine, using a local file system and a local map reduce framework, such as Hadoop's LocalJobRunner.
- Local tests are useful for debugging and testing map reduce programs before deploying them to a cluster.
- Local tests have some advantages and disadvantages compared to cluster tests:

  - Advantages:
    - Faster and easier to set up and run
    - No need for network or cluster resources
    - Easier to inspect intermediate and final outputs
    - Easier to attach a debugger or a profiler
  - Disadvantages:
    - Cannot test the scalability and reliability of the program
    - Cannot test the interaction with distributed file systems, such as HDFS
    - Cannot test the behavior under different cluster configurations and parameters
    - May not catch some errors or bugs that only occur in a distributed environment

- To perform local tests, one needs to:

  - Generate or obtain test data that is representative of the real data
  - Write a driver class that configures and runs the map reduce job locally
  - Specify the input and output paths as local file system paths
  - Set the map reduce framework to local mode by setting the property `mapreduce.framework.name` to `local`
  - Run the driver class as a Java application
  - Examine the output files and logs for correctness and performance