### Basics of RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system.
- An RTOS creates multiple threads of software execution and a scheduler for managing these threads.
- An RTOS provides the necessary hard real-time computing capabilities, and it does so in an embedded environment.
- An RTOS is used for controlling devices that require timing synchronization with their environment or with other devices.
- An RTOS is a program that acts as an interface between the system hardware and the user.
- An RTOS handles all the interactions between the software and the hardware.
- An RTOS processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS can be classified into three types based on the time limit for completing the tasks:
  - Hard Real-Time operating system: These operating systems guarantee that critical tasks be completed within a range of time. For example, a missile launch system.
  - Soft real-time operating system: This operating system provides some relaxation in the time limit. For example, a video streaming system.
  - Firm Real-time Operating System: RTOS of this type have to meet deadlines but missing a deadline is not a total system failure. For example, a stock market system.
- An RTOS consists of the following basic components:
  - Kernel: The core of the RTOS that provides the basic services, such as thread management, memory management, inter-thread communication, and synchronization.
  - Device drivers: The software modules that interface with the hardware devices, such as sensors, actuators, and communication ports.
  - Middleware: The software layer that provides additional services, such as file system, network stack, graphics, and security.
  - Application: The software that implements the specific functionality of the system, such as user interface, control logic, and data processing.