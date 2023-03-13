The following is a detailed ASCII diagram for Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM.

### Introduction

A distributed system is a system that consists of multiple autonomous computers that communicate with each other via messages. The computers may have different operating systems, hardware, and network configurations, but they cooperate to provide a unified service to the users. A distributed system may have the following characteristics:

- Concurrency: The computers can execute multiple tasks simultaneously and independently.
- Scalability: The system can handle increasing workload and number of computers without degrading performance or reliability.
- Fault tolerance: The system can cope with failures of some computers or network links without affecting the overall functionality.
- Transparency: The system hides the details of its internal structure and communication from the users and applications.

The following diagram illustrates the basic architecture of a distributed system:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application    |     |  Application    |     |  Application    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Middleware     |     |  Middleware     |     |  Middleware     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Operating      |     |  Operating      |     |  Operating      |
|  System         |     |  System         |     |  System         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Hardware       |     |  Hardware       |     |  Hardware       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       +--------------------+--------------------+
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |