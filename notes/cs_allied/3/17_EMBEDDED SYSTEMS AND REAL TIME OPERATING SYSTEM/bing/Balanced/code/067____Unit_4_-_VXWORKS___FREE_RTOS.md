## Unit 4 - VXWORKS / FREE RTOS

- VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems.
- RTOS are designed to provide deterministic and predictable behavior, low latency, and high reliability for applications that require real-time performance.
- VxWorks and FreeRTOS have some similarities and differences in terms of features, cost, support, and target market.

### Similarities

- Both VxWorks and FreeRTOS are based on the preemptive priority-based scheduling algorithm, which allows tasks to be executed according to their assigned priority and preempted by higher priority tasks when necessary.
- Both VxWorks and FreeRTOS support inter-process communication mechanisms such as message queues, semaphores, mutexes, and event flags, which enable tasks to synchronize and exchange data with each other.
- Both VxWorks and FreeRTOS provide memory management functions such as memory allocation, deallocation, and protection, which allow tasks to use dynamic memory safely and efficiently.
- Both VxWorks and FreeRTOS have low interrupt latency, which means the time between the occurrence of an interrupt and the execution of the corresponding interrupt service routine is minimal.

### Differences

- VxWorks is a proprietary RTOS developed by Wind River Systems, while FreeRTOS is an open-source RTOS created by Richard Barry and maintained by Amazon Web Services.
- VxWorks is a more mature and feature-rich RTOS than FreeRTOS, as it has been in the market since 1987 and supports advanced capabilities such as multicore processing, networking, security, graphics, and file systems.
- VxWorks is a more expensive and complex RTOS than FreeRTOS, as it requires a license fee, a development environment, and a dedicated hardware platform, while FreeRTOS is free, simple, and portable to various architectures and compilers.
- VxWorks is a more widely used and supported RTOS than FreeRTOS, as it has a large customer base, a professional technical support team, and a comprehensive documentation and training resources, while FreeRTOS has a smaller community, a limited support options, and a less extensive documentation and training resources.
- VxWorks is a more suitable RTOS for high-end and mission-critical applications that require high performance, reliability, and security, such as aerospace, defense, automotive, and industrial control, while FreeRTOS is a more suitable RTOS for low-end and cost-sensitive applications that require simplicity, flexibility, and portability, such as IoT, education, and hobby projects.