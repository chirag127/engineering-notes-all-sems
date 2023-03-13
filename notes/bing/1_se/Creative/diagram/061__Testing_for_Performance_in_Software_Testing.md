Performance testing is a type of software testing that ensures software applications to perform properly under their expected workload. It is a testing technique carried out to determine system performance in terms of speed, response time, stability, reliability, scalability, and resource usage of a software application under a certain workload  .

There are different types of performance testing, such as load testing, stress testing, spike testing, endurance testing, and volume testing . Each type of performance testing has a different goal and scenario. For example, load testing measures system performance as the workload increases, while stress testing measures system performance when the workload exceeds the normal limits .

The basic architecture of a performance testing process can be illustrated by the following diagram:

```
+----------------+       +-----------------+       +----------------+
|                |       |                 |       |                |
|  Test Scripts  +------>+  Test Scenario  +------>+  Test Results  |
|                |       |                 |       |                |
+----------------+       +-----------------+       +----------------+
       ^                        ^                        |
       |                        |                        |
       |                        |                        v
+----------------+       +-----------------+       +----------------+
|                |       |                 |       |                |
|  Test Data     +------>+  Test Execution +------>+  Test Analysis |
|                |       |                 |       |                |
+----------------+       +-----------------+       +----------------+
```

The test scripts are the code or commands that simulate the user actions or requests to the software application. The test scenario is the set of conditions or parameters that define the test objectives, environment, and workload. The test execution is the process of running the test scripts according to the test scenario. The test results are the data or metrics collected during the test execution. The test analysis is the process of evaluating the test results and identifying the performance bottlenecks or issues    .