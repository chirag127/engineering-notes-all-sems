# RTOS Comparative Study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we will study some of the features and characteristics of different RTOSs and compare them based on various criteria.

## Features of RTOS

Some of the common features of RTOS are:

- Preemptive multitasking: The ability of the operating system to interrupt a running task and switch to another task.
- Priority-based scheduling: The ability of the operating system to assign different priorities to different tasks and execute them accordingly.
- Inter-task communication and synchronization: The ability of the operating system to provide mechanisms for tasks to communicate and coordinate with each other, such as message queues, semaphores, mutexes, etc.
- Memory management: The ability of the operating system to allocate and deallocate memory for tasks and data structures.
- Interrupt handling: The ability of the operating system to respond to external events and signals, such as timers, sensors, etc.
- Device drivers: The ability of the operating system to interface with hardware devices, such as serial ports, network interfaces, etc.

## Criteria for Comparison

Some of the criteria that can be used to compare different RTOSs are:

- Size: The amount of memory (RAM and ROM) required by the operating system and its components.
- Performance: The speed and efficiency of the operating system in executing tasks and handling interrupts.
- Scalability: The ability of the operating system to support a large number of tasks and devices.
- Portability: The ability of the operating system to run on different hardware platforms and architectures.
- Reliability: The ability of the operating system to handle errors and faults and ensure correct operation.
- Security: The ability of the operating system to protect the system and data from unauthorized access and manipulation.
- Licensing: The terms and conditions under which the operating system can be used and modified.

## Examples of RTOS

Some of the examples of RTOSs are:

- FreeRTOS: An open source RTOS that supports a wide range of microcontrollers and architectures. It is designed to be small, simple, and easy to use. It provides basic features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization, memory management, and interrupt handling. It does not provide device drivers or networking support, but relies on external libraries and modules. It has a permissive MIT license that allows free use and modification of the source code.
- Zephyr: An open source RTOS that targets small and resource-constrained devices, such as IoT and wearable devices. It is designed to be modular, scalable, and secure. It provides features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization, memory management, interrupt handling, device drivers, networking support, and security mechanisms. It has a permissive Apache 2.0 license that allows free use and modification of the source code.
- LynxOS: A proprietary RTOS that targets high-performance and safety-critical applications, such as aerospace, defense, and industrial systems. It is designed to be fast, reliable, and secure. It provides features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization, memory management, interrupt handling, device drivers, networking support, security mechanisms, and POSIX compliance. It has a proprietary license that requires a fee for use and modification of the source code.

## Comparison Table

The following table summarizes some of the features and characteristics of the three RTOSs mentioned above:

| Feature | FreeRTOS | Zephyr | LynxOS |
| --- | --- | --- | --- |
| Size | 8 KB - 1.5 MB | 16 KB - 1.5 MB | 1.4 MB - 2.5 MB |
| Performance | Moderate | High | High |
| Scalability | Moderate | High | High |
| Portability | High | High | Moderate |
| Reliability | Moderate | High | High |
| Security | Low | High | High |
| Licensing | MIT | Apache 2.0 | Proprietary |

: https://en.wikipedia.org/wiki/FreeRTOS
: https://en.wikipedia.org/wiki/Zephyr_(operating_system)
: https://www.lynx.com/embedded-systems-learning-center/how-to-choose-a-real-time-operating-system-rtos