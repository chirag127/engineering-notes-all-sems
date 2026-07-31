# Real Time System

A real time system is a system that can process data and events within a specified and predictable time frame. A real time system must meet the deadlines imposed by the environment, otherwise it may cause a system failure or undesirable consequences. A real time system is often used for applications that require high reliability, safety, and performance, such as flight control systems, industrial automation, robotics, and medical devices.

Some characteristics of a real time system are:

- Timeliness: The system must produce the correct output within the required time limit.
- Time synchronization: The system must coordinate the activities of different components that operate with independent clocks.
- Concurrency: The system must handle multiple tasks or events that occur simultaneously or overlap in time.
- Determinism: The system must behave in a predictable and consistent manner under all circumstances.
- Fault tolerance: The system must be able to recover from errors or failures without compromising the functionality or safety of the system.

There are two types of real time systems based on the severity of the deadlines:

- Hard real time system: A system that must meet the deadlines without any exception. A missed deadline can result in a catastrophic failure or loss of life. For example, a missile guidance system, a pacemaker, or an airbag system.
- Soft real time system: A system that can tolerate some degree of deadline violation. A missed deadline can result in a degraded performance or quality of service, but not a fatal outcome. For example, a video streaming system, a voice recognition system, or a web server.

A real time system requires a special type of operating system, called a real time operating system (RTOS), that can support the features and requirements of the system. An RTOS is different from a general purpose operating system, such as Windows or Linux, that is designed for time-sharing or multitasking applications. An RTOS provides the following functions:

- Task scheduling: The RTOS assigns priorities to the tasks and allocates the CPU time according to the deadlines and importance of the tasks.
- Interrupt handling: The RTOS responds to the external or internal events that trigger the execution of the tasks or interrupt the current task.
- Memory management: The RTOS allocates and deallocates the memory space for the tasks and data structures.
- Inter-task communication: The RTOS provides mechanisms for the tasks to exchange information or synchronize their activities, such as message queues, semaphores, or mutexes.
- Device drivers: The RTOS interfaces with the hardware devices and peripherals that are used by the system, such as sensors, actuators, or network cards.

Some examples of RTOS are:

- FreeRTOS: An open source RTOS that supports various microcontrollers and platforms.
- VxWorks: A commercial RTOS that is widely used for aerospace, defense, and industrial applications.
- QNX: A commercial RTOS that is based on a microkernel architecture and is used for automotive, medical, and telecommunications applications.
- RTLinux: An extension of the Linux kernel that provides hard real time capabilities.