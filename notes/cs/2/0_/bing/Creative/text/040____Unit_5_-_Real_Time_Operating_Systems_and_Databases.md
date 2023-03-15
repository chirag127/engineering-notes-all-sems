## Unit 5 - Real Time Operating Systems and Databases

- A **real-time operating system (RTOS)** is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations  .
- An RTOS is different from a general-purpose operating system, such as Windows or Linux, which are designed for multitasking and user interaction, and do not guarantee predictable response times.
- An RTOS typically has the following features  :
  - **Real-time multithreading**: The ability to run multiple tasks or threads concurrently, each with its own priority and scheduling policy.
  - **Inter-thread communication and synchronization**: The ability to exchange data and coordinate actions between threads using mechanisms such as message queues, semaphores, mutexes, and events.
  - **Memory management**: The ability to allocate and deallocate memory dynamically, and to protect the memory space of each thread from interference by other threads.
  - **Interrupt handling**: The ability to respond to external or internal signals that require immediate attention, such as hardware events, timers, or software exceptions.
  - **Input/output management**: The ability to access and control peripheral devices, such as sensors, actuators, displays, and network interfaces, using drivers and protocols.
  - **Power management**: The ability to conserve energy and extend battery life by adjusting the CPU frequency, voltage, and sleep modes according to the workload and system state.
- A **real-time database** is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock prices, or online transactions .
- A real-time database is different from a traditional database, which contains data that is persistent and changes less frequently, such as customer records, product catalogs, or historical data.
- A real-time database typically has the following characteristics :
  - **High performance**: The ability to process a large number of transactions or queries per second, with low latency and high throughput.
  - **High availability**: The ability to maintain data consistency and reliability in the presence of failures, such as network partitions, node crashes, or disk errors.
  - **High scalability**: The ability to handle increasing data volumes and user demands by adding more nodes or resources to the system, without compromising performance or availability.
  - **High flexibility**: The ability to support different data models and query languages, such as SQL or NoSQL, and to adapt to changing data schemas and application requirements.
  - **High security**: The ability to protect data from unauthorized access, modification, or deletion, using encryption, authentication, and authorization mechanisms.