## Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal delay and predictable response times .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks .
- A real-time kernel supports different scheduling algorithms, such as priority-based, round-robin, or deadline-based, to determine which task should run at any given time .
- A real-time kernel provides mechanisms for inter-task communication and synchronization, such as semaphores, message queues, mutexes, and event flags .
- A real-time kernel can be classified into two types: hard real-time and soft real-time. Hard real-time kernels guarantee that deadlines are always met, while soft real-time kernels allow occasional deadline misses .
- A real-time kernel can be identified by the presence of the rt keyword in the kernel version, which indicates that the kernel has been patched with the PREEMPT_RT patch to reduce the latency and increase the determinism of the system .