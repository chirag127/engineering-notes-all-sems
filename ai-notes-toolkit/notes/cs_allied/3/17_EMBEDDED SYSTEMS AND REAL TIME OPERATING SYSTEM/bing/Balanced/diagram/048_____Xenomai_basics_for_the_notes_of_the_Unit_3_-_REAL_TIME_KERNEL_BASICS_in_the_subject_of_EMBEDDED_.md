### Xenomai basics

- Xenomai is a real-time development software framework that cooperates with the Linux kernel to provide hard real-time computing support to user space applications .
- Xenomai allows real-time threads to run either in kernel space or in user space, with the benefit of memory protection and direct scheduling by Xenomai.
- Xenomai uses Linux as a background task and preempts it as a simple task, making the concept of impossible preemption and handlers obsolete.
- Xenomai consists of three main components: the RT-Nucleus, the RT-Skins, and the RT-Drivers.
  - The RT-Nucleus is the core of Xenomai that provides the real-time services and the scheduling of the real-time threads.
  - The RT-Skins are the interfaces that allow the user space applications to access the real-time services of the RT-Nucleus. They can emulate different real-time APIs, such as POSIX, VxWorks, or RTAI.
  - The RT-Drivers are the device drivers that can operate in real-time mode and communicate with the RT-Nucleus and the RT-Skins.
- Xenomai can be installed on a Linux system by patching the kernel with the Xenomai source code and compiling it with the appropriate configuration options .
- Xenomai can be used to program real-time applications in C or C++ using the RT-Skins APIs and the Xenomai libraries .