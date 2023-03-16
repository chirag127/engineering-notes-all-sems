### Real Time Operating Systems

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints .
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS is designed for critical systems and for devices like microcontrollers that are timing-specific.
- An RTOS has two key features: predictability and determinism.
  - Predictability means that repeated tasks are performed within a tight time boundary, while in a general-purpose operating system, this is not necessarily so.
  - Determinism means that the system responds to an input stimulus within a known and bounded time, regardless of the system load or the number of tasks.
- An RTOS typically consists of the following components:
  - A kernel, which is the core of the RTOS that provides the basic services, such as task management, inter-task communication and synchronization, memory management, interrupt handling, and timer services.
  - A set of device drivers, which are software modules that interface with the hardware devices, such as sensors, actuators, communication ports, and storage devices.
  - A set of middleware, which are software modules that provide higher-level functionality, such as networking, file systems, graphics, security, and web services.
  - A set of application programming interfaces (APIs), which are the interfaces that allow the application developers to use the services of the RTOS and the middleware.
- Some examples of RTOSes are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, and Zephyr.