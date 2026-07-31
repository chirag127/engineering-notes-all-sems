### Real Time Operating Systems

- A real time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints .
- An RTOS guarantees real time applications a certain capability within a specified deadline.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS has two key features: predictability and determinism.
  - Predictability means that repeated tasks are performed within a tight time boundary, regardless of the system load or other factors.
  - Determinism means that the system responds to an input stimulus within a known and bounded time, regardless of the complexity or frequency of the stimulus.
- An RTOS is designed for critical systems and for devices like microcontrollers that are timing-specific.
- An RTOS typically consists of the following components:
  - A kernel that manages the core functions of the system, such as task scheduling, interrupt handling, inter-task communication and synchronization, and memory management.
  - A set of libraries and APIs that provide various services and utilities for the application development.
  - A set of device drivers that interface with the hardware and peripherals.
  - A set of middleware components that enable higher-level functionality, such as networking, file systems, graphics, security, etc.
- Some examples of RTOSes are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, RTEMS, etc.