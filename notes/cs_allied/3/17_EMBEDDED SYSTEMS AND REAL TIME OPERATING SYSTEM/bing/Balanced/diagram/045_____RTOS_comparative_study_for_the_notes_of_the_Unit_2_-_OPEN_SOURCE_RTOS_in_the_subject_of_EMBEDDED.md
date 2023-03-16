### RTOS comparative study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we will study some of the characteristics and features of different RTOSs and compare them based on various criteria.

#### Characteristics of RTOS

Some of the common characteristics of RTOS are:

- Determinism: The ability to perform operations or tasks in a fixed amount of time, regardless of the system load or external factors.
- Responsiveness: The ability to respond quickly to external events or stimuli, such as interrupts or signals.
- Reliability: The ability to function correctly and consistently, even in the presence of faults or errors.
- Scalability: The ability to adapt to different hardware platforms, system configurations, and application requirements.
- Modularity: The ability to separate the system into independent components or modules, which can be reused, replaced, or updated easily.
- Portability: The ability to run on different hardware architectures, processors, or devices, with minimal or no changes to the source code.

#### Features of RTOS

Some of the common features of RTOS are:

- Multitasking: The ability to execute multiple tasks or processes concurrently, by sharing the CPU time among them.
- Preemptive scheduling: The ability to interrupt a running task or process and switch to a higher priority one, based on predefined rules or algorithms.
- Inter-task communication: The ability to exchange data or messages between different tasks or processes, using various mechanisms such as queues, pipes, semaphores, mutexes, or events.
- Memory management: The ability to allocate, deallocate, and manage the memory resources for different tasks or processes, using techniques such as static, dynamic, or hybrid allocation, memory pools, or memory protection.
- Device drivers: The ability to interface with different hardware devices, such as sensors, actuators, or peripherals, using standardized or customized protocols or interfaces.
- File system: The ability to store, retrieve, and manipulate data on different storage media, such as flash, EEPROM, or SD card, using hierarchical or flat structures, or different file formats.
- Network stack: The ability to communicate with other systems or devices over different network protocols, such as TCP/IP, UDP, MQTT, or CoAP, using wired or wireless connections, such as Ethernet, Wi-Fi, or Bluetooth.

#### Comparison of RTOS

There are many RTOSs available in the market, each with its own advantages and disadvantages, depending on the application domain, system requirements, and user preferences. Some of the popular RTOSs are:

- FreeRTOS: An open source RTOS that is designed to be small, simple, and portable. It supports preemptive and cooperative multitasking, inter-task communication, memory management, and device drivers. It can run on various microcontrollers, such as ARM, AVR, PIC, or MSP430. It is widely used in embedded systems, IoT devices, and educational projects.
- Zephyr: An open source RTOS that is designed to be scalable, modular, and secure. It supports preemptive and cooperative multitasking, inter-task communication, memory management, device drivers, file system, and network stack. It can run on various microcontrollers, such as ARM, x86, RISC-V, or ARC. It is mainly used in IoT devices, wearable devices, and smart home applications.
- LynxOS: A proprietary RTOS that is designed to be deterministic, reliable, and compliant. It supports preemptive multitasking, inter-task communication, memory management, device drivers, file system, and network stack. It can run on various processors, such as x86, PowerPC, or ARM. It is mainly used in aerospace, defense, industrial, and medical applications.
- QNX: A proprietary RTOS that is designed to be robust, secure, and real-time. It supports preemptive multitasking, inter-task communication, memory management, device drivers, file system, and network stack. It can run on various processors, such as x86, ARM, MIPS, or SH. It is mainly used in automotive, telecommunications, and industrial applications.

The following table summarizes some of the key differences among these RTOSs based on various criteria:

| Criteria | FreeRTOS | Zephyr | LynxOS | QNX |
| --- | --- | --- | --- | --- |
| License | MIT | Apache 2.0 | Proprietary | Proprietary |
| Size | 8 KB - 16 KB |