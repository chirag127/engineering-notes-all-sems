# Overview of Open source RTOS for Embedded systems (Free RTOS/ ChibiosRT) and application development

- An **open source RTOS** is a real-time operating system that is freely available for anyone to use, modify, and distribute under a permissive license.
- An **embedded system** is a computer system that is designed to perform a specific function within a larger system, often with limited resources and strict timing constraints.
- An **application development** is the process of creating software programs that run on an embedded system, using various tools and languages.
- Some of the most popular open source RTOS for embedded systems are **FreeRTOS** and **ChibiOS/RT**.

## FreeRTOS

- FreeRTOS is a market-leading RTOS for microcontrollers and small microprocessors.
- It is designed to be simple and easy to use, with only 3 source files that are common to all RTOS ports, and one microcontroller specific source file.
- It supports over 40 architectures and 18 toolchains, and has a large community of users and contributors.
- It provides basic features such as task management, inter-task communication, synchronization, timers, memory management, and hooks for application-specific functionality.
- It also supports advanced features such as tick-less mode, event groups, software timers, queue sets, trace and visualization tools, and kernel-aware debugging.
- It is distributed under the MIT license, which allows commercial use without any restrictions.

## ChibiOS/RT

- ChibiOS/RT is a compact and fast RTOS for embedded systems, with a rich set of features and a high level of portability.
- It is designed to be modular and configurable, with a kernel that can be tailored to the specific needs of the application.
- It supports over 30 architectures and 10 toolchains, and has a growing community of users and developers.
- It provides basic features such as task management, inter-task communication, synchronization, timers, memory management, and hooks for application-specific functionality.
- It also supports advanced features such as tick-less mode, event flags, software timers, binary semaphores, mutexes, condition variables, memory pools, heap allocators, dynamic threads, and kernel statistics.
- It is distributed under the GPL license, with an optional commercial license for closed-source projects.

## Application development

- Application development for embedded systems using open source RTOS requires a set of tools and skills that are different from general-purpose software development.
- Some of the common tools and steps involved are:

  - **Choosing an RTOS** that suits the requirements and constraints of the embedded system, such as performance, memory, power, functionality, license, and support.
  - **Choosing a hardware platform** that is compatible with the chosen RTOS, such as a microcontroller, a development board, or a custom board.
  - **Choosing a toolchain** that can compile, link, and debug the application code for the target hardware, such as GCC, IAR, Keil, or Eclipse.
  - **Downloading and installing the RTOS** source code and documentation, and configuring the RTOS options and parameters according to the application needs.
  - **Writing the application code** using the RTOS API and libraries, and following the RTOS coding style and conventions.
  - **Building and flashing the application** to the target hardware, using tools such as make, CMake, or IDEs.
  - **Testing and debugging the application** using tools such as serial console, logic analyzer, oscilloscope, or RTOS-specific tools.