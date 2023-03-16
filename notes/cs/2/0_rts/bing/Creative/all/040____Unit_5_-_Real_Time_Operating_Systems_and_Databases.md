# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed to optimize the average performance and resource utilization, but not the worst-case performance or predictability.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to create and manage multiple tasks or threads that can run concurrently and independently, each with its own priority and deadline.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between threads, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to prevent memory fragmentation and leaks.
  - Interrupt handling: The ability to respond to external or internal events that require immediate attention, such as hardware inputs or timers, and to resume the normal execution afterwards.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, displays, and network interfaces, and to provide a uniform and abstracted access to them.
- Some examples of applications that use RTOS are industrial control, telephone switching, flight control, and real-time simulations.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can perform transactions and queries with real-time constraints.
- A real-time constraint is a requirement that a database operation must be completed within a specified time interval, or else it is considered invalid or obsolete.
- A RTDB is different from a conventional database, such as Oracle or MySQL, which are designed to optimize the throughput and consistency, but not the timeliness or freshness of the data.
- A RTDB typically has the following features:
  - Real-time transactions: The ability to execute database operations, such as insert, update, delete, and select, with deadlines and priorities, and to abort or restart them if they miss their deadlines or encounter conflicts.
  - Real-time queries: The ability to retrieve data from the database with temporal constraints, such as freshness, validity, and accuracy, and to handle data inconsistencies or uncertainties.
  - Real-time data: The ability to store and manage data that have temporal properties, such as timestamps, expiration dates, and versions, and to reflect the changes in the external environment or the internal state of the system.
  - Real-time concurrency control: The ability to coordinate the access and modification of the data by multiple transactions or queries, and to prevent or resolve data conflicts, such as deadlock, starvation, or inconsistency.
- Some examples of applications that use RTDB are stock market, air traffic control, online gaming, and sensor networks.