### Clocking

Clocking is the process of measuring and synchronizing the passage of time in a real time kernel. Clocking is essential for scheduling, timing, and performance analysis of real time systems. There are two main types of clocks in a real time kernel:

- **Hardware clock**: This is a battery-backed device that keeps track of the wall clock time (the date and time in the real world) even when the system is powered off. The hardware clock is usually initialized by the BIOS or the bootloader, and can be accessed by the kernel or the user space applications. The hardware clock is also known as the Real Time Clock (RTC), the CMOS clock, or the BIOS clock .
- **Software clock**: This is a virtual device that keeps track of the elapsed time since the system was booted. The software clock is maintained by the kernel using timer interrupts or other sources of time information. The software clock is also known as the system clock, the kernel clock, or the monotonic clock .

The software clock and the hardware clock may not be synchronized, especially if the system is subject to clock drift, time zone changes, daylight saving time adjustments, or manual corrections. Therefore, the kernel provides various mechanisms to synchronize the clocks, such as the Network Time Protocol (NTP), the adjtimex system call, or the clock_settime system call .

The kernel also provides various interfaces to access the clocks, such as the clock_gettime system call, the gettimeofday system call, the time system call, or the /proc and /sys file systems   . The kernel supports different clock IDs to specify which clock to use, such as CLOCK_REALTIME, CLOCK_MONOTONIC, CLOCK_BOOTTIME, or CLOCK_PROCESS_CPUTIME_ID  . Each clock may have different properties, such as resolution, precision, accuracy, stability, and drift .

Clocking is important for real time kernels because it affects the following aspects:

- **Scheduling**: The kernel uses the software clock to determine when to switch between tasks, when to run periodic or sporadic tasks, when to enforce deadlines or priorities, and when to handle timer events or signals .
- **Timing**: The kernel and the user space applications use the clocks to measure the duration or frequency of events, to implement delays or timeouts, to generate timestamps or logs, and to coordinate actions or communications  .
- **Performance analysis**: The kernel and the user space applications use the clocks to monitor the resource utilization, the throughput, the latency, the jitter, the overhead, and the quality of service of the real time system  .

Therefore, clocking is a fundamental concept in real time kernel basics.