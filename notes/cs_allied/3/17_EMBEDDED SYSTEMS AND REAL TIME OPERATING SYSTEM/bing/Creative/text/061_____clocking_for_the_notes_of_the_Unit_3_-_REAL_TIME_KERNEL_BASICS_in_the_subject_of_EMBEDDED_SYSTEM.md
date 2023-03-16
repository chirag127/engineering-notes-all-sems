### Clocking

- Clocking is the process of measuring and synchronizing the passage of time in a real time kernel.
- A real time kernel is a software component that provides basic services for real time applications, such as task scheduling, interrupt handling, inter-task communication, and synchronization.
- Clocking is essential for a real time kernel to ensure that tasks are executed at the right time, deadlines are met, and events are processed in the correct order.
- There are two main types of clocks in a real time kernel: hardware clocks and software clocks.

#### Hardware clocks

- Hardware clocks are physical devices that generate periodic signals based on a quartz crystal or an atomic oscillator.
- Hardware clocks are also known as Real Time Clocks (RTCs), CMOS clocks, or Hardware clocks.
- Hardware clocks are usually battery-backed and can keep track of time even when the system is powered off.
- Hardware clocks are used to initialize the software clocks when the system boots up, and to synchronize the software clocks with external time sources, such as network time servers or GPS signals.
- Hardware clocks typically have a low resolution (e.g., milliseconds) and a low accuracy (e.g., drifts of a few seconds per day).

#### Software clocks

- Software clocks are logical entities that are maintained by the real time kernel using software algorithms and data structures.
- Software clocks are also known as system clocks, kernel clocks, or software clocks.
- Software clocks are used to measure the elapsed time and the current time while the system is running, and to provide time-related services to the real time applications, such as timers, timeouts, delays, and timestamps.
- Software clocks typically have a high resolution (e.g., nanoseconds) and a high accuracy (e.g., drifts of a few microseconds per day).
- Software clocks are based on hardware clocks, but they can be adjusted by the real time kernel to compensate for the hardware clock errors, or to follow a specific time standard, such as UTC or TAI.

#### Clock sources

- A clock source is a hardware device that provides a reference signal for a software clock.
- A clock source can be either a hardware clock or a high-frequency counter that is incremented by a hardware timer.
- A clock source can have different characteristics, such as frequency, stability, precision, and availability.
- A real time kernel can support multiple clock sources, and select the best one for each software clock, depending on the application requirements and the system configuration.
- Some examples of clock sources are:

  - The RTC, which provides a low-frequency (e.g., 32.768 kHz) and low-precision (e.g., milliseconds) signal that can be used to initialize and synchronize the software clocks.
  - The TSC (Time Stamp Counter), which is a 64-bit register that is incremented by the CPU clock on each cycle, and provides a high-frequency (e.g., GHz) and high-precision (e.g., nanoseconds) signal that can be used to measure the elapsed time and the current time.
  - The HPET (High Precision Event Timer), which is a hardware timer that provides a high-frequency (e.g., MHz) and high-precision (e.g., nanoseconds) signal that can be used to generate periodic interrupts and to measure the elapsed time and the current time.
  - The PIT (Programmable Interval Timer), which is a hardware timer that provides a low-frequency (e.g., kHz) and low-precision (e.g., microseconds) signal that can be used to generate periodic interrupts and to measure the elapsed time and the current time.

#### Clock types

- A clock type is a software abstraction that defines the behavior and the properties of a software clock.
- A clock type can have different attributes, such as resolution, accuracy, monotonicity, adjustability, and continuity.
- A real time kernel can support multiple clock types, and provide different interfaces and services for each clock type, depending on the application needs and the system capabilities.
- Some examples of clock types are:

  - CLOCK_REALTIME, which represents the wall clock time, and is based on the RTC or another external time source. It has a low resolution (e.g., milliseconds) and a low accuracy (e.g., drifts of a few seconds per day). It is not monotonic, meaning that it can jump forward or backward due to time adjustments. It is adjustable, meaning that it can be set or corrected by the user or the system. It is continuous, meaning that it does not stop or wrap around.
  - CLOCK_MONOTONIC, which represents the elapsed time since an arbitrary point in the past