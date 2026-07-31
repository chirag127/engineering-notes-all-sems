### Basics of RTOS

- RTOS stands for Real-Time Operating System, which is a software system that provides the necessary hard real-time computing capabilities in an embedded environment.
- A real-time system is one that has to respond to events or data within a specified time limit, otherwise it may fail or cause undesirable consequences.
- An RTOS is different from a general-purpose operating system (GPOS) such as Windows or Linux, which are designed for time-sharing and multitasking applications, and do not guarantee deterministic or predictable response times.
- An RTOS consists of the following components:
  - A kernel, which is the core of the RTOS that manages the hardware resources, creates and schedules the software threads, and handles the interrupts and exceptions.
  - A set of services, which are the functions or libraries that provide the application programming interface (API) for the RTOS, such as memory management, inter-process communication, file system, network stack, etc.
  - A set of device drivers, which are the software modules that interface with the specific hardware devices, such as sensors, actuators, communication ports, etc.
- An RTOS can be classified into three types based on the degree of time constraints:
  - Hard real-time, which means that the RTOS must meet the deadlines for all the critical tasks, otherwise the system may fail or cause catastrophic consequences. For example, a missile control system or a pacemaker.
  - Soft real-time, which means that the RTOS can tolerate some delays or missed deadlines for some non-critical tasks, but the system performance may degrade or lose some functionality. For example, a video streaming or a voice recognition system.
  - Firm real-time, which means that the RTOS has to meet the deadlines for most of the tasks, but some tasks can be discarded or ignored if they are too late. For example, a stock trading or a web server system.
- Some examples of RTOS are :
  - FreeRTOS, which is an open source RTOS that supports a wide range of microcontrollers and platforms, and provides a simple and lightweight kernel with minimal memory footprint and low overhead.
  - Azure RTOS, which is a commercial RTOS that offers a comprehensive suite of services and device drivers, and integrates with the Azure cloud platform for IoT applications.
  - VxWorks, which is a proprietary RTOS that is widely used in aerospace, defense, industrial, and automotive sectors, and provides a robust and scalable kernel with advanced security and reliability features.