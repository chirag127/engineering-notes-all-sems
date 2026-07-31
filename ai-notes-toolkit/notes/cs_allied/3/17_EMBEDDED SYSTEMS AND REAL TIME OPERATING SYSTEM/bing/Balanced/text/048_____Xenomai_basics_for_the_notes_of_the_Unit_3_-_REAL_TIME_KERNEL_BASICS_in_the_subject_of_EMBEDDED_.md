### Xenomai basics

- Xenomai is a real-time development software framework that cooperates with the Linux kernel to provide hard real-time computing support to user space applications .
- Xenomai allows real-time threads to run either in kernel space or in user space, with the benefit of memory protection and direct scheduling by Xenomai.
- Xenomai uses Linux as a background task that can be preempted by real-time tasks, and provides a dual kernel architecture with a real-time nucleus and a Linux kernel .
- Xenomai supports various real-time interfaces, such as POSIX, RTAI, VxWorks, and others, and provides a unified API for accessing them .
- Xenomai can be installed on a Linux system by patching the kernel with the Xenomai source code and compiling it with the Xenomai configuration options.