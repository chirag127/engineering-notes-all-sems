# Monolithic and Microkernel Systems

## Monolithic Kernel

- A monolithic kernel is an operating system architecture where the entire operating system is working in kernel space.
- Kernel space is a privileged memory area that can access hardware directly and execute any instruction.
- A monolithic kernel implements both user services and kernel services under the same address space.
- User services are the functions that are requested by the user applications, such as file system, network, process management, etc.
- Kernel services are the functions that are essential for the kernel to operate, such as memory management, interrupt handling, device drivers, etc.
- A monolithic kernel has the following advantages :
  - It provides high performance, as there is no overhead of switching between user mode and kernel mode.
  - It is easier to implement and debug, as all the components are in one place and can communicate directly.
  - It supports a wide range of device drivers, as they can be loaded and unloaded dynamically into the kernel space.
- A monolithic kernel has the following disadvantages :
  - It is less secure and reliable, as a failure or bug in one component can crash the entire system.
  - It is less modular and flexible, as any change or update in one component requires recompiling and rebooting the whole kernel.
  - It is harder to maintain and extend, as the kernel code becomes large and complex over time.

## Microkernel

- A microkernel is an operating system architecture where the operating system is divided into two parts: a small kernel that runs in kernel space, and a collection of user-level servers that run in user space.
- User space is a non-privileged memory area that can only access hardware through system calls and has limited instructions.
- A microkernel implements only the core kernel services in kernel space, such as memory management, inter-process communication, and low-level hardware access.
- A microkernel implements most of the user services in user space, such as file system, network, process management, etc.
- A microkernel has the following advantages :
  - It is more secure and reliable, as a failure or bug in one user-level server does not affect the other servers or the kernel.
  - It is more modular and flexible, as user-level servers can be added, removed, or updated without affecting the kernel.
  - It is easier to maintain and extend, as the kernel code is small and simple, and the user-level servers can be written in different languages and platforms.
- A microkernel has the following disadvantages :
  - It provides lower performance, as there is more overhead of switching between user mode and kernel mode, and more system calls and message passing.
  - It is harder to implement and debug, as the communication between user-level servers and the kernel is complex and prone to errors.
  - It supports fewer device drivers, as they have to be implemented in user space or as separate servers.

: https://www.educba.com/monolithic-kernel-vs-microkernel/
: https://www.geeksforgeeks.org/monolithic-kernel-and-key-differences-from-microkernel/
: https://techdifferences.com/difference-between-microkernel-and-monolithic-kernel.html
: https://www.geeksforgeeks.org/difference-between-microkernel-and-monolithic-kernel/
: https://en.wikipedia.org/wiki/Monolithic_kernel