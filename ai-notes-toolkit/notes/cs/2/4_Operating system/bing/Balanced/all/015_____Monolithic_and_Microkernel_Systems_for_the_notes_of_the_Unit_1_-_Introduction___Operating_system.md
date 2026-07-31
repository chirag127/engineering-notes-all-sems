# Monolithic and Microkernel Systems

## Monolithic Kernel

- A monolithic kernel is an operating system architecture where the entire operating system is working in kernel space.
- The kernel space is a protected memory area that can only be accessed by the kernel and privileged processes.
- The monolithic kernel provides low-level services such as device drivers, memory management, file system, inter-process communication, etc. as well as high-level services such as system calls, user interface, network protocols, etc. in the same address space  .
- The advantages of a monolithic kernel are:
  - It is fast and efficient, as there is no overhead of switching between user mode and kernel mode.
  - It is simple and easy to implement, as there is no need to design complex communication mechanisms between different modules.
- The disadvantages of a monolithic kernel are:
  - It is large and complex, as it contains many lines of code and functions.
  - It is less secure and reliable, as a bug or error in one module can crash the entire system or compromise its security.
  - It is less modular and flexible, as adding or removing a feature requires recompiling and rebooting the whole kernel.

## Microkernel

- A microkernel is an operating system architecture where the operating system is divided into two parts: a small kernel that runs in kernel space and provides the most basic services, and a collection of user-level servers that run in user space and provide the rest of the services .
- The user space is a non-protected memory area that can be accessed by any process.
- The microkernel provides low-level services such as process management, thread management, inter-process communication, etc. in the kernel space, while the user-level servers provide high-level services such as device drivers, file system, network protocols, system calls, user interface, etc. in the user space .
- The advantages of a microkernel are:
  - It is small and simple, as it contains only the essential functions and code.
  - It is more secure and reliable, as a bug or error in one server does not affect the other servers or the kernel.
  - It is more modular and flexible, as adding or removing a feature does not require recompiling and rebooting the kernel, but only the corresponding server.
- The disadvantages of a microkernel are:
  - It is slow and inefficient, as there is a lot of overhead of switching between user mode and kernel mode, and of communicating between different servers.
  - It is complex and difficult to implement, as it requires designing and maintaining sophisticated communication mechanisms between different modules.

## References

: https://www.educba.com/monolithic-kernel-vs-microkernel/
: https://pediaa.com/what-is-the-difference-between-microkernel-and-monolithic-kernel/
: https://www.geeksforgeeks.org/difference-between-microkernel-and-monolithic-kernel/
: https://en.wikipedia.org/wiki/Monolithic_kernel
: https://www.geeksforgeeks.org/monolithic-kernel-and-key-differences-from-microkernel/