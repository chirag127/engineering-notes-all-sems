### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems

A distributed system is a collection of independent computers that appear to its users as a single coherent system. The computers in a distributed system communicate and coordinate their actions only by passing messages. A distributed system has the following characteristics :

- Concurrency of components: The computers in a distributed system can execute programs concurrently, and they need to coordinate their actions to share resources or achieve a common goal.
- Lack of a global clock: The computers in a distributed system do not have a shared notion of time, and they can only synchronize their clocks with a limited accuracy. Therefore, there is no single global notion of the correct time in a distributed system.
- Independent failures of components: The computers in a distributed system can fail independently, leaving the others still running. The failure of a computer or a program is not immediately made known to the other components with which it communicates. The network can also fail, resulting in the isolation of some computers.

The following diagram illustrates the basic architecture of a distributed system:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Computer 1    |      |   Computer 2    |      |   Computer 3    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Program 1     |      |   Program 2     |      |   Program 3     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   OS 1          |      |   OS 2          |      |   OS 3          |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Clock 1       |      |   Clock 2       |      |   Clock 3       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Memory 1      |      |   Memory 2      |      |   Memory 3      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   CPU 1         |      |   CPU 2         |      |   CPU 3         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       +------------------+------------------+
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