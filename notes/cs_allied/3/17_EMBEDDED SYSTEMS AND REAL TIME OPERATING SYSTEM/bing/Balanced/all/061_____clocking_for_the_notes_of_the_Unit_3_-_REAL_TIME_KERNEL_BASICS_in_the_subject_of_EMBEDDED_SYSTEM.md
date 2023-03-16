# Clocking

Clocking is the process of measuring and synchronizing the passage of time in a real time kernel. Clocking is essential for scheduling, timing, and performance analysis of real time systems. There are two main types of clocks in a real time kernel:

- **Hardware clock**: This is a battery-backed device that keeps track of the wall clock time (the date and time in the real world) even when the system is powered off. The hardware clock is usually initialized by the BIOS or the bootloader, and can be accessed by the kernel or the user space applications. The hardware clock is also known as the Real Time Clock (RTC), the CMOS clock, or the BIOS clock .
- **Software clock**: This is a virtual device that keeps track of the elapsed time since the system was booted. The software clock is maintained by the kernel using timer interrupts, and can be accessed by the kernel or the user space applications. The software clock is also known as the system clock, the kernel clock, or the monotonic clock .

The hardware clock and the software clock may not be synchronized, especially if the system is subject to clock drift, frequency scaling, or time adjustments. Therefore, the kernel provides different interfaces for accessing different types of clocks, such as:

- `clock_gettime()`: This is a system call that returns the current value of a specified clock. The clock can be one of the following constants :
  - `CLOCK_REALTIME`: This is the clock that corresponds to the hardware clock, and reflects the wall clock time. This clock can be set or adjusted by the user or by a network time protocol (NTP) daemon.
  - `CLOCK_MONOTONIC`: This is the clock that corresponds to the software clock, and reflects the elapsed time since the system was booted. This clock cannot be set or adjusted by the user, and is not affected by changes in the hardware clock.
  - `CLOCK_REALTIME_HR`: This is a high resolution version of `CLOCK_REALTIME`, which provides nanosecond precision. This clock may not be available on all platforms.
  - `CLOCK_MONOTONIC_HR`: This is a high resolution version of `CLOCK_MONOTONIC`, which provides nanosecond precision. This clock may not be available on all platforms.
- `gettimeofday()`: This is a system call that returns the current value of the `CLOCK_REALTIME` clock, along with the time zone information. This system call is obsolete and should be replaced by `clock_gettime()`.
- `time()`: This is a library function that returns the current value of the `CLOCK_REALTIME` clock, in seconds since the Unix epoch (January 1, 1970). This function is less precise than `clock_gettime()` and does not provide the time zone information.
- `rtc_read_time()`: This is a kernel function that reads the current value of the hardware clock, and returns it as a `struct rtc_time` structure. This function is used by the kernel to initialize or update the software clock.
- `rtc_set_time()`: This is a kernel function that writes the current value of the software clock to the hardware clock. This function is used by the kernel to synchronize the hardware clock with the software clock.

Clocking is important for real time kernels because it enables the following features:

- **Scheduling**: The kernel uses the software clock to determine when to switch between tasks, and to enforce deadlines and priorities. The kernel also uses the hardware clock to implement periodic or absolute timers, and to wake up tasks that are sleeping or waiting for events.
- **Timing**: The kernel and the user space applications use the clocks to measure the execution time and the latency of tasks, and to generate timestamps and logs. The clocks also help to synchronize the system with external devices or networks that rely on a common time reference.
- **Performance analysis**: The kernel and the user space applications use the clocks to collect and report statistics and metrics about the system's behavior and performance, and to identify and diagnose bottlenecks and anomalies. The clocks also help to compare and evaluate different configurations and algorithms.