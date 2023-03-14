#### Test data and local tests in map reduce

- Map reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Testing map reduce applications can be challenging due to the complexity and scale of the data and the distributed nature of the execution.
- One way to simplify testing is to use test data and local tests that can run on a single machine without requiring a hadoop cluster.
- Test data can be generated or sampled from real data sets, depending on the requirements and objectives of the test cases.
- Local tests can use tools and frameworks such as hadoop streaming, MRUnit, and JUnit to test the functionality and performance of the map and reduce functions in isolation or in combination.
- Some examples of local tests are:

  - Using hadoop streaming to pipe data from files to the map and reduce scripts and verify the output. For example: `cat *.csv | map.py | sort -k1,1 | reducer.py`
  - Using MRUnit to create mock inputs and outputs for the map and reduce functions and assert the expected results. MRUnit also provides methods to test counters, configuration, and multiple inputs and outputs.
  - Using JUnit to write unit tests for the map and reduce classes and methods, and use mock objects or stubs to simulate the context and configuration objects.

- Local tests can help to catch bugs and errors early in the development cycle, and improve the quality and reliability of the map reduce applications. However, they are not a substitute for integration and system tests that run on a real hadoop cluster with large-scale data sets.