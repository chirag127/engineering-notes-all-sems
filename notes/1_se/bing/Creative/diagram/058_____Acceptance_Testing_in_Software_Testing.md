Acceptance testing is a level of software testing where a system is tested for acceptability. The purpose of this test is to evaluate the system’s compliance with the business requirements and assess whether it is acceptable for delivery. There are different types of acceptance testing, such as user acceptance testing, operational acceptance testing, contract acceptance testing, and regulatory acceptance testing.

A possible ASCII diagram for acceptance testing in software testing is:

```
+-----------------+       +-----------------+       +-----------------+
| Business        |       | Development     |       | Testing         |
| Requirements    |       | Team            |       | Team            |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| 1. Define       |       | 4. Develop      |       | 7. Test         |
| acceptance      |       | system based on |       | system based on |
| criteria        |       | acceptance      |       | acceptance      |
|                 |       | criteria        |       | criteria        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |                         |                         |
        |------------------------>|                         |
        | 2. Communicate         |                         |
        | acceptance criteria    |                         |
        | to development team    |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |------------------------>|
        |                        | 5. Communicate          |
        |                        | acceptance criteria     |
        |                        | to testing team         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |<-----------------------|                         |
        | 3. Review and approve  |                         |
        | system design          |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |<------------------------|
        |                        | 6. Review and approve   |
        |                        | test cases and results  |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
        |                        |                         |
+-----------------+       +-----------------+       +-----------------+
| Business        |       | Development     |       | Testing         |
| Stakeholders    |       | Team            |       | Team            |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
| 8. Conduct      |       |                 |       |                 |
| acceptance      |       |                 |       |                 |
| testing on      |       |                 |       |                 |
| system          |       |                 |       |                 |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```