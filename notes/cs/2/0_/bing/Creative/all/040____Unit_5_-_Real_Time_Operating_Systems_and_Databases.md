# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can handle data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and resource sharing, but do not guarantee any timing requirements.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to run multiple tasks or threads concurrently, each with its own priority and scheduling policy.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between threads, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, etc.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to protect the memory space of each thread from corruption or interference by other threads.
  - Interrupt handling: The ability to respond to external or internal events that require immediate attention, such as hardware inputs, timers, or exceptions.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, or network interfaces, using standard or custom protocols.
- An RTOS is suitable for applications that have real-time requirements, such as industrial control, embedded systems, robotics, avionics, or multimedia.

## Real Time Databases

- A real time database is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive.
- A real time database is different from a traditional database, which contains data that is persistent and changes much less frequently.
- A real time database typically has the following characteristics :
  - High performance: The ability to write and read data within a strict time bound, usually on the order of seconds to milliseconds.
  - High availability: The ability to maintain data consistency and integrity even in the presence of failures, such as network partitions, power outages, or hardware malfunctions.
  - High scalability: The ability to handle increasing data volumes and concurrent users without compromising performance or availability.
  - High flexibility: The ability to support various data types and structures, such as structured, semi-structured, or unstructured data, and to adapt to changing data schemas and queries.
- A real time database is suitable for applications that need to process and analyze data in real time, such as online transactions, streaming analytics, IoT, or gaming .

## Operational Database

- An operational database is a type of real time database that is oriented toward real-time, transactional operations.
- An operational database is different from a data warehouse, which is a type of traditional database that is oriented toward historical, analytical operations.
- An operational database typically has the following attributes:
  - Low latency: The ability to execute transactions and queries with minimal delay, usually on the order of microseconds to milliseconds.
  - High throughput: The ability to process a large number of transactions and queries per second, usually on the order of thousands to millions.
  - ACID compliance: The ability to ensure that transactions are atomic, consistent, isolated, and durable, meaning that they are executed as a whole, without errors, without interference, and without loss.
  - Data freshness: The ability to reflect the most recent state of the data, without stale or outdated information.
- An operational database is suitable for applications that need to perform real-time, transactional operations on the data, such as e-commerce, banking, or social media.