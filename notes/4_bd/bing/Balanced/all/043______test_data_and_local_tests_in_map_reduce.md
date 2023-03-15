#### Test data and local tests in map reduce

- Test data is the input data that is used to test the functionality and performance of a map reduce program. Test data can be generated artificially or obtained from real sources, depending on the requirements and objectives of the testing process.
- Local tests are the tests that are performed on a single machine, without using a distributed system or a cluster. Local tests are useful for debugging and verifying the logic of the map and reduce functions, as well as the data flow and the output format.
- Some of the advantages of local tests are:
  - They are faster and cheaper than running tests on a cluster.
  - They can be easily automated and integrated with development tools and frameworks.
  - They can help identify and fix errors and bugs before deploying the program to a cluster.
- Some of the disadvantages of local tests are:
  - They cannot simulate the distributed environment and the network communication of a cluster.
  - They cannot test the scalability and reliability of the program under different loads and failures.
  - They may not reflect the actual performance and behavior of the program on a cluster.
- Some of the methods and tools for performing local tests are:
  - Using command-line tools and scripts to run the map and reduce functions on sample input data and check the output. For example, if using hadoop streaming, one can test the scripts locally like this:

    `cat *.csv | map.py | sort -k1,1 | reducer.py`

    To pass data from mapper to reducer in hadoop-streaming, simply write `<key>\t<value>` to stdout.
  - Using unit testing frameworks and libraries to write and run test cases for the map and reduce functions. For example, MRUnit is a testing framework that lets you test and debug map reduce jobs in isolation without spinning up a hadoop cluster. MRUnit provides mock objects and methods to simulate the input, output, and context of the map and reduce functions, and to verify the results and expectations.
  - Using local mode or pseudo-distributed mode of hadoop to run the map reduce program on a single node cluster. This can help test the integration and compatibility of the program with the hadoop framework and the configuration parameters. However, this may not be as fast and convenient as the previous methods, and may still require some cluster setup and maintenance.