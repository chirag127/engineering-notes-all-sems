Hello, I am Sydney, your AI assistant. I can help you with your notes on clocking for the unit 3 of embedded systems and real time operating system. Here is some information that I found from the web:

### Clocking
- Clocking is the process of measuring and synchronizing the passage of time in a system.
- There are two types of clocks in a Linux system: the real time clock (RTC) and the system clock .
- The RTC is a hardware device that keeps track of the wall clock time even when the system is powered off. It is usually battery-backed and does not depend on the local time zone or daylight saving time .
- The system clock is a software abstraction that tracks the elapsed time since the system was booted. It is based on the frequency of a hardware timer and can be adjusted by the kernel or user space applications .
- The system clock can be accessed by different interfaces, such as the `clock_gettime` system call, which provides different clock sources, such as `CLOCK_REALTIME`, `CLOCK_MONOTONIC`, `CLOCK_PROCESS_CPUTIME_ID`, etc .
- The system clock can have different resolutions, depending on the hardware and kernel configuration. The `clock_getres` system call can be used to query the resolution of a given clock source .
- The system clock can be synchronized with the RTC or an external time source, such as a network time protocol (NTP) server, using user space applications, such as `ntpd` or `chrony` .
- Clocking is important for real time kernels, because it affects the scheduling, timing, and performance of real time tasks and applications. A real time kernel should provide accurate and consistent clocking, as well as mechanisms to adjust and synchronize the system clock with external sources .