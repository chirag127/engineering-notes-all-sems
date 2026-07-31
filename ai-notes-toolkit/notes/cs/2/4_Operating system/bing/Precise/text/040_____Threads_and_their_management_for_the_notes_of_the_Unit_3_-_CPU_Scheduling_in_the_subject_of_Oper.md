### Threads and their management for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- A thread is a basic unit of CPU utilization, consisting of a program counter, a stack, and a set of registers.
- Threads are sometimes referred to as lightweight processes and they do not require much memory overhead; they are cheaper than processes.
- A thread has or shares with other threads certain resources like code, data, and files.
- Threads can communicate with each other more easily than processes can.
- There are two types of threads: user-level threads and kernel-level threads.
- User-level threads are managed by the user-level library and the kernel is not aware of them.
- Kernel-level threads are managed by the operating system and the kernel is aware of them.
- Thread management involves creating, scheduling, and terminating threads.
- Thread scheduling can be done at the user level or at the kernel level.
- Thread synchronization is important to ensure that threads do not interfere with each other when accessing shared resources.
