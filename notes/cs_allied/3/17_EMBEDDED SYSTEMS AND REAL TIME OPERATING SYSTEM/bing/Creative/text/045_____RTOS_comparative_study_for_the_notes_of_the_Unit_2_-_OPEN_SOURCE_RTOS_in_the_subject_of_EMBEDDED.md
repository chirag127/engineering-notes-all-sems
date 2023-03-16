### RTOS comparative study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we provide a brief description and comparison of some of the most popular and widely used RTOSs.

- **Zephyr**: Zephyr is a small, scalable, and open source RTOS that is designed for resource-constrained devices, such as IoT devices. Zephyr supports multiple architectures, such as ARM, x86, RISC-V, and others. Zephyr offers features such as threading, interrupts, memory allocation, Bluetooth communication, networking, filesystems, and more. Zephyr has a minimum configuration of 8 KB, which can increase depending on the features enabled. Zephyr is suitable for applications that require low power consumption, high security, and fast response times.

- **LynxOS**: LynxOS is a POSIX-compliant, deterministic, and hard real-time operating system that is designed for safety- and security-critical applications, such as avionics, industrial control, and medical devices. LynxOS supports multiple architectures, such as x86, PowerPC, ARM, and others. LynxOS offers features such as thread and process support, floating point, filesystems, USB, networking, optional bash shell, and more. LynxOS has a default configuration of 1.4 MB, which can be customized depending on the requirements. LynxOS is suitable for applications that require high reliability, robustness, and compliance with standards.

- **FreeRTOS**: FreeRTOS is a free, open source, and market-leading RTOS that is designed for microcontrollers and small embedded systems. FreeRTOS supports multiple architectures, such as ARM, x86, RISC-V, and others. FreeRTOS offers features such as preemptive or cooperative multitasking, inter-task communication, memory management, timers, and more. FreeRTOS has a very small footprint, typically less than 10 KB, which can vary depending on the configuration. FreeRTOS is suitable for applications that require portability, simplicity, and flexibility.

- **VxWorks**: VxWorks is a proprietary, high-performance, and scalable RTOS that is designed for embedded and real-time applications, such as aerospace, defense, automotive, industrial, and medical devices. VxWorks supports multiple architectures, such as x86, PowerPC, ARM, and others. VxWorks offers features such as multicore and SMP support, networking, security, graphics, filesystems, USB, and more. VxWorks has a modular and configurable architecture, which allows for optimizing the footprint and performance. VxWorks is suitable for applications that require high performance, security, and reliability.

The following table summarizes some of the key differences among the RTOSs mentioned above:

| Feature | Zephyr | LynxOS | FreeRTOS | VxWorks |
|---------|--------|--------|----------|---------|
| License | Open source | Proprietary | Open source | Proprietary |
| Footprint | 8 KB - 16 KB | 1.4 MB | < 10 KB | Variable |
| POSIX compliance | Partial | Full | No | Full |
| Multicore support | Yes | Yes | Yes | Yes |
| Networking support | Yes | Yes | Yes | Yes |
| Security support | Yes | Yes | No | Yes |
| Graphics support | No | No | No | Yes |
| Filesystem support | Yes | Yes | No | Yes |
| USB support | Yes | Yes | No | Yes |
| Shell support | No | Yes | No | No |

: https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems
: https://www.lynx.com/embedded-systems-learning-center/how-to-choose-a-real-time-operating-system-rtos