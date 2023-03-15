# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed to optimize the average performance and resource utilization, but not the worst-case performance or predictability.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to run multiple tasks or threads concurrently, each with its own priority and scheduling policy.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between threads, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, etc.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to protect the memory regions of different threads from each other.
  - Interrupt handling: The ability to respond to external events, such as hardware interrupts or software exceptions, in a timely and deterministic manner.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, network interfaces, etc., using standard or custom protocols.
  - System services: The ability to provide common functionalities, such as file systems, networking, timers, logging, etc., to the application threads.
- Some examples of RTOS are Azure RTOS, FreeRTOS, VxWorks, QNX, etc.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive.
- A RTDB is different from a conventional database, which is designed to store and process data that is persistent and changes much less frequently.
- A RTDB typically has the following attributes:
  - Live data: The data in a RTDB is continuously updated by external sources, such as sensors, devices, or users, and reflects the current state of the real world.
  - Time constraints: The data in a RTDB has associated deadlines or validity intervals, which specify how long the data is relevant or useful for the application.
  - Predictable performance: The RTDB is able to write and/or read data within a strict performance envelope, usually defined on the order of seconds to milliseconds.
  - High availability: The RTDB is able to tolerate failures and maintain data consistency and integrity across multiple nodes or replicas.
  - Scalability: The RTDB is able to handle increasing volumes and velocities of data without compromising the performance or availability.
- Some examples of RTDB are ScyllaDB, Raima, InfluxDB, MongoDB, etc.