### Overview of Open source RTOS for Embedded systems (Free RTOS/ ChibiosRT) and application development

- An open source RTOS is a real-time operating system that is freely available for developers to use, modify, and distribute under a license that allows such actions.
- An RTOS is designed to support time-critical applications by providing deterministic execution of tasks, preemptive scheduling, interrupt handling, inter-task communication, and memory management.
- An embedded system is a computer system that is integrated with a specific hardware device and performs a dedicated function or functions. Embedded systems often have limited resources, such as memory, processing power, and battery life.
- Some examples of open source RTOS for embedded systems are:
  - FreeRTOS: A market-leading RTOS that is widely used in various industries and applications. It is highly portable, configurable, and scalable. It supports multiple architectures, such as ARM, AVR, PIC, and x86. It also provides a tick-less mode to support low power applications .
  - ChibiOS/RT: A compact and fast RTOS that supports multiple architectures, such as ARM, AVR, MSP430, and x86. It provides a rich set of features, such as dynamic threads, semaphores, mutexes, queues, timers, and event flags. It also supports various communication protocols, such as I2C, SPI, UART, and USB.
- Application development for embedded systems using open source RTOS involves the following steps:
  - Selecting an appropriate RTOS and hardware platform for the application requirements and constraints.
  - Configuring the RTOS kernel and libraries according to the application needs and preferences. This may involve using a graphical tool, such as eCos configuration tool for eCos RTOS, or editing a configuration file, such as FreeRTOSConfig.h for FreeRTOS.
  - Writing the application code using the RTOS API and the hardware-specific drivers. The application code typically consists of one or more tasks that perform the desired functions and interact with each other and the hardware using the RTOS services.
  - Compiling, linking, and debugging the application code using an integrated development environment (IDE), such as Eclipse, or a command-line toolchain, such as GCC. The application code may also be tested and verified using a simulator, such as QEMU, or a hardware debugger, such as JTAG.
  - Deploying the application code to the target device and running it. The application code may also be updated or modified using a bootloader, such as U-Boot, or an over-the-air (OTA) mechanism, such as MQTT.