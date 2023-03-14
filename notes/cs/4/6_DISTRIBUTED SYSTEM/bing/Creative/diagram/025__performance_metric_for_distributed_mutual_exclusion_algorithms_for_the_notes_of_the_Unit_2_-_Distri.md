The following diagram illustrates the basic architecture of a distributed mutual exclusion algorithm:

```
    +-----------------+             +-----------------+
    |                 |             |                 |
    |  Process 1      |             |  Process N      |
    |                 |             |                 |
    +-----------------+             +-----------------+
          |   ^                         |   ^
          |   |                         |   |
          v   |                         v   |
    +-----------------+             +-----------------+
    |                 |             |                 |
    |  Request Queue  |             |  Request Queue  |
    |                 |             |                 |
    +-----------------+             +-----------------+
          |   ^                         |   ^
          |   |                         |   |
          v   |                         v   |
    +-----------------+             +-----------------+
    |                 |             |                 |
    |  Critical       |             |  Critical       |
    |  Section        |             |  Section        |
    |                 |             |                 |
    +-----------------+             +-----------------+
```

The performance metrics for distributed mutual exclusion algorithms are  :

- Response time: The interval of time when a request waits for the end of its critical section execution after its solicitation messages have been delivered.
- Synchronization delay: The time required for the next process to enter the critical section after a process leaves the critical section.
- Message complexity: The number of messages needed to execute each critical section by the process.
- Throughput: The amount at which the system executes requests for the critical section.