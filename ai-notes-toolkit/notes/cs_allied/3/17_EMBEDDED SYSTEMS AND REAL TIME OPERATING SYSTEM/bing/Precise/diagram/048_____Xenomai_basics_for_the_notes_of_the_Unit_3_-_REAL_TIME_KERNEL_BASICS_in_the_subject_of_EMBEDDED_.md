### Unit 3 - REAL TIME KERNEL BASICS: Xenomai

- Xenomai is a real-time development software framework that cooperates with the Linux kernel to provide pervasive, interface-agnostic, hard real-time computing support to user space application software seamlessly integrated into the Linux environment .
- The Xenomai project was launched in August 2001 .
- Xenomai allows real-time threads to run either strictly in kernel space or within the address space of a Linux process .
- A real-time task in user space still has the benefit of memory protection, but is scheduled by Xenomai directly, and no longer by the Linux kernel .
- Xenomai is a real-time OS using Linux as a background task. Linux is preempted as a simple task. With Xenomai, the idea of impossible preemption, handlers, is no longer valid .