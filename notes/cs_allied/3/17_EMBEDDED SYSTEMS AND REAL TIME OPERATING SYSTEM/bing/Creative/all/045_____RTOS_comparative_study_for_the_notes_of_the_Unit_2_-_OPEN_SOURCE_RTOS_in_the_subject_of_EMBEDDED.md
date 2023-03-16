# RTOS comparative study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we will study some of the characteristics and features of different RTOSs and compare them based on various criteria.

## Characteristics of RTOS

Some of the common characteristics of RTOS are:

- **Determinism**: The ability to perform operations or tasks in a fixed amount of time, regardless of the system load or external factors.
- **Responsiveness**: The ability to respond quickly to external events or stimuli, such as interrupts or signals.
- **Reliability**: The ability to function correctly and consistently, even in the presence of faults or errors.
- **Scalability**: The ability to adapt to changing requirements or conditions, such as adding or removing tasks, devices, or resources.
- **Efficiency**: The ability to utilize the available resources, such as memory, CPU, or power, in an optimal way, without wasting or overloading them.

## Features of RTOS

Some of the common features of RTOS are:

- **Task management**: The ability to create, delete, suspend, resume, prioritize, and schedule tasks or threads, which are the basic units of execution in an RTOS.
- **Memory management**: The ability to allocate, deallocate, and protect memory regions for tasks, data, or code, as well as to support different types of memory, such as static, dynamic, or shared.
- **Inter-task communication**: The ability to exchange data or signals between tasks, using various mechanisms, such as message queues, semaphores, mutexes, events, or pipes.
- **Interrupt handling**: The ability to handle external or internal interrupts, which are requests for immediate attention from the hardware or software, and to dispatch them to the appropriate tasks or handlers.
- **Device management**: The ability to control and access various devices, such as sensors, actuators, or peripherals, using different protocols, such as serial, parallel, or USB.
- **File system**: The ability to store and retrieve data from persistent storage, such as disks, flash, or EEPROM, using different formats, such as FAT, NTFS, or EXT.
- **Network support**: The ability to communicate with other systems or devices over a network, using different protocols, such as TCP/IP, UDP, or MQTT.
- **Time management**: The ability to measure and manipulate time, using different units, such as ticks, milliseconds, or seconds, and to provide various services, such as timers, clocks, or alarms.

## Comparison of RTOS

There are many RTOSs available in the market, each with its own advantages and disadvantages. Some of the popular RTOSs are:

- **FreeRTOS**: An open source RTOS that is designed to be small, simple, and portable. It supports various architectures, such as ARM, AVR, PIC, and x86, and provides basic features, such as task management, memory management, inter-task communication, and interrupt handling. It does not provide advanced features, such as file system, network support, or graphical user interface. It is suitable for embedded systems that have limited resources and require low complexity.
- **Zephyr**: An open source RTOS that is designed to be scalable, modular, and secure. It supports various architectures, such as ARM, x86, RISC-V, and ARC, and provides basic and advanced features, such as task management, memory management, inter-task communication, interrupt handling, device management, file system, network support, and time management. It also supports Bluetooth communication, which doubles its footprint. It is suitable for embedded systems that have diverse requirements and require high performance.
- **LynxOS**: A proprietary RTOS that is designed to be reliable, deterministic, and POSIX-compliant. It supports various architectures, such as ARM, x86, PowerPC, and MIPS, and provides basic and advanced features, such as task management, memory management, inter-task communication, interrupt handling, device management, file system, network support, and time management. It also provides a graphical user interface, a bash shell, and a printf function. It is suitable for embedded systems that have critical applications and require high reliability.

The following table summarizes some of the criteria and features of the three RTOSs:

| Criteria | FreeRTOS | Zephyr | LynxOS |
| --- | --- | --- | --- |
| License | Open source | Open source | Proprietary |
| Architecture |