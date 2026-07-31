### Clocking

- Clocking is the process of measuring and synchronizing the passage of time in a computer system.
- Clocking is essential for real time kernels, which are operating systems that provide deterministic and predictable response times to events.
- Clocking involves two types of clocks: hardware clocks and software clocks.

#### Hardware clocks

- Hardware clocks are physical devices that generate periodic signals based on a quartz crystal or an atomic oscillator.
- Hardware clocks are also known as Real Time Clocks (RTCs), CMOS clocks, or Hardware Time Sources (HTSs).
- Hardware clocks keep track of the wall clock time, which is the date and time in a specific time zone, even when the system is powered off.
- Hardware clocks are usually battery-backed or powered by a separate power source to maintain accuracy.
- Hardware clocks are accessed by the kernel through special registers or memory-mapped I/O ports.
- Hardware clocks have limited resolution and precision, typically in the range of milliseconds or microseconds.
- Hardware clocks may drift or lose synchronization due to environmental factors, such as temperature, humidity, or magnetic fields.

#### Software clocks

- Software clocks are logical entities that are maintained by the kernel using software algorithms and data structures.
- Software clocks are also known as system clocks, kernel clocks, or software time sources (STSs).
- Software clocks keep track of the monotonic time, which is the elapsed time since an arbitrary point, such as the system boot or the Unix epoch.
- Software clocks are updated by the kernel using interrupts or timers that are triggered by hardware clocks or other sources, such as network protocols or user input.
- Software clocks have higher resolution and precision, typically in the range of nanoseconds or picoseconds.
- Software clocks may be affected by system load, scheduling, or clock adjustments, such as time synchronization or frequency scaling.