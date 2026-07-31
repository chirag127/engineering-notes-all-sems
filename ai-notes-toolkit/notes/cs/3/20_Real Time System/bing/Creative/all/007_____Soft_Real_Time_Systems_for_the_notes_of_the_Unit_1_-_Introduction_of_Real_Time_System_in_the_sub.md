# Soft Real Time Systems

- A soft real time system is a system that has a **flexible deadline** for completing its tasks, meaning that it can tolerate some **delay** or **jitter** in the execution time without causing a **system failure** or a **significant degradation** in the quality of service   .
- A soft real time system is typically used to handle **concurrent** and **dynamic** situations where the system needs to **adapt** to changing conditions and **update** the state of multiple connected components.
- Some examples of soft real time systems are:
  - **Multimedia applications** such as streaming audio and video, where a small delay or loss of data does not affect the overall user experience .
  - **Network protocols** such as TCP/IP, where packets can be retransmitted or dropped if the network is congested or unreliable.
  - **Air traffic control systems** such as flight planning and scheduling, where the system can adjust the routes and timings of the flights based on the weather, traffic, and other factors.
- The main characteristics of soft real time systems are:
  - They have **non-deterministic** timing behavior, meaning that the execution time of a task can vary depending on the system load, the input data, the hardware, and other factors  .
  - They have **probabilistic** timing requirements, meaning that the system can specify a **desired** or **average** deadline for a task, but not a **guaranteed** or **worst-case** deadline  .
  - They have **degradable** performance, meaning that the system can **trade-off** the quality of the output or the service for the timeliness of the execution, depending on the **priority** or the **importance** of the task   .
  - They can run on **multiprocessor** or **multicore** platforms, meaning that the system can **distribute** the workload among multiple processing units and **exploit** the parallelism and the concurrency of the tasks .
  - They have **fewer** or **looser** restrictions on the applications, meaning that the system can **support** a wider range of functionalities and features, such as dynamic memory allocation, garbage collection, exception handling, and so on .