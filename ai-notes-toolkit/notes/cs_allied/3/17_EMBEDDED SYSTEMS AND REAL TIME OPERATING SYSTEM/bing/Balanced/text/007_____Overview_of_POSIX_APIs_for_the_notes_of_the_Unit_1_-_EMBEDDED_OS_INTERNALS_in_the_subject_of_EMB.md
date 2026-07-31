### Overview of POSIX APIs

- POSIX stands for **Portable Operating System Interface** and it is a family of standards specified by **IEEE** for maintaining compatibility among operating systems.
- POSIX defines both the **system** and **user-level** application programming interfaces (APIs), along with **command line shells** and **utility interfaces**, for software compatibility (portability) with variants of **Unix** and other operating systems.
- POSIX is also a **trademark** of the IEEE and it is intended to be used by both **application** and **system developers**.
- POSIX APIs are an increasingly popular **OSAL** (operating system abstraction layer) for **IoT** and **embedded applications**, as can be seen in **Zephyr**, **AWS:FreeRTOS**, **TI-RTOS**, and **NuttX**.
- POSIX APIs offer a **familiar** and **standardized** interface to non-embedded programmers, especially from **Linux**.
- POSIX APIs are divided into several **components**, each with a different **scope** and **functionality**. Some of the components are:
  - **POSIX.1**: Core Services, which covers **processes**, **signals**, **timers**, **pipes**, **I/O**, **file systems**, etc.
  - **POSIX.1b**: Real-time Extensions, which covers **scheduling**, **clocks**, **semaphores**, **message queues**, **shared memory**, etc.
  - **POSIX.1c**: Threads Extensions, which covers **threads**, **mutexes**, **condition variables**, **cancellation**, etc.
  - **POSIX.2**: Shell and Utilities, which covers **shell commands**, **shell scripting**, **utilities**, etc.
  - **POSIX.4**: Application Environment Profile, which covers **asynchronous I/O**, **memory mapping**, **synchronization**, etc.
  - **POSIX.5**: Ada Language Interfaces, which covers **Ada bindings** for POSIX APIs.
  - **POSIX.6**: Security Extensions, which covers **access control**, **auditing**, **user authentication**, etc.
  - **POSIX.7**: System Administration, which covers **system management**, **logging**, **backup**, **restore**, etc.
  - **POSIX.8**: Network Services, which covers **sockets**, **protocols**, **services**, **name resolution**, etc.
  - **POSIX.9**: Hardware Abstraction, which covers **device drivers**, **device control**, **device configuration**, etc.
  - **POSIX.10**: System Interfaces and Headers, which covers **header files**, **data types**, **constants**, **macros**, **function prototypes**, etc. for POSIX APIs.