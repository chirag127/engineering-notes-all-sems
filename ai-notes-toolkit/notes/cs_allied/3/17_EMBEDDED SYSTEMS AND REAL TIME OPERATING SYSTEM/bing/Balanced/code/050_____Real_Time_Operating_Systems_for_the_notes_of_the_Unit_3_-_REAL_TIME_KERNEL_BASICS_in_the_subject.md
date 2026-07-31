# Real Time Operating Systems

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints .
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS is designed for critical systems and for devices like microcontrollers that are timing-specific.
- An RTOS has two key features: predictability and determinism.
  - Predictability means that repeated tasks are performed within a tight time boundary, while in a general-purpose operating system, this is not necessarily so.
  - Determinism means that the system can guarantee a certain response time for a given event or input stimulus.
- An RTOS typically consists of the following components:
  - A kernel that provides the core functionality of the RTOS, such as task scheduling, inter-task communication and synchronization, interrupt handling, and memory management.
  - A set of libraries and APIs that provide additional services and features, such as networking, file system, device drivers, graphical user interface, and security.
  - A development environment that supports the creation, debugging, and testing of real-time applications.
- Some examples of RTOSes are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, and Zephyr.