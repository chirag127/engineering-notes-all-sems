### Unit 3 - MapReduce: Test Data and Local Tests

1. **Test Data:** Test data refers to the data used to test the functionality and performance of a MapReduce program. It is important to use realistic and representative test data to ensure that the program works correctly and efficiently when processing large datasets.

2. **Local Tests:** Local tests refer to running MapReduce programs on a local machine, rather than on a distributed cluster. This can be useful for debugging and testing the program before deploying it on a cluster. Local tests can be performed using tools such as Hadoop's `LocalJobRunner` class, which simulates a MapReduce cluster on a single machine.

3. **Benefits of Local Tests:** Local tests can help developers to quickly identify and fix issues with their MapReduce programs. They can also be used to test the program's performance and scalability on smaller datasets, before running it on larger datasets on a cluster.

4. **Limitations of Local Tests:** While local tests can be useful for debugging and testing MapReduce programs, they do have some limitations. Since they are run on a single machine, they may not accurately reflect the performance and scalability of the program when run on a distributed cluster. Additionally, local tests may not be able to handle very large datasets, due to the limited resources of a single machine.