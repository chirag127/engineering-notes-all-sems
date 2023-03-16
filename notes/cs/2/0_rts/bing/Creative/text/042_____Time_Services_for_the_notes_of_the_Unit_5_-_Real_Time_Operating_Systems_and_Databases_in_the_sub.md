### Time Services

- Time services are the mechanisms that provide the notion of time and temporal ordering in real-time systems.
- Time services are essential for real-time systems because they enable the specification, verification, and enforcement of timing constraints and deadlines.
- Time services can be classified into two categories: **time representation** and **time synchronization**.
- Time representation is the way of encoding and manipulating the values of time in a system. It can be based on different models, such as physical time, logical time, or hybrid time.
- Physical time is the time measured by physical clocks, such as quartz oscillators or atomic clocks. It is also called wall-clock time or absolute time. Physical time is continuous, linear, and universal.
- Logical time is the time defined by the order of events in a system. It is also called causal time or relative time. Logical time is discrete, partial, and local.
- Hybrid time is the combination of physical and logical time. It is used to capture both the temporal order and the temporal distance of events in a system. Hybrid time is continuous, partial, and local.
- Time synchronization is the process of aligning the clocks of different devices or processes in a system. It can be based on different methods, such as clock skew estimation, clock drift compensation, clock offset correction, or clock agreement.
- Clock skew estimation is the technique of measuring the difference between the clocks of two devices or processes. It can be done by exchanging timestamps or using external reference signals.
- Clock drift compensation is the technique of adjusting the frequency of a clock to match the frequency of a reference clock. It can be done by using feedback control or feedforward control.
- Clock offset correction is the technique of adding or subtracting a constant value to a clock to match the value of a reference clock. It can be done by using one-way or two-way message exchanges.
- Clock agreement is the technique of reaching a consensus on the value of a clock among multiple devices or processes. It can be done by using voting algorithms or averaging algorithms.
- Time services can be implemented in different levels of a system, such as hardware, operating system, middleware, or application.
- Hardware time services are the physical devices that generate and distribute time signals, such as oscillators, timers, counters, or buses.
- Operating system time services are the software components that manage and access the hardware time services, such as clock drivers, interrupt handlers, or system calls.
- Middleware time services are the software components that provide time services to the applications, such as time protocols, time libraries, or time services.
- Application time services are the software components that use the time services to implement the functionality and logic of the applications, such as time stamps, time triggers, or time constraints.

: https://www.geeksforgeeks.org/real-time-systems/
: https://www.intel.com/content/www/us/en/robotics/real-time-systems.html