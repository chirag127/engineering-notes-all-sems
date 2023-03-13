Acceptance testing is a level of software testing that evaluates the system's compliance with the user needs, requirements, and business processes. It is conducted to determine whether the system satisfies the acceptance criteria and whether the user, customer, or other authorized entity is willing to accept the system. Acceptance testing occurs after system testing, but before deployment. It is usually done manually, with users creating real-world situations and testing how the software reacts and performs.

The following diagram illustrates the basic architecture of acceptance testing in software testing using ASCII characters:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  User/Customer  |       |  Development    |       |  Testing Team   |
|                 |       |  Team           |       |                 |
+-----------------+       +-----------------+       +-----------------+
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |<-----------------------|                        |
        |                        |                        |
        |  Provide user needs,   |                        |
        |  requirements, and     |                        |
        |  business processes    |                        |
        |                        |                        |
        |----------------------->|                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |<-----------------------|
        |                        |                        |
        |                        |  Provide system test   |
        |                        |  results and feedback  |
        |                        |                        |
        |                        |----------------------->|
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |<-----------------------|                        |
        |                        |                        |
        |  Accept or reject the  |                        |
        |  system based on       |                        |
        |  acceptance criteria   |                        |
        |                        |                        |
        |----------------------->|                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
        |                        |                        |
+-----------------+       +-----------------+       +-----------------+
```