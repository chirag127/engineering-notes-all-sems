### Event based real time kernel

- A real-time kernel is a kernel that provides deterministic response times to service events, aiming to minimize the response time guarantee .
- A real-time kernel is also known as kernel-rt or preempt-rt.
- A real-time kernel can be identified by executing the `uname -r` command on the terminal, and then looking for the `rt` keyword in the kernel version.
- A real-time kernel is suitable for applications that have strict timing constraints and require low latency, such as telco, industrial automation, robotics, etc.
- A real-time kernel is different from a standard kernel in the following aspects :
  - A real-time kernel has a higher priority for interrupt handling and task scheduling, which reduces the latency and jitter of the system.
  - A real-time kernel uses a fully preemptible kernel configuration, which allows any kernel code to be preempted by a higher priority task, except for a few critical sections.
  - A real-time kernel implements priority inheritance for kernel spinlocks, which prevents priority inversion and deadlock situations.
  - A real-time kernel supports high-resolution timers, which enable finer-grained timing control and accuracy.
  - A real-time kernel provides additional tuning options and tools for optimizing the system performance and behavior.