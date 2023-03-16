# Clocking

Clocking is the process of measuring and synchronizing the passage of time in a real time kernel. Clocking is essential for scheduling, timing, and performance analysis of real time systems. There are two main types of clocks in a real time kernel:

- **Hardware clock**: This is a battery-backed device that keeps track of the wall clock time (the date and time of the real world) even when the system is powered off. The hardware clock is usually initialized by the BIOS or the bootloader, and can be accessed by the kernel or the user space applications. The hardware clock is also known as the Real Time Clock (RTC), the CMOS clock, or the BIOS clock .
- **Software clock**: This is a virtual device that keeps track of the elapsed time since the system was booted. The software clock is maintained by the kernel using timer interrupts or other sources of time information. The software clock is also known as the system clock, the kernel clock, or the monotonic clock .

The software clock and the hardware clock may have different resolutions, accuracies, and drifts. The software clock may also be affected by system load, frequency scaling, or clock adjustments. Therefore, the kernel may need to synchronize the software clock with the hardware clock periodically, or use other methods to improve the software clock's quality. The kernel may also provide different interfaces for accessing the software clock, such as:

- **CLOCK_REALTIME**: This is a software clock that represents the wall clock time. It can be set or adjusted by the user space applications or the kernel. It may be affected by time zone changes, daylight saving time changes, or leap seconds .
- **CLOCK_MONOTONIC**: This is a software clock that represents the elapsed time since an unspecified point in the past. It cannot be set or adjusted by the user space applications or the kernel. It is not affected by time zone changes, daylight saving time changes, or leap seconds. It is suitable for measuring intervals or durations .
- **CLOCK_REALTIME_HR**: This is a high resolution version of CLOCK_REALTIME. It may have a finer granularity than CLOCK_REALTIME, but it may also have a higher overhead or a lower availability.
- **CLOCK_MONOTONIC_HR**: This is a high resolution version of CLOCK_MONOTONIC. It may have a finer granularity than CLOCK_MONOTONIC, but it may also have a higher overhead or a lower availability.

The kernel may also provide other types of software clocks for specific purposes, such as:

- **CLOCK_PROCESS_CPUTIME_ID**: This is a software clock that measures the CPU time consumed by a process.
- **CLOCK_THREAD_CPUTIME_ID**: This is a software clock that measures the CPU time consumed by a thread.
- **CLOCK_BOOTTIME**: This is a software clock that represents the elapsed time since the system was booted, including the time spent in suspend or hibernation.
- **CLOCK_TAI**: This is a software clock that represents the International Atomic Time, which is a continuous and uniform time scale that does not have leap seconds.

The kernel provides various system calls and functions for accessing and manipulating the software clocks, such as:

- **clock_gettime()**: This function returns the current value of a specified software clock.
- **clock_settime()**: This function sets the current value of a specified software clock.
- **clock_getres()**: This function returns the resolution of a specified software clock.
- **clock_nanosleep()**: This function suspends the execution of the calling thread until a specified software clock reaches a certain value or a certain amount of time has passed.
- **clock_adjtime()**: This function adjusts the frequency or the offset of a specified software clock.
- **timer_create()**: This function creates a timer object that is associated with a specified software clock.
- **timer_settime()**: This function sets the expiration time and the interval of a timer object.
- **timer_gettime()**: This function returns the remaining time and the interval of a timer object.
- **timer_delete()**: This function deletes a timer object.
- **timer_getoverrun()**: This function returns the number of times a timer object has expired without being serviced.

The kernel may also provide other mechanisms for accessing and manipulating the software clocks, such as:

- **/proc/sys/kernel/hz**: This file contains the value of the kernel timer frequency, which is the number