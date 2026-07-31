### Event based real time kernel

- An event based real time kernel is a kernel that responds to external events within a specified deadline .
- An event based real time kernel aims to minimize the response time guarantee and provide deterministic behavior .
- An event based real time kernel can be identified by the `rt` keyword in the kernel version.
- An event based real time kernel is suitable for applications that require extreme latency sensitivity, such as telco, industrial automation, and robotics.
- An event based real time kernel can be implemented by applying patches to the standard Linux kernel, such as the PREEMPT_RT patch .
- An event based real time kernel can support different scheduling policies, such as FIFO, RR, and EDF.
- An event based real time kernel can also support features such as priority inheritance, high-resolution timers, and lockless data structures .