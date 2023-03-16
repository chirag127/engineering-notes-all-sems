# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and resource sharing, but do not guarantee any timing requirements.
- An RTOS typically has the following features:
  - Real-time multithreading: The ability to run multiple tasks concurrently, each with its own priority and deadline.
  - Inter-thread communication and synchronization: The ability to exchange data and coordinate actions between different tasks, using mechanisms such as message queues, semaphores, mutexes, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, without causing memory fragmentation or affecting performance.
  - Interrupt handling: The ability to respond to external events, such as hardware signals or user inputs, in a timely and predictable manner.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, displays, and network interfaces, using standard or custom protocols.
- Some examples of RTOS are Azure RTOS, FreeRTOS, VxWorks, QNX, and RTEMS.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can handle transactions and queries that have time constraints, such as deadlines, freshness, or validity.
- An RTDB is different from a conventional database, such as Oracle or MySQL, which are designed for data consistency and reliability, but do not guarantee any timing requirements.
- An RTDB typically has the following features:
  - Real-time transactions: The ability to execute a sequence of operations on the database, such as read, write, or update, within a specified deadline, and to abort or rollback if the deadline is missed.
  - Real-time queries: The ability to retrieve data from the database, such as select, join, or aggregate, within a specified deadline, and to return partial or approximate results if the deadline is missed.
  - Data freshness: The ability to maintain the temporal validity of the data in the database, such as timestamps, expiration, or versioning, and to discard or update stale or obsolete data.
  - Data replication: The ability to distribute the data across multiple nodes or sites, such as clusters, clouds, or edge devices, and to synchronize the data in a timely and consistent manner.
  - Data security: The ability to protect the data from unauthorized access, modification, or deletion, using mechanisms such as encryption, authentication, or authorization.
- Some examples of RTDB are ScyllaDB, MongoDB, Cassandra, and Redis.