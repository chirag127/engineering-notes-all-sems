### Real Time Operating Systems

- A real time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints  .
- An RTOS guarantees real time applications a certain capability within a specified deadline.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS is designed for critical systems and for devices like microcontrollers that are timing-specific.
- An RTOS has two key features: predictability and determinism.
  - Predictability means that repeated tasks are performed within a tight time boundary.
  - Determinism means that the system responds to events in a consistent and predictable manner.
- An RTOS typically consists of the following components:
  - A kernel that provides the core functionality of the RTOS, such as task management, inter-task communication and synchronization, memory management, interrupt handling, and timer services .
  - A set of device drivers that interface with the hardware devices and peripherals.
  - A set of middleware libraries that provide additional functionality, such as networking, file system, graphics, security, and connectivity .
  - A set of application programming interfaces (APIs) that allow the application developers to use the services of the RTOS .
- Some examples of RTOSs are Azure RTOS ThreadX, FreeRTOS, QNX, VxWorks, and Zephyr .