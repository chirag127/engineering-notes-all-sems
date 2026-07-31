### Overview of Open source RTOS for Embedded systems (Free RTOS/ ChibiosRT) and application development

- An open source RTOS is a real-time operating system that is freely available for developers to use, modify, and distribute under a license that allows such actions.
- An RTOS is designed to support time-critical applications by providing deterministic execution of tasks, preemptive scheduling, inter-task communication, and synchronization mechanisms.
- An embedded system is a computer system that is integrated with a specific hardware device and performs a dedicated function or functions. Embedded systems often have limited resources, such as memory, processing power, and battery life, and require high reliability and efficiency.
- Some examples of open source RTOS for embedded systems are:
  - FreeRTOS: A market-leading RTOS that is widely used in various industries and applications, such as aerospace, medical, automotive, IoT, and robotics. It is highly configurable, portable, and scalable, and supports a variety of architectures and compilers. It also provides a rich set of features, such as tick-less mode, event groups, queues, semaphores, mutexes, timers, software timers, task notifications, and stream buffers .
  - ChibiOS/RT: A compact and fast RTOS that is optimized for high-performance embedded applications. It supports multiple architectures, such as ARM, AVR, MSP430, and x86, and provides a modular structure, a HAL layer, a portable kernel, and a comprehensive set of libraries. It also offers features such as round-robin scheduling, priority inheritance, dynamic memory allocation, message passing, mailboxes, binary semaphores, and event flags.
- Application development for embedded systems using open source RTOS involves the following steps:
  - Selecting an appropriate RTOS and hardware platform for the specific requirements and constraints of the application.
  - Configuring the RTOS kernel and libraries according to the desired functionality and performance.
  - Writing the application code using the RTOS API and the supported programming language, such as C or C++.
  - Compiling and linking the application code with the RTOS kernel and libraries using a cross-compiler and a linker.
  - Loading and running the application on the target device using a debugger or a flash programmer.
  - Testing and debugging the application using the RTOS tools and features, such as trace, assert, and statistics.