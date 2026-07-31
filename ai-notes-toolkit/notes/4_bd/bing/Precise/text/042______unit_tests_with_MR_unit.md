#### Unit Tests with MR Unit

- MRUnit is a library that helps developers to write unit tests for Hadoop MapReduce jobs.
- MRUnit provides a driver class that runs the map or reduce function in isolation and feeds it input data.
- The output of the map or reduce function is captured and can be compared to the expected output.
- MRUnit supports testing of map, reduce, and combiner functions, as well as testing of complete MapReduce jobs.
- MRUnit can be used to test jobs that use the old and the new MapReduce APIs.
- MRUnit tests are written in Java and are run using JUnit.
- MRUnit tests are fast to run because they do not require a Hadoop cluster.
- MRUnit tests can help developers to catch errors early in the development process, before the job is run on a cluster.
