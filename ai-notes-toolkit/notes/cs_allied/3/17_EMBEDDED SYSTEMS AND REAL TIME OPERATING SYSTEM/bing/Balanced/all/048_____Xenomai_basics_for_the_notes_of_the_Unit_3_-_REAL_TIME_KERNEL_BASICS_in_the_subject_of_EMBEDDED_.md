# Xenomai basics

- Xenomai is a software framework that provides hard real-time computing support to user space applications on Linux-based systems .
- Xenomai allows real-time threads to run either in kernel space or in user space, bypassing the Linux scheduler and using the RT-Nucleus scheduler instead .
- Xenomai uses Linux as a background task that can be preempted by any real-time thread .
- Xenomai can be installed by patching the Linux kernel with the I-pipe patch and compiling the Xenomai source code.
- Xenomai provides various APIs for real-time programming, such as POSIX, RTDM, Alchemy, and Cobalt .
- Xenomai threads can switch between primary mode (real-time) and secondary mode (non-real-time) depending on the system state and the services they invoke .