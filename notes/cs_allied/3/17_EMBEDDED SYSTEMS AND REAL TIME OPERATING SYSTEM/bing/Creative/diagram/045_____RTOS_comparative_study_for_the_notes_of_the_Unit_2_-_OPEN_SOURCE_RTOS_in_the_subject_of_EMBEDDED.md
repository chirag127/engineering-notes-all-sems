### RTOS comparative study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we will study some of the characteristics and features of different RTOSs and compare them.

Some of the criteria that can be used to compare RTOSs are:

- Size: The size of the RTOS refers to the amount of memory it occupies. A smaller RTOS can be more suitable for embedded systems with limited resources, while a larger RTOS can offer more functionality and features.
- Performance: The performance of the RTOS refers to how fast it can execute tasks, respond to interrupts, and switch between contexts. A higher performance RTOS can provide more predictable and reliable behavior for real-time applications, while a lower performance RTOS can be more prone to delays and jitter.
- Scalability: The scalability of the RTOS refers to how well it can adapt to different hardware platforms, application domains, and workload variations. A more scalable RTOS can support a wider range of devices and applications, while a less scalable RTOS can be more specialized and optimized for a specific use case.
- Standards compliance: The standards compliance of the RTOS refers to how well it conforms to the specifications and guidelines of recognized standards bodies, such as POSIX, ISO, or IEEE. A more standards compliant RTOS can offer more portability, interoperability, and compatibility with other systems and software, while a less standards compliant RTOS can be more proprietary and vendor-specific.
- Licensing: The licensing of the RTOS refers to the terms and conditions under which it can be used, modified, and distributed. A more open and free RTOS can offer more flexibility, transparency, and innovation, while a more closed and proprietary RTOS can offer more security, stability, and support.

Based on these criteria, we can compare some of the popular RTOSs in the market, such as:

- Zephyr: Zephyr is a small, open source RTOS that is designed for IoT devices and supports multiple architectures, such as ARM, x86, RISC-V, and others. It has a minimal configuration of 8KB, which includes threading, interrupts, and memory allocation, but can be extended with additional features, such as Bluetooth, networking, filesystem, and shell. It has a high performance and low latency, and supports various standards, such as POSIX, Bluetooth, and IEEE 802.15.4. It is licensed under the Apache 2.0 license, which allows for commercial and non-commercial use, modification, and distribution.
- LynxOS: LynxOS is a general purpose, POSIX-compliant RTOS that is designed for safety- and security-critical applications, such as aerospace, defense, industrial, and medical. It has a default configuration of 1.4MB, which includes thread and process support, floating point, filesystem, USB, networking, shell, and printf. It has a high performance and determinism, and supports various standards, such as POSIX, ARINC 653, FACE, and MILS. It is licensed under a proprietary license, which requires a fee and a contract for use, modification, and distribution.
- FreeRTOS: FreeRTOS is a popular, open source RTOS that is designed for embedded systems and supports multiple architectures, such as ARM, x86, MIPS, and others. It has a minimal configuration of 9KB, which includes threading, interrupts, timers, queues, and semaphores, but can be extended with additional features, such as networking, filesystem, USB, and shell. It has a high performance and low footprint, and supports various standards, such as POSIX, CMSIS, and MISRA. It is licensed under the MIT license, which allows for commercial and non-commercial use, modification, and distribution.

The following table summarizes the comparison of the RTOSs:

| Criterion | Zephyr | LynxOS | FreeRTOS |
| --- | --- | --- | --- |
| Size | 8KB - 16KB | 1.4MB | 9KB - 40KB |
| Performance | High | High | High |
| Scalability | High | Medium | High |
| Standards compliance | High | High | Medium |
| Licensing | Open | Proprietary | Open |

: https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems

: https://www.lynx.com/embedded-system