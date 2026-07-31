### Xenomai basics

- Xenomai is a real-time development software framework that cooperates with the Linux kernel to provide hard real-time computing support to user space applications .
- Xenomai allows real-time threads to run either in kernel space or in user space, with the benefit of memory protection and direct scheduling by Xenomai.
- Xenomai uses Linux as a background task and preempts it as a simple task, making the concept of impossible preemption and handlers obsolete.
- Xenomai consists of three main components: the RT-Nucleus, the RT-IPC and the RT-Skins.
  - The RT-Nucleus is the core of Xenomai that provides the real-time services, such as scheduling, timers, interrupts and synchronization primitives.
  - The RT-IPC is the inter-process communication layer that allows real-time threads to communicate with each other and with Linux processes.
  - The RT-Skins are the interface layers that provide different APIs for real-time programming, such as POSIX, VxWorks, RTAI and native Xenomai.
- Xenomai can be installed on a Linux system by patching the kernel with the Xenomai source code and compiling it with the appropriate configuration options.
- Xenomai provides various tools and libraries for developing and testing real-time applications, such as xeno-config, xeno-test, libxenomai and libalchemy.