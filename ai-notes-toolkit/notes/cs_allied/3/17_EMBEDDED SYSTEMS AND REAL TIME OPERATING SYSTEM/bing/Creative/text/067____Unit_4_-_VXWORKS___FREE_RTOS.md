## Unit 4 - VXWORKS / FREE RTOS

- VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems.
- RTOS are designed to provide deterministic and predictable behavior, low latency, and high reliability for applications that require real-time performance.
- VxWorks and FreeRTOS have some similarities and differences in terms of features, cost, support, and target market.

### Similarities

- Both VxWorks and FreeRTOS are based on the preemptive priority-based scheduling algorithm, which allows tasks to be executed according to their assigned priorities and preempted by higher priority tasks when necessary.
- Both VxWorks and FreeRTOS support inter-process communication (IPC) mechanisms such as message queues, semaphores, mutexes, and event flags, which enable tasks to synchronize and exchange data with each other.
- Both VxWorks and FreeRTOS support memory management features such as memory pools, memory partitions, and heap allocation, which allow tasks to dynamically allocate and deallocate memory as needed.
- Both VxWorks and FreeRTOS support interrupt handling features such as interrupt service routines (ISRs), interrupt nesting, and interrupt latency, which allow tasks to respond to external events in a timely manner.

### Differences

- VxWorks is a proprietary RTOS developed by Wind River Systems, while FreeRTOS is an open-source RTOS developed by Richard Barry and maintained by Amazon Web Services.
- VxWorks is a more mature and feature-rich RTOS than FreeRTOS, as it has been in the market since 1987 and supports advanced features such as symmetric multiprocessing (SMP), memory protection, file system, network stack, graphical user interface (GUI), and security.
- VxWorks is a more expensive and complex RTOS than FreeRTOS, as it requires a license fee, a development environment, and a hardware board support package (BSP), while FreeRTOS is free, simple, and portable, and can run on various microcontrollers and development boards.
- VxWorks is a more widely used and supported RTOS than FreeRTOS, as it has a large customer base, a strong partner ecosystem, and a dedicated technical support team, while FreeRTOS has a smaller community, a limited partner network, and a volunteer-based support forum.
- VxWorks is a more suitable RTOS than FreeRTOS for high-end and mission-critical applications that require high performance, reliability, and security, such as aerospace, defense, industrial, and automotive, while FreeRTOS is a more suitable RTOS for low-end and cost-sensitive applications that require simplicity, flexibility, and portability, such as IoT, consumer, and hobbyist.