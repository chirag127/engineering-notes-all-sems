## Unit 4 - VxWorks / FreeRTOS

- VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems.
- An RTOS is a software that manages the hardware resources and tasks of an embedded system, providing deterministic and predictable behavior.
- VxWorks and FreeRTOS have some similarities and differences in terms of features, performance, licensing, and support.

### Features

- VxWorks is a full-featured RTOS that supports multi-core, symmetric multiprocessing (SMP), and asymmetric multiprocessing (AMP) architectures, as well as various communication protocols, file systems, security mechanisms, and graphical user interfaces (GUIs).
- FreeRTOS is a minimalistic RTOS that provides only the core functionality of task scheduling, inter-task communication, and memory management. It can be extended with additional libraries and components, such as FreeRTOS+TCP, FreeRTOS+FAT, and FreeRTOS+POSIX.
- VxWorks supports both preemptive and cooperative multitasking, while FreeRTOS only supports preemptive multitasking.
- VxWorks supports both priority-based and time-slice scheduling, while FreeRTOS only supports priority-based scheduling.
- VxWorks supports various inter-task communication mechanisms, such as message queues, pipes, signals, semaphores, mutexes, and events, while FreeRTOS only supports message queues, semaphores, and events.
- VxWorks supports various memory management techniques, such as memory pools, memory partitions, and memory protection, while FreeRTOS only supports heap allocation and stack overflow detection.

### Performance

- VxWorks and FreeRTOS both claim to offer high performance, low latency, and low footprint for embedded systems.
- VxWorks claims to have the lowest interrupt latency in the industry, as well as the highest network throughput and the fastest boot time.
- FreeRTOS claims to have a very small code size, ranging from 6KB to 12KB, depending on the configuration and compiler optimization.
- The actual performance of VxWorks and FreeRTOS may vary depending on the hardware platform, the application requirements, and the system configuration.

### Licensing and Support

- VxWorks is a proprietary RTOS that requires a commercial license and a royalty fee for each deployed device. It is developed and maintained by Wind River Systems, a subsidiary of Intel Corporation.
- FreeRTOS is an open-source RTOS that is licensed under the MIT license, which allows free use, modification, and distribution of the software. It is developed and maintained by Amazon Web Services (AWS), which acquired the original developer, Real Time Engineers Ltd, in 2017.
- VxWorks offers professional support and training services, as well as a large online community and documentation resources.
- FreeRTOS offers limited support and training services, as well as a moderate online community and documentation resources.