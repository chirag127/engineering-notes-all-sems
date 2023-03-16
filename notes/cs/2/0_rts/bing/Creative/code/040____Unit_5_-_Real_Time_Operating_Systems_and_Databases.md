# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and resource sharing, but do not guarantee any timing requirements.
- An RTOS typically has the following features:
  - Real-time multithreading: The ability to run multiple tasks concurrently, each with its own priority and deadline.
  - Inter-thread communication and synchronization: The ability to exchange data and coordinate actions between different tasks, using mechanisms such as message queues, semaphores, mutexes, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, without causing memory fragmentation or affecting performance.
  - Interrupt handling: The ability to respond to external events, such as hardware signals or timers, with minimal latency and overhead.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, or network interfaces, using standard or custom protocols.
- Some examples of applications that use RTOS are industrial control, telephone switching, flight control, and real-time simulations.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can perform read and write operations within a strict performance envelope, usually defined on the order of seconds to milliseconds.
- An RTDB is different from a conventional database, such as Oracle or MySQL, which are designed for batch processing, data warehousing, and business analytics, but do not guarantee any timing requirements.
- An RTDB typically has the following features:
  - Temporal consistency: The ability to maintain the validity and freshness of data, which may change over time or expire after a certain period.
  - Concurrency control: The ability to handle multiple transactions that access or modify the same data, while ensuring data integrity and isolation.
  - Scheduling: The ability to assign priorities and deadlines to transactions, and execute them in an optimal order, while avoiding conflicts and deadlocks.
  - Recovery: The ability to restore the database to a consistent state, in case of failures or errors, without violating the timing constraints.
- Some examples of applications that use RTDB are stock trading, online gaming, sensor networks, and multimedia systems.