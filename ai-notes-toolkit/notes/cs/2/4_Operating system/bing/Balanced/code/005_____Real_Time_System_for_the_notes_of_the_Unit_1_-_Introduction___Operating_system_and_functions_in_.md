### Real Time System for the notes of the Unit 1 - Introduction : Operating system and functions in the subject of Operating system

- A real-time system is a system that must process data and events within a specific time limit, otherwise it may cause failure or unacceptable results.
- A real-time operating system (RTOS) is an operating system that supports real-time applications by providing features such as predictability, determinism, fast context switching, inter-thread communication and synchronization, and memory management  .
- There are three types of real-time systems based on the consequences of missing a deadline:
  - Hard real-time system: The system must complete the task within the deadline, otherwise it may cause catastrophic damage or loss of life. For example, air traffic control, missile guidance, pacemaker, etc.
  - Soft real-time system: The system can tolerate some delay in completing the task, but the quality of service may degrade. For example, video streaming, online gaming, voice over IP, etc.
  - Firm real-time system: The system must complete the task within the deadline, otherwise the result is useless and discarded. However, there is no damage or danger involved. For example, stock market analysis, sensor data processing, etc.
- The functions of an RTOS are similar to those of a general-purpose operating system, but with some additional requirements and optimizations  :
  - Process management: The RTOS must be able to create, delete, suspend, resume, and prioritize processes or threads according to their deadlines and importance. It must also provide fast context switching and preemptive scheduling to ensure timely execution of tasks.
  - Memory management: The RTOS must be able to allocate, deallocate, and protect memory for processes or threads. It must also avoid memory fragmentation and support dynamic memory allocation if needed.
  - Device management: The RTOS must be able to handle input/output devices and provide device drivers for them. It must also support interrupt handling and synchronization mechanisms to coordinate with the devices.
  - File management: The RTOS must be able to store, retrieve, and manipulate files and directories on various storage media. It must also provide security and access control for the files.
  - Communication management: The RTOS must be able to support inter-process communication (IPC) and network communication for data exchange and coordination. It must also provide protocols and services for reliable and efficient communication.
  - User interface: The RTOS may or may not provide a graphical user interface (GUI) or a command-line interface (CLI) for the user to interact with the system. It depends on the application and the hardware constraints of the system.
- Some examples of RTOS are :
  - Azure RTOS: A commercial RTOS developed by Microsoft for embedded and IoT applications. It supports various architectures and platforms and provides a suite of middleware components for connectivity, security, and cloud integration.
  - VxWorks: A commercial RTOS developed by Wind River for aerospace, defense, industrial, medical, and automotive applications. It supports various architectures and platforms and provides a rich set of features and services for real-time performance, security, and reliability.
  - FreeRTOS: An open source RTOS developed by Amazon for embedded and IoT applications. It supports various architectures and platforms and provides a simple and lightweight kernel for real-time multitasking.
  - Linux: A general-purpose operating system that can be configured and modified to support real-time applications. It supports various architectures and platforms and provides a large and diverse set of features and services for various domains and purposes.