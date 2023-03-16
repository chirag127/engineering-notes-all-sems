## Unit 1 - EMBEDDED OS INTERNALS

- An embedded operating system (OS) is a specialized software that runs on a dedicated hardware platform and provides a set of services and interfaces for the applications running on it.
- Embedded OSes are designed to meet the specific requirements of the embedded systems, such as real-time performance, low memory footprint, power efficiency, reliability, security, etc.
- Embedded OSes can be classified into two categories: general-purpose embedded OSes and real-time embedded OSes.
- General-purpose embedded OSes are based on standard OSes, such as Linux, Windows, or Android, and are modified or customized to suit the needs of the embedded systems. They offer a rich set of features and functionalities, but may not guarantee deterministic behavior or strict timing constraints.
- Real-time embedded OSes are designed to provide predictable and timely responses to the events or stimuli in the system. They have a minimal kernel that handles the scheduling, synchronization, and communication of the tasks, and a set of services and libraries that support the application development. They can be further divided into hard real-time OSes and soft real-time OSes, depending on the degree of criticality of the timing requirements.
- Some examples of general-purpose embedded OSes are Embedded Linux, Windows Embedded, and Android Things. Some examples of real-time embedded OSes are FreeRTOS, VxWorks, and QNX.
- The main components of an embedded OS are:
  - Kernel: The core of the OS that manages the resources, such as CPU, memory, and I/O devices, and provides the basic services, such as task management, inter-task communication, interrupt handling, and timer services.
  - Device drivers: The software modules that interface with the hardware devices and abstract their functionalities for the applications.
  - File system: The software module that organizes the data storage and retrieval on the persistent memory devices, such as flash, EEPROM, or SD card.
  - Network stack: The software module that implements the protocols and standards for the data communication over the network interfaces, such as Ethernet, Wi-Fi, Bluetooth, or CAN.
  - Middleware: The software layer that provides the common functionalities and services for the applications, such as graphical user interface (GUI), database, web server, security, etc.
  - Application programming interface (API): The set of functions, data structures, and constants that define the interface between the applications and the OS.
  - Applications: The software programs that implement the specific functions and logic of the embedded system.