### Unit 3 - Map Reduce: Unit Tests with MRUnit

1. **MRUnit** is a library that helps developers to write unit tests for Hadoop MapReduce jobs.
2. MRUnit provides a driver class for running MapReduce jobs in a controlled environment, without the need for a full Hadoop cluster.
3. The driver class takes as input the mapper, reducer, and combiner classes, as well as the input and expected output data.
4. The driver class then runs the MapReduce job and compares the actual output with the expected output.
5. MRUnit supports testing of multiple inputs and outputs, counters, and custom partitioners and comparators.
6. MRUnit can be used with popular testing frameworks such as JUnit and TestNG.
7. To use MRUnit, developers need to add the MRUnit library to their project's dependencies and write test cases using the provided driver class.
8. MRUnit helps developers to catch errors and regressions early in the development process, improving the quality and reliability of MapReduce jobs.