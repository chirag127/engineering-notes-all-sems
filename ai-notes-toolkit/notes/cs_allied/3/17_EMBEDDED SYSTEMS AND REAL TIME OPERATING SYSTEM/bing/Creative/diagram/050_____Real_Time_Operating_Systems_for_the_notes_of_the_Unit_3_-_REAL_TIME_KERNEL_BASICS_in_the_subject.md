Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of real time operating systems for the unit 3 - real time kernel basics in the subject of embedded systems and real time operating systems.

### Real Time Operating Systems

- A real time operating system (RTOS) is an operating system (OS) that processes data and events that have critically defined time constraints  .
- An RTOS is different from a general-purpose OS, such as Windows or Linux, which may not guarantee the timely execution of tasks or the predictability of response times  .
- An RTOS is designed for critical systems and devices that are timing-specific, such as embedded systems, industrial controllers, robotics, avionics, medical devices, etc  .
- An RTOS typically has two key features: predictability and determinism.
  - Predictability means that the RTOS can guarantee that a task will be completed within a specified deadline, regardless of the system load or other factors.
  - Determinism means that the RTOS can guarantee that the same input will always produce the same output and behavior, regardless of the timing or order of events.
- An RTOS usually consists of a kernel and a set of services or libraries that provide various functionalities, such as real-time multithreading, inter-thread communication and synchronization, memory management, interrupt handling, device drivers, file systems, network protocols, etc  .
- An RTOS can be classified into two types: hard real-time and soft real-time  .
  - A hard real-time system is one that must meet all the deadlines, otherwise the system may fail or cause severe consequences  .
  - A soft real-time system is one that can tolerate some missed deadlines, but the quality of service may degrade or the system may experience performance issues  .
- Some examples of RTOSes are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, RTLinux, etc .