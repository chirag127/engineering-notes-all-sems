# I/O Systems for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- I/O systems are the mechanisms that provide uniform access to devices, software stacks, file systems, and other resources in embedded systems and real-time operating systems (RTOS).
- I/O systems can be classified into two types: synchronous and asynchronous.
  - Synchronous I/O systems block the calling thread until the I/O operation is completed, which may cause delays and jitter in real-time applications.
  - Asynchronous I/O systems allow the calling thread to continue execution while the I/O operation is performed in the background, which may improve responsiveness and performance in real-time applications.
- VXWORKS and FREE RTOS are two popular RTOS for embedded systems and real-time applications.
  - VXWORKS is a proprietary RTOS that provides high performance, reliability, safety, and security for the most critical infrastructure's embedded computing systems. It supports C++17, Boost, Rust, Python, pandas, and more, as well as an edge-optimized, OCI-compliant container engine. It has a preemptive, deterministic scheduler that prioritizes real-time tasks and has low latency and minimal jitter.
  - FREE RTOS is an open source RTOS that can be thought of as a thread library rather than an operating system, although command line interface and POSIX-like input/output (I/O) abstraction are available. It implements multiple threads by having the host program call a thread tick method at regular short intervals. It has a cooperative, priority-based scheduler that allows tasks to yield the processor voluntarily or when blocked on an I/O operation.
- Some of the differences between VXWORKS and FREE RTOS in terms of I/O systems are:
  - VXWORKS provides a unified I/O system that supports block, character, network, and memory-mapped devices, as well as pipes, sockets, and message queues. It also provides a virtual file system (VFS) layer that allows applications to access different file systems transparently.
  - FREE RTOS provides a minimal I/O system that supports only character devices, such as serial ports, LCDs, and keyboards. It also provides a simple file system (FFS) layer that supports only FAT file systems.
  - VXWORKS supports asynchronous I/O operations through the asynchronous I/O (AIO) library, which allows applications to submit multiple I/O requests and receive completion notifications through signals, callbacks, or message queues.
  - FREE RTOS does not support asynchronous I/O operations natively, but it can be implemented using tasks, queues, semaphores, and timers.
  - VXWORKS supports advanced I/O features, such as memory mapping, direct I/O, scatter/gather I/O, zero-copy I/O, and DMA I/O.
  - FREE RTOS does not support advanced I/O features natively, but some of them can be implemented using third-party libraries or hardware-specific drivers.