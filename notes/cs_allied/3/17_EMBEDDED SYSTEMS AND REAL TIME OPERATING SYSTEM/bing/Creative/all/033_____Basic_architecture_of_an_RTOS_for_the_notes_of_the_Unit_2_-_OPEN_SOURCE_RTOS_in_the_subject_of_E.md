# Basic architecture of an RTOS

An RTOS (Real-Time Operating System) is a specialized operating system that provides deterministic and predictable behavior for time-critical applications. An RTOS typically consists of the following components  :

- **The kernel**: The kernel is the core component of the RTOS that manages the basic functions such as task scheduling, interrupt handling, memory management, inter-task communication and synchronization, and timer services. The kernel can be either monolithic or microkernel, depending on the design philosophy and the trade-off between performance and modularity.
- **The tasks**: The tasks are the units of execution that run on the RTOS. Each task has a priority, a stack, a context, and a state. The tasks can be either periodic or aperiodic, depending on their timing requirements. The tasks can communicate with each other and with the kernel using various mechanisms such as message queues, semaphores, mutexes, event flags, pipes, signals, etc .
- **The device drivers**: The device drivers are the modules that interface with the hardware devices and provide a uniform abstraction for the tasks. The device drivers can be either integrated with the kernel or implemented as separate tasks, depending on the RTOS architecture and the device characteristics .
- **The middleware**: The middleware is the layer that provides additional services and functionalities to the tasks, such as networking, file system, graphical user interface, debugging, etc. The middleware can be either part of the RTOS or provided by third-party vendors, depending on the application requirements and the RTOS compatibility .

The following diagram illustrates the general architecture of an RTOS:

![RTOS architecture](https://www.engineersgarage.com/wp-content/uploads/2011/07/RTOS-Architecture.jpg)

: https://www.engineersgarage.com/rtos-real-time-operating-system/
: https://www.windriver.com/solutions/learning/rtos
: https://microcontrollerslab.com/rtos-real-time-operating-system/