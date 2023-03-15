# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and user interaction, but do not guarantee a timely response to external stimuli.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to run multiple tasks concurrently, each with its own priority and scheduling policy, and to switch between them with minimal overhead.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between tasks, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to protect the memory space of each task from corruption or interference by other tasks.
  - Interrupt handling: The ability to respond to hardware or software interrupts quickly and deterministically, and to resume the interrupted task without losing its state or timing.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, or network interfaces, using standard or custom protocols and APIs.
- An RTOS is suitable for applications that require high reliability, predictability, and performance, such as industrial control, embedded systems, robotics, aerospace, medical devices, and real-time simulations.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive.
- A RTDB is different from a conventional database, such as Oracle or MySQL, which are designed for persistent and consistent data storage, but do not guarantee a timely response to data queries or updates.
- A RTDB typically has the following features :
  - Data freshness: The ability to maintain the validity and accuracy of data, despite frequent changes and updates, and to provide the most recent data to the users or applications.
  - Data timeliness: The ability to process data queries or updates within a predefined deadline, and to notify the users or applications of any delays or failures.
  - Data concurrency: The ability to support multiple users or applications accessing or modifying the same data simultaneously, and to resolve any conflicts or inconsistencies using mechanisms such as locking, versioning, or timestamping.
  - Data availability: The ability to ensure the accessibility and durability of data, despite any failures or disruptions in the system, and to recover from any data loss or corruption using mechanisms such as replication, backup, or checkpointing.
- A RTDB is suitable for applications that require real-time analysis, decision making, or action, such as online gaming, stock trading, e-commerce, social media, or IoT.