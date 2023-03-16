## Unit 1 - EMBEDDED OS INTERNALS

- An embedded operating system (OS) is a specialized software that runs on a dedicated hardware device and provides a platform for running applications.
- Embedded OSes are designed to meet the specific requirements of the device, such as performance, reliability, security, power efficiency, and memory footprint.
- Embedded OSes can be classified into two categories: real-time and non-real-time.
  - A real-time OS (RTOS) is an embedded OS that guarantees to respond to events or tasks within a predefined time limit, regardless of the system load. RTOSes are suitable for time-critical applications, such as industrial control, robotics, and avionics.
  - A non-real-time OS (NRTOS) is an embedded OS that does not provide any timing guarantees, but offers more functionality and flexibility than an RTOS. NRTOSes are suitable for general-purpose applications, such as multimedia, networking, and user interfaces.
- Embedded OSes can be further classified into two types: monolithic and modular.
  - A monolithic OS is an embedded OS that consists of a single executable image that contains the kernel and all the drivers, libraries, and applications. Monolithic OSes are simple, fast, and compact, but difficult to maintain, debug, and update.
  - A modular OS is an embedded OS that consists of multiple components that can be loaded and unloaded dynamically. Modular OSes are more flexible, scalable, and secure, but require more memory and processing overhead.
- Embedded OSes have some common components, such as:
  - The kernel, which is the core of the OS that manages the hardware resources, such as CPU, memory, and I/O devices, and provides basic services, such as task scheduling, interrupt handling, and memory management.
  - The drivers, which are software modules that communicate with the hardware devices and abstract their functionality for the applications.
  - The libraries, which are collections of reusable functions that provide common functionality, such as math, string, and network operations.
  - The applications, which are software programs that perform specific tasks for the user or the device, such as user interface, data processing, and communication.
- Embedded OSes have some unique challenges, such as:
  - Limited hardware resources, such as CPU, memory, and power, which require the OS to be optimized for performance and efficiency.
  - Diverse hardware platforms, such as microcontrollers, microprocessors, and system-on-chips, which require the OS to be portable and adaptable.
  - High reliability and security requirements, which require the OS to be robust and resilient against errors and attacks.
  - Long life cycle and maintenance, which require the OS to be stable and compatible with future updates and changes.